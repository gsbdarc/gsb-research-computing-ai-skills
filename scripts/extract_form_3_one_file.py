import os
import json
from openai import OpenAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

# Load API key from .env in repo root
load_dotenv()
client = OpenAI(
    base_url="https://aiapi-prod.stanford.edu/v1",
    api_key=os.getenv("STANFORD_API_KEY"),
)

# Filing to process — swap this path for any Form 3 .txt file
FILING_PATH = "data/sec_filings/form3_sample.txt"
OUTPUT_PATH = "results/form3_result.json"

with open(FILING_PATH, "r") as f:
    filing_text = f.read()


class Form3Filing(BaseModel):
    insider_name: str
    insider_role: List[str]
    company_name: str
    company_cik: str
    filing_date: str


system_prompt = """
You are a data extraction agent for SEC Form 3 filings.

Extract the following fields:
- insider_name: The name of the insider (from reportingOwner or anywhere in the document).
- insider_role: A list of roles the insider holds (Director, Officer, 10% Owner, Other).
- company_name: The issuer's company name.
- company_cik: The CIK number of the issuer (from issuerCik or COMPANY DATA).
- filing_date: The filing date (prefer signatureDate or FILED AS OF DATE).

Return valid JSON matching the schema exactly.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": filing_text},
    ],
)

result = Form3Filing.model_validate_json(response.choices[0].message.content)

os.makedirs("results", exist_ok=True)
with open(OUTPUT_PATH, "w") as f:
    json.dump(result.model_dump(), f, indent=2)

print(result.model_dump())
print(f"\nSaved to {OUTPUT_PATH}")
