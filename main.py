import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://in.bookmyshow.com/movies/hyderabad/peddi/ET00439772"

TARGET_THEATRE = "peddi"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(URL, headers=headers)

page_text = response.text.lower()

if TARGET_THEATRE.lower() in page_text:

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": f"🔥 PEDDI BOOKINGS OPENED at {TARGET_THEATRE} 🔥"
    }

    requests.post(telegram_url, data=data)

    print("Alert Sent")

else:
    print("Bookings Not Open Yet")
