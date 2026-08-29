import os
from datetime import datetime

report_title = os.getenv("REPORT_TITLE")
api_key = os.getenv("DEMO_API_KEY")

if not report_title:
    raise ValueError("REPORT_TITLE is missing")

if not api_key:
    raise ValueError("DEMO_API_KEY is missing")

report = f"""
{report_title}
{"=" * len(report_title)}

Generated at: {datetime.now()}

Configuration status:
- REPORT_TITLE loaded successfully
- DEMO_API_KEY loaded successfully
- Secret length: {len(api_key)} characters

The secret value itself is not displayed.
"""

with open("config-report.txt", "w") as file:
    file.write(report)

print(report)
