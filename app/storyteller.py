from openai import OpenAI
import os

def generate_story(df):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    You are a data analyst. Given this summary of a dataset, write a short business insight report:

    Dataset contains {len(df)} records about startup funding in India.
    Top cities: {df['CityLocation'].value_counts().head(3).to_dict()}
    Top sectors: {df['IndustryVertical'].value_counts().head(3).to_dict()}
    Top investors: {df['InvestorsName'].value_counts().head(3).to_dict()}
    Most common funding types: {df['InvestmentType'].value_counts().head(3).to_dict()}

    Write 3–5 sentences summarizing this data in natural, business-friendly English.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content
