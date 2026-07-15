QUESTION_BANK = {

    "Phishing": [
        "What is the phishing website or URL?",
        "How did you receive the phishing link (Email, SMS, WhatsApp, etc.)?",
        "When did you receive it?",
        "Did you click the link?",
        "Did you enter any personal information?",
        "Were any passwords or OTPs shared?",
        "Upload screenshots or emails."
    ],

    "UPI Fraud": [
        "Which UPI application did you use?",
        "What is the Transaction ID?",
        "How much money was lost?",
        "What is the Receiver UPI ID?",
        "Which bank account is linked?",
        "When did the transaction happen?",
        "Upload the payment screenshot."
    ],

    "Banking Fraud": [
        "Which bank account was affected?",
        "How much money was lost?",
        "Was your debit or credit card involved?",
        "Did you receive any OTP or verification message?",
        "Have you contacted your bank?",
        "Transaction date and time?",
        "Upload bank transaction proof."
    ],

    "Credit/Debit Card Fraud": [
        "Is it a Credit Card or Debit Card?",
        "Last four digits of your card?",
        "Did you lose the card or was it cloned?",
        "Amount involved?",
        "Merchant or website name?",
        "Transaction date?",
        "Upload transaction proof."
    ],

    "Identity Theft": [
        "Which identity document was misused?",
        "Where do you suspect it was used?",
        "When did you discover the issue?",
        "Did you share your documents online?",
        "Have you reported it to any authority?",
        "Upload supporting documents."
    ],

    "Social Media Hacking": [
        "Which social media platform was hacked?",
        "What is your username?",
        "Registered email address?",
        "Registered phone number?",
        "When was the account hacked?",
        "Have you tried recovering the account?",
        "Upload screenshots."
    ],

    "Email Hacking": [
        "Which email provider do you use?",
        "What is your email address?",
        "When was the account compromised?",
        "Can you still access your account?",
        "Did you receive any suspicious login alerts?",
        "Have you changed your password?",
        "Upload screenshots."
    ],

    "Online Shopping Fraud": [
        "Which shopping website or app was used?",
        "What product did you purchase?",
        "Order ID?",
        "Amount paid?",
        "Payment method used?",
        "Did you receive the product?",
        "Upload order receipt."
    ],

    "Job Scam": [
        "Company name?",
        "Job portal or source?",
        "Did they ask for money?",
        "How much money did you pay?",
        "Communication method used?",
        "Do you have offer letters or chats?",
        "Upload supporting documents."
    ],

    "Investment Scam": [
        "Investment platform or company name?",
        "Amount invested?",
        "Expected return promised?",
        "How were you contacted?",
        "Transaction details?",
        "Do you have investment receipts?",
        "Upload screenshots."
    ],

    "Lottery/Prize Scam": [
        "What prize was promised?",
        "How were you contacted?",
        "Did they ask for any payment?",
        "Amount paid?",
        "Phone number or email of scammer?",
        "Date of incident?",
        "Upload screenshots."
    ],

    "Cyber Bullying": [
        "Which platform did the bullying occur on?",
        "Describe the abusive content.",
        "Who is responsible (if known)?",
        "How long has this been happening?",
        "Do you know the person?",
        "Has it affected your safety?",
        "Upload screenshots."
    ],

    "Sextortion": [
        "How did the offender contact you?",
        "Did they demand money or other actions?",
        "Which platform was used?",
        "Have any private images or videos been shared?",
        "Do you know the offender?",
        "Have you blocked the offender?",
        "Upload evidence."
    ],

    "Malware/Ransomware": [
        "Which device is infected?",
        "Operating System?",
        "When did the infection occur?",
        "Did you download any suspicious file?",
        "Are your files encrypted?",
        "Did you receive a ransom demand?",
        "Upload screenshots."
    ],

    "Fake Customer Care Scam": [
        "Which company was impersonated?",
        "Phone number of the scammer?",
        "Did you install any remote access app?",
        "How much money was lost?",
        "Transaction ID?",
        "Date of incident?",
        "Upload call recordings or screenshots."
    ]

}


def get_questions(crime_type):
    return QUESTION_BANK.get(
        crime_type,
        [
            "Please describe the incident in detail.",
            "When did it happen?",
            "Upload any available evidence."
        ]
    )