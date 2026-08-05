import requests

from bs4 import BeautifulSoup

from app.schemas.website_data import WebsiteData


class WebsiteScraper:

    @staticmethod
    def scrape(url: str) -> WebsiteData:

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/138.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        # Title
        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else None
        )

        # Meta Description
        meta_description = None

        meta = soup.find("meta", attrs={"name": "description"})

        if meta:
            meta_description = meta.get("content")

        # Canonical URL
        canonical = None

        canonical_tag = soup.find(
            "link",
            attrs={"rel": "canonical"}
        )

        if canonical_tag:
            canonical = canonical_tag.get("href")

        # H1 + H2
        headings = [
            tag.get_text(strip=True)
            for tag in soup.find_all(["h1", "h2"])
        ]

        # First 10 paragraphs
        paragraphs = [
            p.get_text(strip=True)
            for p in soup.find_all("p")[:10]
        ]

        # JSON-LD
        json_ld = [
            script.string
            for script in soup.find_all(
                "script",
                attrs={"type": "application/ld+json"},
            )
            if script.string
        ]

        # robots.txt
        robots = requests.get(
            url.rstrip("/") + "/robots.txt",
            headers=headers,
        )

        # sitemap.xml
        sitemap = requests.get(
            url.rstrip("/") + "/sitemap.xml",
            headers=headers,
        )

        return WebsiteData(
            url=url,
            title=title,
            meta_description=meta_description,
            canonical=canonical,
            headings=headings,
            paragraphs=paragraphs,
            json_ld=json_ld,
            robots_exists=robots.status_code == 200,
            sitemap_exists=sitemap.status_code == 200,
        )