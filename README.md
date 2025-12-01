# News_Summariser_v1
An AI-powered News Summariser that fetches real-time headlines from Google News and generates concise summaries using Llama/Groq models. Automatically tracks updates, detects changes, and provides clear insights. Lightweight, fast, and perfect for automation, agents, and personal assistants.


🚀 Features

Fetches live news from Google News (RSS)

Summarises using AI (Groq Llama)

Tracks topic/location of your choice

Auto-detects updated headlines

Lightweight and fast

Perfect for agentic AI systems



📦 Installation
pip install feedparser groq python-dotenv requests




Add your Groq API key to .env:

GROQ_API_KEY=your_key_here



▶️ Usage
python ai_news_summariser_google.py


Enter your topic:

Enter topic/location for news: Hyderabad



⚙️ Configuration

Polling interval: edit interval in run_news_agent()

Number of articles: adjust max_articles in fetch_google_news()

Summary style: modify the AI prompt



📄 License

MIT License
