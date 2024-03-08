from src.modules.rag import rag
import openai
import os
from openai import OpenAI
from src.modules.query_augmenter import augment_multiple_query, augment_query_generated
from src.modules.text_processor import chroma_collection

from dotenv import load_dotenv, find_dotenv

url = 'https://classics.mit.edu/Homer/iliad.mb.txt'


_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

openai_client = OpenAI()

# collection_reference = process_text_from_url(url)
# print(collection_reference)  # Use the reference to the collection as needed

##args 

query = "Who killed Hector and how?"
# query = "How did the Greeks enter in Troy?"
# query = "How did Achilles die?" 
# query = "Who fought against Hyrtius son of Gyrtius?"

# aug_query_plus_answer = augment_query_generated(query,openai_client)
# aug_query_mult_query = augment_multiple_query(query, openai_client)

# print(aug_query_mult_query)
# print(aug_query_plus_answer)
# print(collection_reference, type(collection_reference))
results = chroma_collection.query(query_texts=[query], n_results=5)

retrieved_documents = results['documents'][0]

information = "\n\n".join(retrieved_documents)

# print("information:", information)

print("reponse finale:", rag(query, information, chroma_collection,openai_client))