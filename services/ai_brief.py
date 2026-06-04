# =============================================
# BriefOS — AI-powered incident brief generator
# services/ai_brief.py
# Core analysis engine powered by Claude API
# =============================================

import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))


def generate_brief(incident_notes, org_name="", incident_type=""):
    """
    Convert rough incident notes into a structured executive brief.
    Returns structured JSON result.
    """

    context_lines = []
    if org_name:
        context_lines.append(f"Organisation: {org_name}")
    if incident_type:
        context_lines.append(f"Incident type: {incident_type}")
    context_block = "\n".join(context_lines) if context_lines else "No additional context provided."

    prompt = f"""You are a senior cybersecurity incident response consultant. 
Your job is to take rough, messy incident notes and convert them into a clean, professional executive brief.

Additional context:
{context_block}

Incident notes:
{incident_notes}

You MUST reply with ONLY a valid JSON object. No prose, no markdown, no explanation.
Return exactly this structure:

{{
  "incident_title": "short descriptive title for the incident",
  "severity": "CRITICAL or HIGH or MEDIUM or LOW",
  "status": "Ongoing or Contained or Resolved or Under Investigation",
  "executive_summary": "2-3 sentences a non-technical executive can understand. What happened, what was affected, what is being done.",
  "timeline": [
    {{
      "time": "approximate time or date if known, otherwise sequence e.g. T+0h",
      "event": "what happened at this point"
    }}
  ],
  "business_impact": {{
    "operational": "impact on business operations",
    "financial": "potential or confirmed financial impact",
    "reputational": "reputational risk",
    "regulatory": "any compliance or regulatory implications"
  }},
  "technical_summary": "2-3 sentences on what technically occurred, written for a technical audience",
  "affected_systems": [
    "list of affected systems, services or data"
  ],
  "actions_taken": [
    "list of response actions already taken"
  ],
  "next_actions": [
    {{
      "action": "what needs to be done",
      "owner": "who should own this e.g. IT team, Legal, CISO",
      "priority": "Immediate or 24h or 72h or This week"
    }}
  ],
  "escalation_recommendation": "one sentence — should this be escalated further and to whom",
  "lessons_learned": [
    "any early lessons or observations from the incident"
  ]
}}

Be specific. Use information from the notes. Fill in reasonable assumptions where details are missing but flag them clearly.
Order timeline events chronologically. Keep executive summary free of jargon."""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw = response.content[0].text

    try:
        clean = raw.strip()
        if clean.startswith("```"):
            clean = clean.split("```")[1]
            if clean.startswith("json"):
                clean = clean[4:]
        return json.loads(clean.strip())
    except json.JSONDecodeError:
        return {
            "incident_title": "Parse Error",
            "severity": "UNKNOWN",
            "status": "Unknown",
            "executive_summary": "Analysis failed — could not parse AI response.",
            "timeline": [],
            "business_impact": {},
            "technical_summary": "",
            "affected_systems": [],
            "actions_taken": [],
            "next_actions": [],
            "escalation_recommendation": "Manual review required.",
            "lessons_learned": [],
            "raw_response": raw
        }
