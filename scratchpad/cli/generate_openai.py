import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk_test_123",
)
for i in range(1):
    res = client.chat.completions.create(
        model="meta-llama/Llama-3.2-1B-Instruct",
        messages=[
            {
                "role": "user",
                "content": "Alan Turing is",
            }
        ],
        temperature=0.7,
        max_tokens=50,
        top_p=0.9,
    )
    print(res)
