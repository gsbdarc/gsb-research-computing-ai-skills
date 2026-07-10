---
layout: default
title: "The Scales"
parent: "Day 3 — The SLURM Mines"
nav_order: 6
permalink: /day3/scales/
---

# The Scales

<div data-room-id="d3-scales"></div>

---

## Optional Exercises

{: .note }
> Finished early? Try one or both of these.

**Bonus 1 — Verbose time**

The `/usr/bin/time -v` command gives much more detail than the shell `time` builtin:

```bash
/usr/bin/time -v python scripts/extract_form_3_one_file.py
```

Find the line that says **"Maximum resident set size"** in the output. This is the peak RAM the process held at any point. How does it compare to what you saw in `htop`?

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="side1"> I used /usr/bin/time -v and found the peak memory (maximum resident set size)</label>

**Bonus 2 — Scaling estimate**

Edit `scripts/extract_form_3_batch.py` to process only 5 filings. Find the line that builds the URL list and add a slice:

```python
urls = [u for u in urls if u.endswith(".txt")][:5]
```

Time it. Then try 10. Does the time scale roughly linearly? Based on that, estimate how long processing all 994 filings would take.

<label class="quest-check"><input type="checkbox" data-room="d3-scales" data-key="side2"> I estimated scaling: how long would processing all 994 filings take?</label>
