import feedparser
import time
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GroqAPIKey")
client = Groq(api_key=GROQ_API_KEY)

def fetch_google_news(query, max_articles=10):
    # Google News RSS URL
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:max_articles]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    return articles

def generate_summary(news_articles):
    if not news_articles:
        return "No news found for this topic."

    headlines = "\n".join([f"- {article['title']}" for article in news_articles])

    prompt = f"""
    Summarise the following news headlines briefly and clearly:

    {headlines}

    Provide:
    • Key updates
    • Recent changes
    • Short actionable insights
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    # Access using attributes (not dict)
    return completion.choices[0].message.content

def run_news_agent(query, interval=300):
    old_news_titles = []

    print(f"\n🔍 Tracking news for: {query}")
    print(f"⏱️ Checking every {interval} seconds...\n")

    while True:
        news = fetch_google_news(query)
        news_titles = [article["title"] for article in news]

        if news_titles != old_news_titles:
            print("\n🆕 News Updated!\n")
            summary = generate_summary(news)
            print(summary)
            print("\n" + "="*60)
            old_news_titles = news_titles

        time.sleep(interval)

if __name__ == "__main__":
    topic = input("Enter topic/location for news: ")
    run_news_agent(topic)
