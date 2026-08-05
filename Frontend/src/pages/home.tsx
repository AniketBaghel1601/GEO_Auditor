import { useState } from "react";
import { api } from "../services/api";
import "../styles/home.css";
import type { AuditResponse } from "../types/audit";

export default function Home() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AuditResponse | null>(null);

  async function handleAudit() {
    if (!url) return;

    setLoading(true);

    try {
      const response = await api.post<AuditResponse>(
        "/audit",
        {
          url,
        }
      );

      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Audit failed");
    }

    setLoading(false);
  }

  return (
  <div className="container">
    <h1 className="title">GEO Auditor</h1>

    <p className="subtitle">
      AI Powered Website GEO Analysis
    </p>

    <div className="search-box">
      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="https://example.com"
      />

      <button
        onClick={handleAudit}
        disabled={loading}
      >
        {loading ? "Auditing..." : "Audit"}
      </button>
    </div>

    {result && (
      <>
        <div className="score-card">
          <h2>Overall Score</h2>

          <div className="score">
            {result.score}/100
          </div>
        </div>

        <h2 className="section-title">
          Technical Findings
        </h2>

        {result.findings.map((finding) => (
          <div
            key={finding.name}
            className="finding-card"
          >
            <h3>{finding.name}</h3>

            <span
              className={`badge ${finding.status.toLowerCase()}`}
            >
              {finding.status}
            </span>

            <p>
              <strong>Score:</strong> {finding.score}
            </p>

            <p>{finding.evidence}</p>
          </div>
        ))}

        <div className="ai-card">
          <h2>AI Summary</h2>

          <p>{result.ai_report.summary}</p>

          <h3>Strengths</h3>

          <ul>
            {result.ai_report.strengths.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>

          <h3>Weaknesses</h3>

          <ul>
            {result.ai_report.weaknesses.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>

          <h3>Recommendations</h3>

          <ul>
            {result.ai_report.recommendations.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </>
    )}
  </div>
);
}