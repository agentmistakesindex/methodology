# Agent Mistakes Index

The Agent Mistakes Index is an independent test of consumer AI shopping agents available in the United States. Round 1 covers 6 agents and 8 shopping tasks, with real orders placed where a task allows. We compare what each agent was asked to do, what it said it did, and what the receipts show it actually did.

Results are expected in mid-November 2026. They will be published with the raw run log and redacted evidence (screenshots, screen recordings, order emails) so anyone can re-score the runs.

## The method

The full method is in [METHODOLOGY.md](METHODOLOGY.md): the agents, the exact prompts, the scoring rules and weights, and how each run is recorded. It was published before any Round 1 test was run. Any later change is listed in its changelog with a date and a reason, and this repository's commit history shows every edit.

## The second-scorer lottery

A second person, who does not run the tests, scores a random 30% of runs from the evidence alone. We do not choose which runs they get.

- The sample is drawn from a secret seed. Its SHA-256 fingerprint is published in METHODOLOGY.md, so the seed cannot be swapped later.
- [select_sample.py](select_sample.py) is the drawing method. It was published before the first run.
- When results are published, we reveal the seed. Anyone can then check it against the fingerprint and run:

```
python3 select_sample.py --seed <SEED> run_ids.txt
```

where `run_ids.txt` lists the run IDs from the published run log, one per line. The script needs only Python 3 and prints the same 30% sample we used.

## Report an error

Open an [issue](https://github.com/agentmistakesindex/methodology/issues) in this repository, or email agentmistakesindex@gmail.com. Confirmed errors are fixed publicly within 48 hours and noted in the changelog.

## Independence

The test is self-funded. There are no sponsors, no ads and no affiliate links. We accept no money, free credits, review units or other benefits from agent makers, retailers, merchants or payment companies.

## Licence

Data and evidence: CC BY 4.0, with credit to "Agent Mistakes Index".
