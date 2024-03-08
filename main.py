import argparse
import os

import openai
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

from src.modules.query_augmenter import augment_multiple_query, augment_query_generated
from src.modules.rag import rag
from src.modules.text_processor import get_vector_db_reference

url = "https://classics.mit.edu/Homer/iliad.mb.txt"

parser = argparse.ArgumentParser(description="RAG based question answering.")
parser.add_argument(
    "--query", type=str, help="The query string for which you want to find an answer."
),


_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]

openai_client = OpenAI()

# collection_reference = process_text_from_url(url)
# print(collection_reference)  # Use the reference to the collection as needed

args = parser.parse_args()

query = args.query

chroma_collection = get_vector_db_reference()

# aug_query = augment_query_generated(query,openai_client)
aug_query = augment_multiple_query(query, openai_client)

# print(collection_reference, type(collection_reference))
print("XXX", aug_query)

results = chroma_collection.query(query_texts=[aug_query], n_results=5)

retrieved_documents = results["documents"][0]


information = "\n\n".join(retrieved_documents)

print("information:", information)

print("reponse finale:", rag(query, information, chroma_collection, openai_client))
