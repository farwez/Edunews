📰 EduPulse Daily Tech Digest

A Python-based automated daily newsletter for personal use that fetches news from NewsAPI, summarizes it using Groq AI, and sends a beautiful HTML email via Brevo API.

Features

Fetches AI/ML, ECE/Science, and Indian Startup news daily

Summarizes articles with Groq API in 1-2 sentences

Sends HTML-formatted newsletter using Brevo (Sendinblue) API

Includes clickable “Read more →” links for each article

Fully automatable with Windows Task Scheduler or cron

📦 Project Structure
EduPulse/
│
├─ fetch_news.py         # Fetch news articles from NewsAPI
├─ summarizer.py         # Summarize articles using Groq API
├─ send_email.py         # Send email using Brevo API
├─ daily_digest.py       # Main script to generate and send digest
├─ config.py             # Store your API keys
├─ requirements.txt      # Python dependencies
└─ templates/
   └─ email_template.html  # HTML newsletter template

⚡ Prerequisites

Python 3.10+
NewsAPI account + API key
Groq API account + API key
Brevo (Sendinblue) account + API key
Verified sender email in Brevo

🛠 Installation

Clone the repo:
git clone https://github.com/yourusername/EduPulse.git
cd EduPulse

Create a virtual environment and activate it:
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
source .venv/bin/activate     # Linux/Mac


Install dependencies:
pip install -r requirements.txt

⚙️ Configuration
Create a config.py file with your API keys:
NEWS_API_KEY = "your_newsapi_key"
GROQ_API_KEY = "your_groq_api_key"
BREVO_API_KEY = "your_brevo_api_key"

Also, make sure your sender email is verified in Brevo.

🚀 Run the Digest
python daily_digest.py


You should receive a daily newsletter in your inbox with AI, ECE, and startup news summaries.

⏰ Automate Daily
Windows (Task Scheduler)
Program: path\to\python.exe
Arguments: path\to\daily_digest.py
Trigger: Daily at your preferred time
Linux / Mac (cron)
0 8 * * * /path/to/python /path/to/daily_digest.py

This runs the script every day at 8:00 AM.
📌 Notes

Groq API failures fallback to the original article text
Empty NewsAPI results are skipped
You can customize the HTML template in templates/email_template.html

🧡 License
Personal use only — feel free to customize for your own projects.
