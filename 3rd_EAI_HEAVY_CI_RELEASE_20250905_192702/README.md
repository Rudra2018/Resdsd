
# 3rd EAI — HEAVY CI Release

This repository is wired so that when you **push to GitHub** and run the included **GitHub Actions workflow**, it will:
1) Install and pin **all heavy security tools** (amass/subfinder/naabu/dnsx/httpx/nuclei/katana/sqlmap/ffuf/gobuster/trivy/wpscan/tshark/zsteg/wafw00f/volatility3/grpcurl).
2) Fetch and vendor **SecLists** and **nuclei-templates**.
3) Export a single **release ZIP (>100 MB)** that includes `vendor/*` plus this full codebase (backend, UI, Dockerfiles, agents, templates).

> This approach satisfies your “nothing to do on local” requirement: **GitHub builds and publishes** the heavy ZIP automatically.

## Quick use (no local building)
1. Create an **empty GitHub repo** and push this folder.
2. In GitHub → Actions → **Run workflow** for “HEAVY Release Builder” (or push a git tag like `v1.0.0`).
3. Wait for the job to finish → the release asset named `3rd_EAI_HEAVY_FULL_<date>.zip` appears under **Releases**.

The runtime ZIP contains:
- `/vendor/bin/` → all heavy CLI tools (Linux x86_64) gathered from CI runner and Go builds
- `/vendor/seclists/` → full SecLists bundle
- `/vendor/nuclei-templates/` → latest templates
- `/services/*`, `/apps/*`, `/frontend/*` → full 3rd EAI app (FastAPI + Vue + ZAP sidecar)
- `/templates/` → Jinja2 PoC/report templates
- `/agents/` → CrewAI agents (crawler, PoC synthesizer, report QA) + LangGraph-style workflow config

> If you prefer GCP instead of GitHub: use `cloudbuild.yaml` (included) to produce the same ZIP to a GCS bucket via **Cloud Build**.

Security note: Use only on targets you are authorized to test.
