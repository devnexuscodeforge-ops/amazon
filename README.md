# 🛒 Amazon Price Tracker

A Python script that monitors an Amazon product's price and automatically sends you an **email** or **SMS alert** when the price drops below your target.

---

## ✨ Features

- 🔍 Scrapes real-time product price from Amazon
- 📧 Sends email alerts via Gmail SMTP when price drops
- 📱 Sends SMS notifications via Twilio
- ⚙️ Fully configurable target price and product URL

---

## 📋 Requirements

- Python 3.x
- Gmail account with App Password enabled
- Twilio account (for SMS alerts)

---

## 📦 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/amazon-price-tracker.git
cd amazon-price-tracker
```

**2. Install dependencies:**
```bash
pip install requests beautifulsoup4 lxml twilio
```

---

## ⚙️ Configuration

Open `main.py` and update the following variables:

```python
# ── Product Settings ──────────────────────────────
PRODUCT_URL  = "https://www.amazon.com/dp/XXXXXXXXXX"  # Amazon product URL
TARGET_PRICE = 18000                                    # Your target price
PRODUCT_NAME = "Your Product Name"

# ── Email Settings (Gmail) ────────────────────────
MY_EMAIL        = "your_email@gmail.com"
MY_APP_PASSWORD = "your_gmail_app_password"

# ── SMS Settings (Twilio) ─────────────────────────
account_sid = "YOUR_ACCOUNT_SID"
auth_token  = "YOUR_AUTH_TOKEN"
from_number = "YOUR_TWILIO_NUMBER"
to_number   = "RECEIVER_NUMBER"
```

---

## 🔑 How to Get Gmail App Password

> Regular Gmail passwords won't work — you need an App Password.

1. Go to your Google Account → **Security**
2. Enable **2-Step Verification**
3. Go to **App Passwords** → select "Mail" and "Windows Computer"
4. Copy the generated 16-character password
5. Paste it into `MY_APP_PASSWORD`

---

## 📱 How to Get Twilio Credentials

1. Sign up at [twilio.com](https://www.twilio.com)
2. Get a free phone number
3. Copy your **Account SID** and **Auth Token** from the dashboard
4. Paste them into the script

---

## 🚀 Usage

```bash
python main.py
```

**Example output:**
```
Current Price: $159.99
Price dropped! Sending email alert...
✅ Email sent successfully!
Status Code: 200
```

---

## 📬 Alert Format

When the price drops, you'll receive an email like this:

```
Subject: Amazon Price Alert!

The price of your product has dropped below your target!

Product: 2pcs 20kg Fitness Dumbbells
Current Price: $159.99
Target Price: $180.00

Buy Now: https://www.amazon.com/dp/B0G3P53W6T
```

---

## 🗂️ Project Structure

```
amazon-price-tracker/
│
├── main.py          # Main script
├── README.md        # Documentation
└── requirements.txt # Dependencies
```

---

## 📄 requirements.txt

```
requests
beautifulsoup4
lxml
twilio
```

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. Scraping Amazon may violate their [Terms of Service](https://www.amazon.com/gp/help/customer/display.html?nodeId=508088). Use responsibly.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
