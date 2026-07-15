# ai/regex_filter.py

import re


def redact_sensitive_data(text):

    # Phone Number (10 digits)
    text = re.sub(
        r"\b[6-9]\d{9}\b",
        "[PHONE_NUMBER]",
        text
    )

    # Aadhaar Number (12 digits)
    text = re.sub(
        r"\b\d{4}\s?\d{4}\s?\d{4}\b",
        "[AADHAAR]",
        text
    )

    # PAN Number
    text = re.sub(
        r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",
        "[PAN]",
        text
    )

    # Email Address
    text = re.sub(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "[EMAIL]",
        text
    )

    # UPI ID
    text = re.sub(
        r"\b[\w.-]+@[\w]+\b",
        "[UPI_ID]",
        text
    )

    # Bank Account Number (9–18 digits)
    text = re.sub(
        r"\b\d{9,18}\b",
        "[BANK_ACCOUNT]",
        text
    )

    # Debit/Credit Card Number
    text = re.sub(
        r"\b(?:\d{4}[- ]?){3}\d{4}\b",
        "[CARD_NUMBER]",
        text
    )

    # IFSC Code
    text = re.sub(
        r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
        "[IFSC]",
        text
    )

    return text