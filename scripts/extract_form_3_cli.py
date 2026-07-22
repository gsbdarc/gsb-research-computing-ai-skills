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
from pathlib import Path
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
    filing_path = Path(sys.argv[1])     # 1st argument: the filing to process
    output_path = Path(sys.argv[2])     # 2nd argument: where to write the result

    # Already processed? Skip it. This makes the array safe to resubmit after a
    # partial failure: finished tasks exit instantly, only the missing ones rerun.
    if output_path.exists():
        print(f"{output_path} already exists — skipping")
        return

    # API key comes from .env in the repo root
    load_dotenv()
    client = OpenAI(
        base_url="https://aiapi-prod.stanford.edu/v1",
        api_key=os.getenv("STANFORD_API_KEY"),
    )

    filing_text = filing_path.read_text()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": filing_text},
        ],
    )

    result = Form3Filing.model_validate_json(response.choices[0].message.content)

    # Create the output directory if needed, then write the result
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result.model_dump(), indent=2))

    print(f"Saved {output_path}")


if __name__ == "__main__":
    main()
