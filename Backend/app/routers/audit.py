from fastapi import APIRouter
from app.services.scraper import WebsiteScraper
from app.services.llm_service import LLMService
from app.services.geo_checker import GEOChecker
from app.schemas.audit_request import AuditRequest
from app.schemas.audit_response import AuditResponse

router = APIRouter()


@router.post(
    "/audit",
    response_model=AuditResponse,
)
async def audit(request: AuditRequest):

    website = WebsiteScraper.scrape(str(request.url))

    result = GEOChecker.analyze(website)

    ai_report = LLMService.generate_report(
    result
)

    return AuditResponse(
            success=True,
            score=result["score"],
            findings=result["findings"],
            ai_report=ai_report,
        )