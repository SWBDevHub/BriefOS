# =============================================
# BriefOS — AI-powered incident brief generator
# app.py
# =============================================

import os
from flask import Flask, render_template, request
from services.ai_brief import generate_brief

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'static'))


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    incident_notes = request.form.get("incident_notes", "").strip()
    org_name = request.form.get("org_name", "").strip()
    incident_type = request.form.get("incident_type", "").strip()

    if not incident_notes:
        return render_template("index.html", error="Please paste some incident notes to analyse.")

    result = generate_brief(incident_notes, org_name, incident_type)

    return render_template(
        "result.html",
        result=result,
        incident_notes=incident_notes,
        org_name=org_name,
        incident_type=incident_type
    )


if __name__ == "__main__":
    app.run(debug=True)
