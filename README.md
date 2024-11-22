### Fonctionnalités
- Télécharge un fichier PDF à partir d’un bucket S3 spécifié.
- Extrait le texte des pages du PDF.
- Stocke le résultat dans un fichier local vault.txt.
- Interroger un model IA avec comme contexte le texte du pdf.
- AVEC un mode RAG (avec un contexte ) ou SANS mode RAG (sans contexte).
- Modifier la temperature du model.

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

    AWS_ACCESS_KEY=votre_aws_access_key
    AWS_SECRET_KEY=votre_aws_secret_key
    BUCKET_NAME=votre_bucket_name
    FILE_KEY=votre_pdf.pdf
    REGION_NAME=votre_aws_region 
    TEMPERATURE=temperature 
    
6. pip install -r requirements.txt
7. Install Ollama (https://ollama.com/download)
8. ollama pull llama3
9. ollama pull mxbai-embed-large

### **Utilisation**

## Upload le texte du PDF

bash

`python upload.py`

### **Mode sans RAG**

Dans ce mode, les questions sont posées directement au modèle, sans utiliser de contexte supplémentaire :

bash

`python localrag.py --model llama3`

### **Mode avec RAG**

Dans ce mode, les réponses sont générées en utilisant le contenu de `vault.txt` comme contexte :

bash

`python localrag.py --model llama3 --use_rag`

### **Modifier la temperature du model**

Dans le fichier .env, modifié la temperature:

1. Faible température (ex. : 0.2 - 0.7) :

  Les réponses seront plus cohérentes et déterministes.
  Le modèle privilégiera les mots ou phrases les plus probables dans un contexte donné.
  Utile pour des tâches nécessitant des réponses précises et répétables (par exemple, des réponses techniques ou des explications factuelles).

2. Température moyenne (ex. : 0.7) :

  Balance entre cohérence et créativité.
  Les réponses sont un peu plus variées, mais restent assez fiables.

3. Température élevée (ex. : 1 ou plus) :

  Les réponses deviennent plus créatives et parfois moins cohérentes.
  Le modèle choisit plus souvent des alternatives moins probables, ce qui peut donner des idées nouvelles ou surprenantes.


### Auteur
Alexandre Vital


