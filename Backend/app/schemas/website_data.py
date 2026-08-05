from pydantic import BaseModel
from typing import List


class WebsiteData(BaseModel):
    url: str

    title: str | None = None

    meta_description: str | None = None

    canonical: str | None = None

    headings: List[str] = []

    paragraphs: List[str] = []

    json_ld: List[str] = []

    robots_exists: bool = False

    sitemap_exists: bool = False