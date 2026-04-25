# AI Usage Report

## Tools Utilized
| Tool          | Purpose |
|---------------|---------|
| ChatGPT       | Initial project skeleton, blueprint code, error debugging |
| GitHub Copilot| Inline code completion (models, routes, forms) |

## AI-Generated vs Manually-Written
| Component / File | Source | Notes |
|------------------|--------|-------|
| Folder layout & `create_app` scaffold | ChatGPT | Prompted: “give me Flask app factory with blueprints” |
| `models.py` base fields | Copilot | We renamed / added status enum manually |
| Rate-limiting decorator | ChatGPT | Accepted mostly as-is |
| Ownership checks (`_verify_author`) | Human | Added after ChatGPT suggestion lacked server check |
| Seed script demo data | Human | Wrote manually to match rubric |

## Example Prompts
1. “Generate a Flask blueprint for user registration with WTForms and bcrypt hashing.”
2. “Add a moderation panel route that lists pending posts and allows publish/remove actions.”

## Parts initially unclear
* Proper SQLAlchemy relationship for `Report → Post`; AI suggested `backref` but we had to adjust `post=pending` syntax when seeding.

## Issues / Limitations Observed
* Copilot sometimes inserted UI-only admin checks; we replaced with server-side 403 responses.  
* ChatGPT omitted CSRF tokens in early form snippets—fixed manually.

