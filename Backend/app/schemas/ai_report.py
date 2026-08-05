from pydantic import BaseModel


class AIReport(BaseModel):
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]