# Contributing to BLACKBOX

Thanks for your interest in BLACKBOX! This public repository is a **limited learning preview**, not the full production or private research codebase.

## Areas where help is valuable

- **AI Copilot evaluation:** Propose questions, expected evidence-grounded behavior, and safe fallback answers. See `docs/COPILOT_EVALUATION_TEMPLATE.md`.
- **Data visualization:** Prototype accessible charts using *fabricated* network metadata.
- **Testing:** Add unit tests and synthetic edge cases for the preview.
- **Documentation / UX:** Make the investigation steps clear to a reader who doesn't know networking.

## Workflow

1. Discuss a narrowly scoped task in an issue before writing major code.
2. Work in your own branch, and open a pull request explaining what changed and how you tested it.
3. Never add secrets, real packet captures, private logs, customer metadata, or personal information.
4. Do not claim that unusual traffic automatically proves a malicious attack.
5. Project owner reviews and merges approved changes.

## Privacy and credit

Public synthetic test data only. The private parser, proprietary detection engine, Copilot prompts/integration, credentials, and nonpublic case evidence are not part of this repo. Contributors should be credited for their work in the Thirduni presentation, with permission.
