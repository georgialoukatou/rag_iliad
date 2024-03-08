def augment_multiple_query(query, openai_client, model="gpt-3.5-turbo"):
    messages = [
        {
            "role": "system",
            "content": "You serve as an assistant specializing in history, particularly the Iliad. "
            "Users seek answers about this epic. Your task is to propose supplementary questions related to their queries, aiding them in gathering necessary information."
            "Your suggestions should be concise, covering various aspects of the topic, and fully-formed questions. Ensure the questions are closely linked to the original query.",
        },
        {"role": "user", "content": query},
    ]

    response = openai_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    content = response.choices[0].message.content
    content = content.split("\n")
    return [query] + content


def augment_query_generated(query, openai_client, model="gpt-3.5-turbo"):
    messages = [
        {
            "role": "system",
            "content": "You are illiad expert, provide a hypothetical answer for the question. Focus on specific names and facts that happened in the Iliad.",
        },
        {"role": "user", "content": query},
    ]

    response = openai_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    content = response.choices[0].message.content
    return f"{query} {content}"
