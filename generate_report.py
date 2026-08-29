from datetime import datetime

report = f"""
GitHub Actions Report
=====================

Generated at: {datetime.now()}

Status: Success

This file was generated automatically by Python
inside a GitHub Actions workflow.
"""

with open("report.txt", "w") as file:
    file.write(report)

print("report.txt created successfully")
