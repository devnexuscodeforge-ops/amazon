import requests
from bs4 import BeautifulSoup
import smtplib

# =================================
PRODUCT_URL = "https://www.amazon.com/dp/B0G3P53W6T"
TARGET_PRICE = 18000

MY_EMAIL =  "YOUR EMAIL"        
MY_APP_PASSWORD ="YOUR APP PASSWORD"     

PRODUCT_NAME = "2pcs 20kg Fitness Dumbbells"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

price_tag = soup.select_one("span.a-offscreen")

if price_tag:
    price_text = price_tag.get_text().strip()
    price_clean = price_text.replace("$", "").replace(",", "")
    current_price = float(price_clean)

    print(f"Current Price: ${current_price:.2f}")

    if current_price > TARGET_PRICE:
        print("Price dropped! Sending email alert...")

        subject = "Amazon Price Alert!"
        body = f"""Amazon Price Alert!
The price of your product has dropped below your target!

Product: {PRODUCT_NAME}
Current Price: ${current_price:.2f}
Target Price: ${TARGET_PRICE}

Buy Now: {PRODUCT_URL}
"""
        msg = f"Subject: {subject}\n\n{body}"

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_APP_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, msg)
        connection.close()
        print("✅ Email sent successfully!")
    else:
        print(f"Price is still high (${current_price:.2f}). Waiting for drop...")
else:
    print("Could not find the price on the page.")
print(f"Status Code: {response.status_code}")
#==================================