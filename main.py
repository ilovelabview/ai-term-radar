import requests
import re
from datetime import date
from collections import Counter

def fetch_trending_repos():
    # Simulate fetching from GitHub trending (simplified)
    # In real life, use GitHub API or scrape; here we mock data
    return [
        "AIHOT", "aurelio-finance", "solid-glass", "folkbench", "new-term-radar"
    ]

def extract_ai_terms(repo_names):
    # Extract potential AI-related terms (e.g., ai, agent, llm, model, etc.)
    ai_keywords = ['ai', 'agent', 'llm', 'model', 'neural', 'gpt', 'transformer', 'learning', 'deep']
    term_counter = Counter()
    for name in repo_names:
        words = re.findall(r'[a-z]+', name.lower())
        for w in words:
            if w in ai_keywords:
                term_counter[w] += 1
    return term_counter

def main():
    repos = fetch_trending_repos()
    terms = extract_ai_terms(repos)
    today = date.today().isoformat()
    print(f"AI Term Radar for {today}")
    if terms:
        print("Most mentioned AI terms in top repos:")
        for term, count in terms.most_common(5):
            print(f" - {term}: {count}")
    else:
        print("No AI terms detected.")

if __name__ == "__main__":
    main()
