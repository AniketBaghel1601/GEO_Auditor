import json

from google import genai
from fastapi import HTTPException

from app.config import settings
from app.schemas.ai_report import AIReport

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


class LLMService:

    @staticmethod
    def generate_report(
        analysis: dict
    ) -> AIReport:

        score = analysis["score"]
        findings = analysis["findings"]

        findings_text = "\n".join(
            [
                f"- {finding.name}: "
                f"{finding.status.value} "
                f"(Score: {finding.score}) "
                f"Evidence: {finding.evidence}"
                for finding in findings
            ]
        )

        prompt = f"""
You are an expert in Generative Engine Optimization (GEO).

Analyze the following website audit.

Overall Score:
{score}/100

Technical Findings:
{findings_text}

Return ONLY valid JSON.

The JSON MUST exactly match this schema:

{{
    "summary": "string",
    "strengths": ["string"],
    "weaknesses": ["string"],
    "recommendations": ["string"]
}}

Rules:
1. Return ONLY JSON.
2. Do NOT wrap the JSON in markdown.
3. Do NOT include explanations outside the JSON.
4. Do NOT invent information.
5. Base every conclusion only on the provided findings.
6. Recommendations should be specific and actionable.
7. If no strengths or weaknesses exist, return an empty list.
"""

        try:

            response = client.models.generate_content(
                model=settings.MODEL,
                contents=prompt,
            )

            text = response.text.strip()

            if text.startswith("```"):
                text = text.split("\n", 1)[1]

            if text.endswith("```"):
                text = text[:-3]

            text = text.strip()

            return AIReport.model_validate(
                json.loads(text)
            )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Gemini Error: {str(e)}"
            )