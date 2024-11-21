### Fonctionnalités
- Télécharge un fichier PDF à partir d’un bucket S3 spécifié.
- Extrait le texte des pages du PDF.
- Stocke le résultat dans un fichier local vault.txt.
- Interroger un model IA avec comme contexte le texte du pdf.

### Prérequis
- Python 3.6 ou supérieur.
- ollama
- Les bibliothèques suivantes doivent être installées :
  boto3
  PyPDF2
  python-dotenv
- Un bucket S3 contenant le fichier PDF que vous souhaitez traiter.

### Installation

1. git clone https://github.com/alexvtl/chatpdfollama.git
2. cd repository
3. pip install boto3 PyPDF2 python-dotenv
4. créer bucket s3 et inserer pdf de votre choix.
5. créer un fichier .env avec les accées au bucket:

    AWS_ACCESS_KEY=your_aws_access_key
    AWS_SECRET_KEY=your_aws_secret_key
    BUCKET_NAME=your_bucket_name
    FILE_KEY=your_pdf.pdf
    REGION_NAME=your_aws_region 
    
6. pip install -r requirements.txt
7. Install Ollama (https://ollama.com/download)
8. ollama pull llama3
9. ollama pull mxbai-embed-large
10. python upload.py
11. python localrag.py (with query re-write)
12. python localrag_no_rewrite.py (no query re-write)


### Auteur
Alexandre Vital


