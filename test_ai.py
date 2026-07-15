from ai.classifier import classify_crime

text = """
My Instagram account was hacked yesterday.
"""

result = classify_crime(text)

print("Detected Crime Type:", result)