#!/usr/bin/env python3
"""Agent Mistakes Index - second-scorer sample selection (Round 1).

Published before Round 1 testing. The seed stays private until results day;
its SHA-256 fingerprint is in METHODOLOGY.md.

Rule:
  1. Every run has an ID of the form  <task>-<agent>-p<pass>
     task  = t01 t02 t03 t04 t06 t07 t08 t10
     agent = muse alexa google-gemini google-aimode copilot perplexity chatgpt
     pass  = 1, or 2 for the planned second pass
     e.g.  t10-copilot-p2
  2. Each run's rank = SHA-256( seed + "|" + run_id ), read as a hex number.
  3. Sort the scored runs (all runs in the published CSV that received a score,
     including "could not complete") by rank, lowest first.
  4. The second scorer gets the first ceil(30% x number of scored runs).

Because the rank of any run ID is fixed by the seed, which was committed to
before testing, the sample cannot be chosen after seeing results.

Usage (results day):
  python3 select_sample.py --seed <SEED> run_ids.txt
  (run_ids.txt: one run ID per line, i.e. the run_id column of the CSV)
"""
import argparse, hashlib, math, re, sys

FINGERPRINT = "a7a94d19b5eff967112f8ad35cde13fc5a14dde6297a6af19dc463f4c7e8d94c"
ID_RE = re.compile(r"^t(01|02|03|04|06|07|08|10)-(muse|alexa|google-gemini|google-aimode|copilot|perplexity|chatgpt)-p[12]$")

def rank(seed: str, run_id: str) -> int:
    return int(hashlib.sha256(f"{seed}|{run_id}".encode("utf-8")).hexdigest(), 16)

def select(seed: str, run_ids):
    ids = sorted(set(r.strip().lower() for r in run_ids if r.strip()))
    bad = [r for r in ids if not ID_RE.match(r)]
    if bad:
        sys.exit(f"Invalid run IDs: {bad}")
    k = math.ceil(0.30 * len(ids))
    return sorted(ids, key=lambda r: rank(seed, r))[:k]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", required=True)
    p.add_argument("run_ids_file")
    a = p.parse_args()
    fp = hashlib.sha256(a.seed.encode("utf-8")).hexdigest()
    print(f"SHA-256(seed) = {fp}")
    print("Matches published fingerprint:", fp == FINGERPRINT)
    with open(a.run_ids_file) as f:
        sample = select(a.seed, f)
    print(f"Second-scorer sample ({len(sample)} runs):")
    for r in sample:
        print(r)

if __name__ == "__main__":
    main()
