from fetch_news import get_news
from summarizer import summarize_text
from send_email import send_email

def generate_list_items(articles):
    html = ""
    for a in articles:
        summary = summarize_text(a['description'])
        html += f"<li><b>{a['title']}</b> – {summary} <a href='{a['url']}'>Read more →</a></li>"
    return html

def build_digest():
    # fetch news
    ai_articles = get_news("ai")
    ece_articles = get_news("electronics and communication")
    startup_articles = get_news("startup")

    # read template
    with open("templates/email_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    # fill placeholders
    html_content = template.replace("{{ai_news}}", generate_list_items(ai_articles))
    html_content = html_content.replace("{{ece_news}}", generate_list_items(ece_articles))
    html_content = html_content.replace("{{startup_news}}", generate_list_items(startup_articles))

    return html_content

if __name__ == "__main__":
    html = build_digest()
    send_email("📰 EduPulse News ", html, "23r11a04b6@gcet.edu.in")
