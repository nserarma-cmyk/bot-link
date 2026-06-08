import imaplib
import email
import requests
import time

# بيانات بريدك (استخدم App Password إذا كنت تستخدم Gmail)
EMAIL = "nabil.ser178@gmail.com"
PASSWORD = "ygvi wrxc gosl onkx" 
TELEGRAM_TOKEN = "8260112441:AAHif-SliqYUS2AYtr9eq9jKbR8e5UHAk6Y"
CHAT_ID = "2127722447"

def check_email():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    
    # البحث عن رسائل جديدة من TradingView
    status, messages = mail.search(None, 'FROM "noreply@tradingview.com" UNSEEN')
    
    for num in messages[0].split():
        # هنا يتم استخراج نص الرسالة وإرسالها لتليجرام
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": "إشارة جديدة من TradingView!"})
        
    mail.logout()

while True:
    try:
        check_email()
    except:
        pass
    time.sleep(60) # فحص البريد كل دقيقة
