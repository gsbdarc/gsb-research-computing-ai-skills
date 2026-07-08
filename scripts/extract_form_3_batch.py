import os
import json
import glob
from openai import OpenAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://aiapi-prod.stanford.edu/v1",
    api_key=os.getenv("STANFORD_API_KEY"),
)

FILINGS_DIR = "data/sec_filings"
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)


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

filings = sorted(glob.glob(os.path.join(FILINGS_DIR, "*.txt")))
total = len(filings)
print(f"Found {total} filings in {FILINGS_DIR}")

for idx, filing_path in enumerate(filings, 1):
    filename = os.path.basename(filing_path)
    output_path = os.path.join(RESULTS_DIR, filename.replace(".txt", ".json"))

    print(f"[{idx}/{total}] Processing: {filename}")

    with open(filing_path, "r") as f:
        filing_text = f.read()

    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": filing_text},
        ],
    )

    result = Form3Filing.model_validate_json(response.choices[0].message.content)

    with open(output_path, "w") as f:
        json.dump(result.model_dump(), f, indent=2)

    print(f"  → saved {output_path}")

print(f"\nDone. {total} filings processed.")
