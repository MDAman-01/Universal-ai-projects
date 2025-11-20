response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an intelligent AI assistant. Answer all questions clearly, step-by-step, and correctly."},
        {"role": "user", "content": user_message}
    ]
)
