export interface Finding {
    name: string;
    status: "PASS" | "WARNING" | "FAIL";
    score: number;
    evidence: string;
}

export interface AIReport {
    summary: string;
    strengths: string[];
    weaknesses: string[];
    recommendations: string[];
}

export interface AuditResponse {
    success: boolean;
    score: number;
    findings: Finding[];
    ai_report: AIReport;
}