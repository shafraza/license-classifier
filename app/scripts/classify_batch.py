import asyncio
from app.services.groq_client import classify_license
from app.utils.excel_handler import load_licenses, save_classified_licenses

async def classify_all():
    df = load_licenses("data/input.xlsx")

    for i, row in df.iterrows():
        result = await classify_license(row["License Description"])
        parsed = result['choices'][0]['message']['content']
        # Assume content is a JSON string
        data = eval(parsed)  # safer: use `json.loads` if it's proper JSON
        df.at[i, "category"] = data["category"]
        df.at[i, "explanation"] = data["explanation"]

    save_classified_licenses(df)

if __name__ == "__main__":
    asyncio.run(classify_all())
