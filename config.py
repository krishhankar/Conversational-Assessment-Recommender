from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
MODEL_NAME = os.getenv('MODEL_NAME', 'gemini-2.5-flash')
CHROMA_DB = BASE_DIR / os.getenv('CHROMA_DB', 'data/chroma_db')
CATALOG_PATH = BASE_DIR / os.getenv('CATALOG_PATH', 'data/shl_product_catalog.json')
TOP_K = int(os.getenv('TOP_K', 10))

