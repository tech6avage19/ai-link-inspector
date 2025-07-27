import re
from db import init_db, log_scan
from colorama import init, Fore, Style

init(autoreset=True)  # Resets color after each print


# Basic list of suspicious patterns
SUSPICIOUS_PATTERNS = [
    r"bit\.ly",              # Shortened links
    r"tinyurl\.com",
    r"\.ru$",                # Suspicious country domain
    r"free-\w+",             # "free" with other words
    r"\d{3,}\.\d{3,}\.\d{3,}\.\d{3,}",  # Raw IPs
]

def is_suspicious(url):
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, url, re.IGNORECASE):
            return True, pattern
    return False, None

def ai_score_url(url):
    """Simulated AI scoring based on suspicious keywords."""
    keywords = ['free', 'login', 'verify', 'click', 'account', 'password']
    hits = sum(1 for k in keywords if k in url.lower())
    score = hits / len(keywords)  # Returns float between 0 and 1
    return round(score, 2)

def main():
    init_db()
    print(Fore.YELLOW + "🔗 AI Link Inspector (CLI v0.1)")

    while True:
        url = input(Fore.BLUE + "\nEnter a URL (or type 'exit' to quit): ").strip()
        if url.lower() == "exit":
            break

        suspicious, pattern = is_suspicious(url)
        score = ai_score_url(url)

        log_scan(url, suspicious, pattern)

        if suspicious:
            print(Fore.RED + f"⚠️  Suspicious link detected! Pattern matched: `{pattern}`")
        else:
            print(Fore.GREEN + "✅ Link looks clean (basic checks only).")

        print(Fore.CYAN + f"🤖 AI risk score: {score}")

if __name__ == "__main__":
    main()
