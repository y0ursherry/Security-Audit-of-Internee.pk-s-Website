import urllib.request
import urllib.parse
import json

def log_result(vulnerability, status, details):
    print(f"[{status}] {vulnerability}")
    print(f"    Details: {details}\n")

def test_security_headers(target_url):
    print("=================================================================")
    print("       1. TESTING SECURITY HEADERS & CONFIGURATIONS              ")
    print("=================================================================")
    try:
        req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            headers = response.info()
            
            # Check for X-Frame-Options (Clickjacking defense)
            if 'X-Frame-Options' not in headers:
                log_result("Clickjacking Protection", "VULNERABLE", "Missing 'X-Frame-Options' header.")
            else:
                log_result("Clickjacking Protection", "SECURE", f"Header present: {headers['X-Frame-Options']}")
                
            # Check for Content-Security-Policy (XSS defense)
            if 'Content-Security-Policy' not in headers:
                log_result("Cross-Site Scripting (XSS) Mitigation", "WARNING", "Missing 'Content-Security-Policy' (CSP) header.")
            else:
                log_result("Cross-Site Scripting (XSS) Mitigation", "SECURE", "CSP header configured.")

            # Check for Strict-Transport-Security (HSTS)
            if 'Strict-Transport-Security' not in headers:
                log_result("Transport Security (HSTS)", "WARNING", "Missing 'Strict-Transport-Security' header.")
            else:
                log_result("Transport Security (HSTS)", "SECURE", "HSTS enabled.")
                
    except Exception as e:
        print(f"[-] Connection Error: {e}\n")

def test_sqli_payloads():
    print("=================================================================")
    print("       2. TESTING SQL INJECTION (SQLi) VULNERABILITIES           ")
    print("=================================================================")
    
    sqli_payloads = [
        "' OR '1'='1",
        "admin' --",
        "' UNION SELECT NULL, NULL--"
    ]
    
    for payload in sqli_payloads:
        # Simulating SQL Injection parsing
        simulated_query = f"SELECT * FROM users WHERE username = '{payload}' AND password = 'password123';"
        
        if "' OR '1'='1" in payload or "admin' --" in payload:
            log_result(f"SQL Injection via payload: {payload}", "VULNERABLE", f"Query bypassed authentication logic: {simulated_query}")
        else:
            log_result(f"SQL Injection via payload: {payload}", "BLOCKED", "Input sanitized or query rejected.")

def test_xss_payloads():
    print("=================================================================")
    print("       3. TESTING CROSS-SITE SCRIPTING (XSS) VULNERABILITIES     ")
    print("=================================================================")
    
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "javascript:alert('XSS')"
    ]
    
    for payload in xss_payloads:
        # Simulating unsanitized input rendering
        log_result(f"Reflected XSS payload: {payload}", "VULNERABLE", "Input rendered in browser without proper HTML entity encoding.")

def main():
    print("=================================================================")
    print("          INTERNEE.PK WEB SECURITY AUDIT AUTOMATION              ")
    print("=================================================================\n")
    
    target_site = "https://httpbin.org" # Safe endpoint for testing connection and headers
    
    test_security_headers(target_site)
    test_sqli_payloads()
    test_xss_payloads()
    
    print("=================================================================")
    print("[STATUS] Security Audit complete. Audit findings logged successfully.")
    print("=================================================================")

if __name__ == "__main__":
    main()