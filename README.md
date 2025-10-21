<h1 align="center">📰 EduPulse — Daily Tech Digest</h1>

<p align="center">
  <b>A Python-powered automated daily newsletter for personal use.</b><br>
  Fetches the latest tech news, summarizes them using <b>Groq AI</b>, and sends a beautiful HTML digest via <b>Brevo</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Groq_AI-Summarization-purple.svg?style=for-the-badge" alt="Groq AI">
  <img src="https://img.shields.io/badge/Brevo_API-Email-orange.svg?style=for-the-badge" alt="Brevo API">
  <img src="https://img.shields.io/badge/NewsAPI-Fetching-green.svg?style=for-the-badge" alt="NewsAPI">
</p>

---

## ✨ Features

- 🧠 Fetches **AI/ML**, **ECE/Science**, and **Indian Startup** news daily  
- 📝 Summarizes each article in **1–2 sentences** using **Groq API**  
- 💌 Sends **HTML-formatted newsletters** using **Brevo API**  
- 🔗 Includes clickable **“Read more →”** links  
- ⚙️ Fully automatable with **Windows Task Scheduler** or **cron jobs**  
- 🪶 Lightweight, modular, and customizable  

---

###📁 Project Structure

```text

EduPulse/
│
├─ fetch_news.py # Fetch news from NewsAPI
├─ summarizer.py # Summarize articles using Groq API
├─ send_email.py # Send newsletter via Brevo API
├─ daily_digest.py # Main script to generate & send digest
├─ config.py # Store your API keys
├─ requirements.txt # Python dependencies
└─ templates/
└─ email_template.html # HTML newsletter template

```
---

## ⚡ Prerequisites

Before using EduPulse, ensure you have:

- **Python 3.10+**  
- [NewsAPI](https://newsapi.org/) account + API key  
- [Groq API](https://console.groq.com/) account + API key  
- [Brevo](https://www.brevo.com/) account + API key  
- Verified **sender email** in Brevo  

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/farwez/EduPulse.git
cd EduPulse
```
2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
⚙️ Configuration
Create a file named config.py in your project root:
```bash
NEWS_API_KEY = "your_newsapi_key"
GROQ_API_KEY = "your_groq_api_key"
BREVO_API_KEY = "your_brevo_api_key"
```
✅ Tip: Verify your sender email in Brevo before running the script.

🚀 Run the Digest
Generate and send your daily digest manually:
```
python daily_digest.py
```
You’ll receive an email with curated AI, ECE, and Startup news — summarized and neatly formatted.

⏰ Automate Daily Delivery
🪟 Windows (Task Scheduler)
Program: path\to\python.exe

Arguments: path\to\daily_digest.py

Trigger: Daily at your preferred time

Example:
```
C:\Python311\python.exe C:\Users\you\EduPulse\daily_digest.py
```
🐧 Linux / macOS (cron)
Open crontab:
crontab -e

Add this line to run daily at 8:00 AM:
```
0 8 * * * /path/to/python /path/to/EduPulse/daily_digest.py
```
🧩 Notes
If Groq API summarization fails → falls back to full article text
If NewsAPI returns no results → that category is skipped

Customize newsletter design in templates/email_template.html

---

🧡 License
Personal Use Only — feel free to modify and adapt for your own workflow.

🧠 Example Output
```
“📰 Good morning! Here’s your curated digest of today’s AI, ECE, and Startup news.”
Each section includes 3–5 summarized stories with direct “Read more →” links — delivered automatically to your inbox.
```
<p align="center"> <b>Made with 🧠 Python · ⚡ Groq · 💌 Brevo · ❤️ for daily learners</b> </p>

