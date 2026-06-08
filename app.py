from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    msg = data.get('text', 'Signal!')
    requests.post("https://api.telegram.org/bot8260112441:AAHif-SliqYUS2AYtr9eq9jKbR8e5UHAk6Y/sendMessage", 
                  json={"chat_id": "2127722447", "text": msg})
    return "OK", 200
if __name__ == '__main__':
    app.run()
