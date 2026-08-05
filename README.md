# 🌐 GEO Auditor

> AI-powered Generative Engine Optimization (GEO) auditing platform that analyzes websites for AI search readiness and provides actionable recommendations.

## 📖 Overview

GEO Auditor helps website owners evaluate how well their websites are optimized for modern AI-powered search engines and LLMs such as ChatGPT, Gemini, Claude, and Perplexity.

Unlike traditional SEO tools that focus on search engine rankings, GEO Auditor evaluates websites from the perspective of generative AI systems by inspecting technical signals, structured content, and AI-friendly best practices.

---

## ✨ Features

- 🔍 Website Technical Audit
- 🤖 AI-generated Website Analysis
- 📊 GEO Score (0–100)
- 📋 Technical Findings
- 💡 Actionable Recommendations
- ⚡ FastAPI Backend
- ⚛️ React + TypeScript Frontend
- 🌐 REST API
- 🚀 Vercel Deployment Ready

---

# Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Axios
- CSS

## Backend

- FastAPI
- BeautifulSoup
- Requests
- Gemini API
- Pydantic

---

# Project Structure

```
GEO_Auditor/
│
├── Backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── Frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── types/
│   │   ├── styles/
│   │   └── App.tsx
│   │
│   ├── public/
│   ├── .env
│   └── package.json
│
└── README.md
```

---

# How It Works

```
                 User
                   │
                   ▼
         React Frontend (Vercel)
                   │
                   ▼
         FastAPI Backend (Vercel)
                   │
     ┌─────────────┴──────────────┐
     ▼                            ▼
Website Crawling            Gemini API
     │                            │
     └─────────────┬──────────────┘
                   ▼
           GEO Audit Report
                   │
                   ▼
             React Dashboard
```

---

# Audit Workflow

The application performs the following steps:

1. User submits a website URL.
2. Backend crawls the website.
3. Extracts:
   - HTML
   - Title
   - Meta Description
   - Headings
   - Structured Data
   - Robots.txt
   - Sitemap
4. Performs GEO checks.
5. Calculates technical score.
6. Sends extracted information to OpenAI.
7. Generates:
   - Summary
   - Strengths
   - Weaknesses
   - Recommendations
8. Returns complete audit report.

---

# API Endpoint

### Audit Website

```
POST /api/v1/audit
```

Request

```json
{
    "url":"https://example.com"
}
```

Response

```json
{
  "score": 82,
  "findings": [
    {
      "name": "Title Tag",
      "status": "PASS",
      "score": 10,
      "evidence": "Title tag detected."
    }
  ],
  "ai_report": {
    "summary": "...",
    "strengths": [],
    "weaknesses": [],
    "recommendations": []
  }
}
```

---

# Environment Variables

## Backend

```
GEMINI_API_KEY=your_api_key
MODEL=gemini-3.5-flash
```

---

## Frontend

```
VITE_API_BASE_URL=http://localhost:8000
```

Production

```
VITE_API_BASE_URL=https://geo-auditorbackend.vercel.app/
```

---

# Local Setup

## Backend

```bash
cd Backend

python -m venv venv

source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd Frontend

npm install

npm run dev
```

---

# Deployment

## Frontend

Hosted on

- Vercel

Environment Variable

```
VITE_API_BASE_URL=https://geo-auditorbackend.vercel.app/
```

---

## Backend

Hosted on

- Vercel

Allowed Origins

```python
allow_origins = [
    "http://localhost:5173",
    "https://geo-auditor-tan.vercel.app",
]
```

---

# Current GEO Checks

- Page Title
- Meta Description
- Heading Structure
- Robots.txt
- Sitemap.xml
- Structured Data
- AI Summary

---

# Future Improvements

- Authentication
- User Dashboard
- Audit History
- PDF Report Export
- Batch Website Audits
- Scheduled Audits
- AI Competitor Comparison
- GEO Trend Analysis
- Shareable Reports
- Multi-language Support

---

# Roadmap

### MVP ✅

- Website Crawl
- Technical GEO Audit
- AI Report
- React Dashboard
- FastAPI API

### Phase 2

- User Accounts
- Saved Reports
- Database Integration
- Background Jobs
- Email Reports

### Phase 3

- Team Workspace
- Subscription Plans
- Public API
- Chrome Extension
- Enterprise Dashboard

---

# Learning Outcomes

This project demonstrates practical experience with:

- FastAPI
- REST API Design
- React + TypeScript
- Axios
- Environment Variables
- API Integration
- OpenAI API
- BeautifulSoup
- Web Crawling
- Prompt Engineering
- CORS
- Deployment on Vercel

---

# Author

**Aniket Kumar Baghel**

Backend Developer | Python | FastAPI | AI Applications

---

# License

MIT License
