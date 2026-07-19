"""Extract structured fields from a single SEC Form 3 filing.

Unlike ``extract_form_3_one_file.py`` (which hard-codes its paths), this version
takes the filing path and output path as command-line arguments. That makes it
callable once per filing — for example from a SLURM job array, where each task
passes a different filing:

    python scripts/extract_form_3_cli.py path/to/filing.txt results/filing.json
"""

import os
import sys
import json
from typing import List

from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv


class Form3Filing(BaseModel):
    insider_name: str
    insider_role: List[str]
    company_name: str
    company_cik: str
    filing_date: str


SYSTEM_PROMPT = """
You are a data extraction agent for SEC Form 3 filings.

Extract the following fields:
- insider_name: The name of the insider (from reportingOwner or anywhere in the document).
- insider_role: A list of roles the insider holds (Director, Officer, 10% Owner, Other).
- company_name: The issuer's company name.
- company_cik: The CIK number of the issuer (from issuerCik or COMPANY DATA).
- filing_date: The filing date (prefer signatureDate or FILED AS OF DATE).

Return valid JSON matching the schema exactly.
"""


def main():
    filing_path = sys.argv[1]     # 1st argument: the filing to process
    output_path = sys.argv[2]     # 2nd argument: where to write the result

    # API key comes from .env in the repo root
    load_dotenv()
    client = OpenAI(
        base_url="https://aiapi-prod.stanford.edu/v1",
        api_key=os.getenv("STANFORD_API_KEY"),
    )

    with open(filing_path, "r") as f:
        filing_text = f.read()

    response = client.chat.completions.create(
        model="gpt-5.2",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": filing_text},
        ],
    )

    result = Form3Filing.model_validate_json(response.choices[0].message.content)

    # Create the output directory if needed, then write the result
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result.model_dump(), f, indent=2)

    print(f"Saved {output_path}")


if __name__ == "__main__":
    main()
