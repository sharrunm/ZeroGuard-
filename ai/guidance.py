GUIDANCE = {

    "Phishing": [
        "Do not click the phishing link again.",
        "Change all affected passwords.",
        "Enable Two-Factor Authentication.",
        "Report the phishing website.",
        "Call Cyber Crime Helpline (1930)."
    ],

    "UPI Fraud": [
        "Immediately contact your bank.",
        "Call 1930.",
        "Freeze your bank account if necessary.",
        "Save transaction details.",
        "File an official complaint."
    ],

    "Banking Fraud": [
        "Inform your bank immediately.",
        "Block your debit/credit card.",
        "Save bank statements.",
        "Change Internet banking password.",
        "Call 1930."
    ],

    "Credit/Debit Card Fraud": [
        "Block your card immediately.",
        "Inform your bank.",
        "Save transaction alerts.",
        "Change banking password.",
        "Report fraudulent transactions."
    ],

    "Identity Theft": [
        "Report identity misuse.",
        "Change passwords.",
        "Monitor bank accounts.",
        "Freeze affected accounts if required.",
        "Keep copies of all evidence."
    ],

    "Social Media Hacking": [
        "Change your password immediately.",
        "Enable Two-Factor Authentication.",
        "Recover your account.",
        "Logout from all devices.",
        "Report the account compromise."
    ],

    "Email Hacking": [
        "Change email password.",
        "Enable Two-Factor Authentication.",
        "Check recovery options.",
        "Review recent logins.",
        "Remove unknown devices."
    ],

    "Online Shopping Fraud": [
        "Contact the shopping platform.",
        "Inform your bank.",
        "Keep invoices safely.",
        "Report the seller.",
        "Call 1930."
    ],

    "Job Scam": [
        "Stop further payments.",
        "Report fake recruiters.",
        "Save chats and emails.",
        "Inform your bank.",
        "Call 1930."
    ],

    "Investment Scam": [
        "Stop investing immediately.",
        "Inform your bank.",
        "Keep transaction records.",
        "Report the investment platform.",
        "Call 1930."
    ],

    "Lottery/Prize Scam": [
        "Ignore further messages.",
        "Do not pay additional fees.",
        "Block the sender.",
        "Save all evidence.",
        "Report the scam."
    ],

    "Cyber Bullying": [
        "Block the offender.",
        "Report abusive content.",
        "Save screenshots.",
        "Inform trusted adults if necessary.",
        "Contact police if threats exist."
    ],

    "Sextortion": [
        "Do not pay the blackmailer.",
        "Save all conversations.",
        "Block the offender.",
        "Report immediately.",
        "Call 1930."
    ],

    "Malware/Ransomware": [
        "Disconnect the device from the Internet.",
        "Do not pay ransom.",
        "Run antivirus software.",
        "Backup important files.",
        "Seek technical assistance."
    ],

    "Fake Customer Care Scam": [
        "Disconnect remote access immediately.",
        "Uninstall remote access software.",
        "Inform your bank.",
        "Change passwords.",
        "Call 1930."
    ]

}

def get_guidance(crime_type):
    return GUIDANCE.get(crime_type, ["No guidance available."])