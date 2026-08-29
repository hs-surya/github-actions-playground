import os
import sys

api_key = os.getenv("DEMO_API_KEY")

if not api_key:
    print("DEMO_API_KEY was not found.")
    sys.exit(1)

print("Secret loaded successfully.")
print(f"Secret length: {len(api_key)} characters")
