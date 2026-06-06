# BriefOS

AI-powered incident brief generator. Paste rough incident notes. Get a clean executive brief.

## What it does

BriefOS takes messy, unstructured incident notes and converts them into a structured executive brief covering:

- **Severity & status** — incident classification and current state
- **Executive summary** — plain English overview a non-technical executive can act on
- **Timeline** — reconstructed chronological sequence of events
- **Business impact** — operational, financial, reputational, and regulatory exposure
- **Technical summary** — what happened under the hood
- **Affected systems** — what was compromised or at risk
- **Actions taken** — what's already been done
- **Next actions** — prioritised table with owners and deadlines
- **Escalation recommendation** — whether and where to escalate
- **Early lessons** — observations flagged for post-incident review

## Why it exists

Incident response is chaotic. Notes are messy, timelines are incomplete, and writing up a clean brief for leadership takes time that responders don't have. BriefOS converts raw notes into a professional brief in seconds — reducing report writing from hours to nothing.

## Demo

![BriefOS input page](https://raw.githubusercontent.com/SWBDevHub/BriefOS/main/static/screenshots/input.png)
![BriefOS result page 1](https://raw.githubusercontent.com/SWBDevHub/BriefOS/main/static/screenshots/result1.png)
![BriefOS result page 2](https://raw.githubusercontent.com/SWBDevHub/BriefOS/main/static/screenshots/result2.png)

## Tech stack

- **Python / Flask** — web framework
- **Anthropic Claude API** — AI analysis engine (claude-haiku-4-5)
- **Jinja2** — templating
- **HTML / CSS** — dark, clean UI

## Getting started

**1. Clone the repo**
```bash
git clone https://github.com/SWBDevHub/BriefOS.git
cd BriefOS
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Create a `.env` file in the root:
```
ANTHROPIC_API_KEY=your_key_here
```

Get a key at [console.anthropic.com](https://console.anthropic.com)

**4. Run**
```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Project structure

```
briefos/
├── app.py                  # Flask routes
├── services/
│   └── ai_brief.py         # Claude API integration, structured JSON output
├── templates/
│   ├── index.html          # Input page
│   └── result.html         # Brief output page
├── static/
│   └── style.css           # Dark UI styling
└── requirements.txt
```

## Skills demonstrated

- AI workflow design — structured prompt engineering with enforced JSON output schema
- Cybersecurity domain knowledge — incident response, business impact assessment, escalation paths
- API integration — Anthropic Claude API
- Full-stack Python — Flask, Jinja2, REST routing
- Risk communication — translating technical incidents into executive-ready output

## Limitations & future work

This is a v0.1 prototype built for portfolio and learning purposes.

Planned additions:
- PDF export of generated briefs
- Incident history and log
- Multi-user support with role-based views
- Integration with ticketing systems (Jira, ServiceNow)
- Automated stakeholder email drafting

## Disclaimer

BriefOS generates AI-assisted incident briefs. Always verify content before sharing with executives or stakeholders. Not a substitute for professional incident response.
