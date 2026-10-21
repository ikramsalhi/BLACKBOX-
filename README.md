# BLACKBOX 🧩
### Evidence-first AI Network Incident Investigator

**From raw network observations to a traceable investigation.**

BLACKBOX is a local-first cybersecurity investigation project built for the **Thirduni team challenge**. Its goal is to help analysts and students make sense of suspicious traffic with clear timelines, references to technical evidence, and an optional AI Copilot that explains *observations and uncertainties*, not invented attack stories.

> **Public preview — limited release.** This repository contains a small, runnable demonstration on *synthetic packet metadata*. It is **not** the complete BLACKBOX application, does not ingest PCAP files, and does not include the private investigation engine or DeepSeek integration.

## What the broader project aims to do
d

1. **Import evidence:** organize network captures and associated case metadata.
2. **Explore the network:** visualize communication patterns, packets, and notable events.
3. **Surface investigation leads:** flag heuristic anomalies with packet references and alternative explanations.
4. **Ask the AI Copilot:** get evidence-grounded answers about an investigation, while respecting data boundaries.
5. **Produce reports:** preserve findings, source identity, timestamps and limitations for review.

The full prototype is under private development; these modules are **not** implemented by the small sample in this repository.

## Try the public sample (Python 3.10+)

No dependencies, no external API, no network calls and no real captures required.

```bash
python demo/preview.py demo/synthetic_case.json
python -m unittest discover -s tests -v
```

The script reads a deliberately fabricated eight-packet metadata set, counts protocols, and creates **unverified investigation leads** for two illustrative patterns:

- Several TCP destination ports contacted by one source in a short period (possible port sweep).
- Conflicting ARP MAC ownership claims for a single IP address (ARP identity inconsistency).

Findings include packet IDs so the user can inspect the underlying observations. **Neither rule proves an attack.** The preview does not parse actual PCAPs, decrypt traffic, correlate real-world incidents, or invoke AI.

## Project direction

| Area | Goal |
| --- | --- |
| Backend | Python, FastAPI, SQLite and local-first case processing |
| Investigation | PCAP/PCAPNG analysis, evidence-linked findings and packet explorer |
| AI | Optional DeepSeek or local-provider Copilot; avoid unsupported conclusions |
| Experience | Guided investigation workflow, network relationships, case reporting |

These describe the wider project, not features offered by this public demo.

## Responsible use and privacy

- Do not upload customer traffic, real PCAPs, credentials or sensitive logs to this repository.
- An `.env` file or API key must never be committed. `.gitignore` is only one safeguard; review staged changes and commit history too.
- Network metadata can still contain sensitive information. Use only synthetic or explicitly authorized captures.
- BLACKBOX is an **educational prototype**, not a certified forensic tool or production SOC replacement.
- Any future publicly hosted demonstration should use a separate synthetic, read-only environment; unrestricted public uploads are not supported here.

## Collaborating on the Thirduni challenge

Contributors interested in network analytics, evidence-grounded AI explanations, testing and accessible interface design are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and work through a feature branch and pull request. For AI collaborators, there is a ready-to-use [Copilot evaluation worksheet](docs/COPILOT_EVALUATION_TEMPLATE.md).

**Project lead:** [@ikramsalhi](https://github.com/ikramsalhi)

**License:** No open-source license has been granted yet. Please ask permission before copying, redistributing, or reusing the code outside this project.
