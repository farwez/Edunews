# 📰 EduPulse - Daily Tech Digest

EduPulse is an automated AI-powered newsletter that collects daily news about AI, Electronics (ECE), and Indian Startups, summarizes them using Groq API, and emails a neat HTML digest via Brevo.

---

## 🚀 Features

- Fetches latest news using **NewsAPI**
- Summarizes content using **Groq (Llama 3.1 8B Instant)**
- Sends daily email using **Brevo API**
- Automated with **GitHub Actions**
- Simple, modular Python code

---

## 📁 Project Structure

fetch_news.py → Fetches articles from NewsAPI
summarizer.py → Summarizes text using Groq API
send_email.py → Sends email via Brevo
daily_digest.py → Combines all and builds daily digest
templates/email_template.html → Email layout
.github/workflows/daily_digest.yml → Daily automation
requirements.txt → Dependencies

---

## ⚙️ Setup

1. **Clone this repo**
   ```bash
   git clone https://github.com/farwez/edupulse.git
   cd edupulse
2.Install dependencies
pip install -r requirements.txt

3.Set environment variables
Create a .env file or add GitHub Secrets:

NEWS_API_KEY=your_newsapi_key
GROQ_API_KEY=your_groq_api_key
BREVO_API_KEY=your_brevo_api_key

4.Run manually
python daily_digest.py

🕓 GitHub Actions (Automation)
This project runs automatically every day at 11:30 AM IST.


on:
  schedule:
    - cron: "0 6 * * *"   # 11:30 AM IST
  workflow_dispatch:
Secrets (NEWS_API_KEY, GROQ_API_KEY, BREVO_API_KEY) are stored in
Settings → Secrets → Actions.

💡 Tech Used
Python 3.11
Groq API
NewsAPI
Brevo
GitHub Actions


❤️❤️❤️❤️❤️
