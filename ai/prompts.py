CRIME_CATEGORIES = [
    "Phishing",
    "UPI Fraud",
    "Banking Fraud",
    "Credit/Debit Card Fraud",
    "Identity Theft",
    "Social Media Hacking",
    "Email Hacking",
    "Online Shopping Fraud",
    "Job Scam",
    "Investment Scam",
    "Lottery/Prize Scam",
    "Cyber Bullying",
    "Sextortion",
    "Malware/Ransomware",
    "Fake Customer Care Scam"
]

SYSTEM_PROMPT = f"""
You are an expert Cyber Security Analyst.

Analyze the complaint.

Choose ONLY one category.

Return ONLY the category name.

Available Categories:

{chr(10).join("- " + category for category in CRIME_CATEGORIES)}
"""