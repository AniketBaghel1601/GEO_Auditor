from app.schemas.website_data import WebsiteData
from app.schemas.audit_response import Finding
from app.utils.enums import CheckStatus


class GEOChecker:

    @staticmethod
    def _add_finding(
        findings: list[Finding],
        name: str,
        status: CheckStatus,
        score: int,
        evidence: str,
    ):
        findings.append(
            Finding(
                name=name,
                status=status,
                score=score,
                evidence=evidence,
            )
        )

    @staticmethod
    def analyze(data: WebsiteData):

        findings: list[Finding] = []
        score = 0

        # Title
        if data.title:
            GEOChecker._add_finding(
                findings,
                "Title Tag",
                CheckStatus.PASS,
                10,
                f"Title found: {data.title}",
            )
            score += 10
        else:
            GEOChecker._add_finding(
                findings,
                "Title Tag",
                CheckStatus.FAIL,
                0,
                "Title tag missing",
            )

        # Meta Description
        if data.meta_description:
            GEOChecker._add_finding(
                findings,
                "Meta Description",
                CheckStatus.PASS,
                10,
                data.meta_description,
            )
            score += 10
        else:
            GEOChecker._add_finding(
                findings,
                "Meta Description",
                CheckStatus.FAIL,
                0,
                "Meta description missing",
            )

        # Canonical
        if data.canonical:
            GEOChecker._add_finding(
                findings,
                "Canonical URL",
                CheckStatus.PASS,
                10,
                data.canonical,
            )
            score += 10
        else:
            GEOChecker._add_finding(
                findings,
                "Canonical URL",
                CheckStatus.FAIL,
                0,
                "Canonical URL missing",
            )

        # Robots
        if data.robots_exists:
            GEOChecker._add_finding(
                findings,
                "robots.txt",
                CheckStatus.PASS,
                15,
                "robots.txt found",
            )
            score += 15
        else:
            GEOChecker._add_finding(
                findings,
                "robots.txt",
                CheckStatus.FAIL,
                0,
                "robots.txt missing",
            )

        # Sitemap
        if data.sitemap_exists:
            GEOChecker._add_finding(
                findings,
                "Sitemap",
                CheckStatus.PASS,
                15,
                "sitemap.xml found",
            )
            score += 15
        else:
            GEOChecker._add_finding(
                findings,
                "Sitemap",
                CheckStatus.FAIL,
                0,
                "sitemap.xml missing",
            )

        # Structured Data
        if data.json_ld:
            GEOChecker._add_finding(
                findings,
                "Structured Data",
                CheckStatus.PASS,
                20,
                f"{len(data.json_ld)} JSON-LD block(s) found",
            )
            score += 20
        else:
            GEOChecker._add_finding(
                findings,
                "Structured Data",
                CheckStatus.WARNING,
                0,
                "No JSON-LD schema found",
            )

        # Heading Structure
        if len(data.headings) >= 3:
            GEOChecker._add_finding(
                findings,
                "Heading Structure",
                CheckStatus.PASS,
                10,
                f"{len(data.headings)} headings found",
            )
            score += 10
        else:
            GEOChecker._add_finding(
                findings,
                "Heading Structure",
                CheckStatus.WARNING,
                5,
                "Few headings detected",
            )
            score += 5

        # Content Quality
        total_words = sum(len(p.split()) for p in data.paragraphs)

        if total_words > 300:
            GEOChecker._add_finding(
                findings,
                "Content Quality",
                CheckStatus.PASS,
                10,
                f"{total_words} words detected",
            )
            score += 10

        elif total_words > 100:
            GEOChecker._add_finding(
                findings,
                "Content Quality",
                CheckStatus.WARNING,
                5,
                f"{total_words} words detected",
            )
            score += 5

        else:
            GEOChecker._add_finding(
                findings,
                "Content Quality",
                CheckStatus.FAIL,
                0,
                f"Only {total_words} words detected",
            )

        return {
            "score": score,
            "findings": findings,
        }