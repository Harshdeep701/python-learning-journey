import requests # pip install requests

query = input("What type of news are you interested in today? ")
api = "pub_01cd3f1f1cb04fe996383a0d1f279808"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-08&sortBy=publishedAt&apiKey={api}"

print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
