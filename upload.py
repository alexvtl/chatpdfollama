import PyPDF2
import re
import boto3
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def process_pdf_from_s3(aws_access_key_id, aws_secret_access_key, bucket_name, file_key, region_name):
    # Configurez le client S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("REGION_NAME", region_name)
    )

    # Téléchargez le fichier PDF depuis S3
    local_file_path = '/tmp/temp_pdf_file.pdf'
    s3.download_file(bucket_name, file_key, local_file_path)
    print(f"Fichier {file_key} téléchargé depuis le bucket {bucket_name}.")

    # Extraction du texte du fichier PDF
    with open(local_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        text = ''

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            if page.extract_text():
                text += page.extract_text() + " "

        text = re.sub(r'\s+', ' ', text).strip()

        
        sentences = re.split(r'(?<=[.!?]) +', text)
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            if len(current_chunk) + len(sentence) + 1 < 1000:
                current_chunk += (sentence + " ").strip()
            else:
                chunks.append(current_chunk)
                current_chunk = sentence + " "
        if current_chunk:
            chunks.append(current_chunk)

        # Enregistrez les morceaux de texte dans un fichier local
        with open("vault.txt", "a", encoding="utf-8") as vault_file:
            for chunk in chunks:
                vault_file.write(chunk.strip() + "\n")

        print(f"Contenu du fichier {file_key} ajouté à vault.txt.")

# Variables pour le bucket S3 et le fichier
AWS_ACCESS_KEY=os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY=os.getenv("AWS_SECRET_KEY")
REGION_NAME=os.getenv("REGION_NAME")
BUCKET_NAME = os.getenv("BUCKET_NAME")
FILE_KEY = os.getenv("FILE_KEY")

process_pdf_from_s3(AWS_ACCESS_KEY,AWS_SECRET_KEY, BUCKET_NAME, FILE_KEY, REGION_NAME)