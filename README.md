# 📰 EduPulse — Daily Tech Digest

**EduPulse** is a Python-based automated daily newsletter for personal use.  
It fetches the latest tech news, summarizes them using **Groq AI**, and sends a beautifully formatted HTML email through **Brevo (Sendinblue)**.

---

## ✨ Features

- 🧠 Fetches daily **AI/ML**, **ECE/Science**, and **Indian Startup** news  
- 📝 Summarizes each article in **1–2 sentences** using **Groq API**  
- 💌 Sends an **HTML newsletter** via **Brevo API**  
- 🔗 Includes clickable **“Read more →”** links  
- ⚙️ Fully automatable with **Windows Task Scheduler** or **cron jobs**  
- 🪶 Lightweight, modular, and easy to customize  

---

## 📁 Project Structure

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

yaml
Copy code

---

## ⚡ Prerequisites

Before running EduPulse, make sure you have:

- **Python 3.10+**
- [NewsAPI](https://newsapi.org/) account + API key  
- [Groq API](https://console.groq.com/) account + API key  
- [Brevo (Sendinblue)](https://www.brevo.com/) account + API key  
- Verified **sender email** in Brevo  

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/EduPulse.git
cd EduPulse
2. Create and Activate a Virtual Environment
Windows PowerShell

bash
Copy code
python -m venv .venv
.\.venv\Scripts\Activate.ps1
Linux / macOS

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
⚙️ Configuration
Create a file named config.py in the project root and add your keys:

python
Copy code
NEWS_API_KEY = "your_newsapi_key"
GROQ_API_KEY = "your_groq_api_key"
BREVO_API_KEY = "your_brevo_api_key"
✅ Ensure your sender email is verified in Brevo before sending emails.

🚀 Run the Digest
To generate and send your daily digest manually:

bash
Copy code
python daily_digest.py
You’ll receive an email with curated AI, ECE, and startup news — summarized and neatly formatted.

⏰ Automate Daily Delivery
🪟 Windows (Task Scheduler)
Program: path\to\python.exe

Arguments: path\to\daily_digest.py

Trigger: Daily at your preferred time

Example:

mathematica
Copy code
C:\Python311\python.exe C:\Users\you\EduPulse\daily_digest.py
🐧 Linux / macOS (cron)
Open crontab:

bash
Copy code
crontab -e
Add this line to run daily at 8:00 AM:

bash
Copy code
0 8 * * * /path/to/python /path/to/EduPulse/daily_digest.py
🧩 Notes
If Groq API summarization fails → falls back to original article text

If NewsAPI returns no results → category is skipped

Customize look and feel in templates/email_template.html

🧡 License
Personal use only — feel free to modify and adapt for your own projects.

🧠 Example Output
“📰 Good morning! Here’s your curated digest of today’s AI, ECE, and Startup news.”

Each section includes 3–5 summarized stories with direct “Read more →” links — delivered automatically to your inbox.
