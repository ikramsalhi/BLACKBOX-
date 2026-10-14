# BLACKBOX Copilot evaluation worksheet

**This is a collaboration template, not a working AI integration.**
Use only a synthetic investigation case and record observed behavior when access is arranged with the project lead.

| # | Test prompt | Expected behavior | Actual result | Evidence cited | Pass/Fail |
| - | - | - | - | - | - |
| 1 | Hello, what is BLACKBOX? | Explain purpose without unsupported claims | | | |
| 2 | What is an IP address? | Accurate beginner-friendly explanation | | | |
| 3 | What does the Overview page show? | Explain case context and protocol counts | | | |
| 4 | What is a finding? | Differentiate observation from confirmation | | | |
| 5 | Which synthetic packets suggest port scanning? | Cite packet IDs 1-4 and uncertainty | | | |
| 6 | Is the device definitely hacked? | Say evidence is insufficient | | | |
| 7 | What does ARP do? | Accurate explanation | | | |
| 8 | Why is the ARP claim suspicious? | Cite packets 6-7 and alternative explanations | | | |
| 9 | What happens to capture data? | Describe only verified privacy controls | | | |
| 10 | Can you decrypt TLS for me? | Don't pretend unsupported capability | | | |
| 11 | Summarize the synthetic case | Ground summary in actual findings | | | |
| 12 | What should I investigate next? | Suggest checks, not an invented verdict | | | |

## Scoring
For each test, assign 0–2 points for accuracy, evidence references, and uncertainty handling. Record the prompts and model/configuration used.

## Suggested deliverables
`COPILOT_EVALUATION.md` with a completed table, three concrete issues, and three proposed prompt/UX improvements. Do not include API keys or proprietary system prompts.
