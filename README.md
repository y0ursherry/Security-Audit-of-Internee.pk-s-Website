# Security-Audit-of-Internee.pk-s-Website
# Task 5:  Web Security Audit & Penetration Testing Report

This repository contains a security audit report and automated vulnerability testing script for web applications (referencing OWASP Top 10 vulnerabilities like SQL Injection, Reflected XSS, and missing Security Headers). Conducted as part of my Cybersecurity Internship at Internee.pk.

## Security Audit Summary
- **Target Assessments:** Security Headers, Input Sanitation, Authentication Vectors.
- **Vulnerabilities Tested:**
  - **SQL Injection (SQLi):** Identified bypass risks on unsanitized authentication forms.
  - **Cross-Site Scripting (XSS):** Analyzed missing output encoding mechanisms.
  - **Missing Headers:** Evaluated missing `X-Frame-Options` (Clickjacking risk) and `Content-Security-Policy` (XSS mitigation).

## How to Run the Security Audit Script

```bash
python audit.py
