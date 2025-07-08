import re
from urllib.parse import urlparse

def is_ip_address(domain):
    return bool(re.fullmatch(r'\d+\.\d+\.\d+\.\d+', domain))

def detect_phishing(url):
    suspicious_words = ['login', 'verify', 'secure', 'account', 'update', 'bank', 'confirm']
    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path

    # Rules
    if '@' in url:
        return True, " URL contains '@' — phishing suspected."
    if '//' in url[8:]:  # ignore http:// or https://
        return True, " URL contains '//' beyond protocol — suspicious."
    if '-' in domain:
        return True, " Hyphen in domain name — common in phishing."
    if is_ip_address(domain):
        return True, " Domain is an IP address — suspicious."
    if url.count('.') > 4:
        return True, " Too many dots — suspicious subdomains."
    if any(word in url.lower() for word in suspicious_words):
        return True, " Contains suspicious keyword — phishing suspected."

    return False, " URL seems safe."

# Example usage
'''if __name__ == "__main__":
    test_urls = [
        "http://192.168.1.1/login",
        "https://secure-login.example.com/account/verify",
        "https://www.google.com",
        "http://example.com//extra/path",
        "http://safe-site.com",
        "https://bank-login.verification.info"
    ]
    for url in test_urls:
        is_phishing, reason = detect_phishing(url)
        print(f"{url}\nResult: {reason}\n")'''
#user input 
if __name__ == "__main__":
    print(" Phishing Website Detector (Rule-Based)")
    user_url = input("Enter a URL to check: ")

    is_phish, reason = detect_phishing(user_url)
    print("\nResult:", reason)

