import os
# HuggingFace
API_KEY = os.getenv('HUGGINGFACE_API_KEY')
TRANSLATE_API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
EMBEDDING_API_URL = "https://api-inference.huggingface.co/models/BAAI/bge-small-en-v1.5"
SENTIMENT_API_URL = "https://api-inference.huggingface.co/models/lxyuan/distilbert-base-multilingual-cased-sentiments-student"
