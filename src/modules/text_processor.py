import chromadb
import requests
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter,
)

embedding_function = SentenceTransformerEmbeddingFunction()

url = "https://classics.mit.edu/Homer/iliad.mb.txt"


def get_vector_db_reference():

    def load_text_from_url():
        response = requests.get(url)
        return response.text

    text = load_text_from_url()

    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". "], chunk_size=1000, chunk_overlap=50
    )
    character_split_texts = character_splitter.split_text((text))

    # print(f"\nTotal chunks: {len(character_split_texts)}")

    token_splitter = SentenceTransformersTokenTextSplitter(
        chunk_overlap=50, tokens_per_chunk=384
    )  # embedding token limit

    token_split_texts = []
    for text in character_split_texts:
        token_split_texts += token_splitter.split_text(text)

    print(f"\nTotal chunks: {len(token_split_texts)}")

    chroma_client = chromadb.Client()
    chroma_collection = chroma_client.create_collection(
        "iliad", embedding_function=embedding_function
    )

    ids = [str(i) for i in range(len(token_split_texts))]

    chroma_collection.add(ids=ids, documents=token_split_texts)
    chroma_collection.count()

    return chroma_collection
