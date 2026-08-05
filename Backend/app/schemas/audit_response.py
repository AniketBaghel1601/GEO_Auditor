from pydantic import BaseModel
from typing import List
from app.schemas.ai_report import AIReport
from app.utils.enums import CheckStatus


class Finding(BaseModel):
    name: str
    status: CheckStatus
    score: int
    evidence: str


class AuditResponse(BaseModel):
    success: bool
    score: int
    findings: list[Finding]
    ai_report: AIReport
