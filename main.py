import requests
from bs4 import BeautifulSoup
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://in.bookmyshow.com/explore/movies-hyderabad"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all("h3")

movie_names = []

for movie in movies:
    name = movie.get_text(strip=True)

    if name and name not in movie_names:
        movie_names.append(name)

message = "🎬 BookMyShow Movie Alerts\n\n"

for movie in movie_names[:15]:
    message += f"• {movie}\n"

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": message
}

requests.post(telegram_url, data=data)

print("Alert Sent Successfully")
