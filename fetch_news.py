import requests
import os
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
def get_news(query="technology", page_size=5):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": NEWS_API_KEY,
        "q": query,          # keyword instead of category
        "language": "en",
        "pageSize": page_size,
        "sortBy": "publishedAt"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print("Error:", data)
        return []

    articles = []
    for a in data.get("articles", []):
        articles.append({
            "title": a["title"],
            "description": a["description"] or a["title"],
            "url": a["url"]
        })
    return articles


