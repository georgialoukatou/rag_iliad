def rag(query, information, collection, openai_client, model="gpt-3.5-turbo"):   

    messages = [
        {
            "role": "system",
            "content": "Answer the question based only on the text provided. The text provided contains extracts from Iliad."
        },
        {"role": "user", "content": f"Question: {query}. \n Information: {information}"}
    ]
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    
    content = response.choices[0].message.content
    return content

                # "content": "You are illiad expert, provide an answer for the questions"
