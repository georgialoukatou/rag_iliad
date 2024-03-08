def rag(query, information, collection, openai_client, model="gpt-3.5-turbo"):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful librarian. Your users are asking questions about information contained in the poem of Iliad."
            "You will be shown the user's question, and the relevant information from the Iliad text. Answer the user's question using only this information. If the answer is not mentioned in the text or you are not sure, say that you don't know. Pay attention to negations. If the information given does not answer the question, say I don't know ",
        },
        {
            "role": "user",
            "content": f"Question: {query}. \n Information: {information}",
        },
    ]
    response = openai_client.chat.completions.create(
        model=model, messages=messages, top_p=0.1, temperature=0
    )

    content = response.choices[0].message.content
    return content
