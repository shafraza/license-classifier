import httpx

API_KEY = "API_SECRET_KEY"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

async def classify_license(description):
    system_prompt = (
        "Classify this software into one of: "
        "Productivity, Design, Communication, Development, Finance, Marketing. "
        "Respond with JSON: {\"category\": ..., \"explanation\": ... (150 chars max)}"
    )

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": description}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=HEADERS, json=payload)
        return response.json()
