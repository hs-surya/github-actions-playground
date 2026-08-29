import json
import os
import urllib.request


repository = os.getenv("GITHUB_REPOSITORY")
token = os.getenv("GITHUB_TOKEN")

if not repository:
    raise ValueError("GITHUB_REPOSITORY is missing")

if not token:
    raise ValueError("GITHUB_TOKEN is missing")


url = f"https://api.github.com/repos/{repository}"

request = urllib.request.Request(
    url,
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "github-actions-api-demo",
    },
)

with urllib.request.urlopen(request) as response:
    data = json.loads(response.read().decode())


report = f"""
GitHub Repository API Report
============================

Repository: {data["full_name"]}
Description: {data.get("description")}
Default branch: {data["default_branch"]}
Visibility: {data["visibility"]}
Open issues: {data["open_issues_count"]}
Stars: {data["stargazers_count"]}
Forks: {data["forks_count"]}
GitHub URL: {data["html_url"]}
"""

print(report)

with open("github-api-report.txt", "w") as file:
    file.write(report)

print("github-api-report.txt created successfully")
