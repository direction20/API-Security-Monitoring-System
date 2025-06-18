# app/security_rules.py
import re
from fastapi import Request

SQLI_PATTERNS = [r"(?i)(union.*select)", r"(?i)(or 1=1)", r"(?i)(--|#)"]
XSS_PATTERNS = [r"<script.*?>", r"javascript:"]

async def check_request_for_attacks(request: Request):
    body = await request.body()
    body_text = body.decode() if body else ""

    for pattern in SQLI_PATTERNS + XSS_PATTERNS:
        if re.search(pattern, body_text):
            return f"Attack Detected: {pattern}"
    return None
