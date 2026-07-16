"""A job that failed for a past cohort. Submit it, read the error log, fix it.

Hint: it runs fine on a laptop where the output folder already exists — but a
fresh SLURM job on a compute node starts with nothing set up for you.
"""

import json

record = {"insider_name": "Jane Doe", "role": "Director", "company": "Acme Corp"}

# Save the extracted record.
with open("results/last_year.json", "w") as f:
    json.dump(record, f, indent=2)

print("Wrote results/last_year.json")
