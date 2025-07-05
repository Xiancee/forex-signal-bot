import requests

bot_token = 'your_token_here'
chat_id = 'your_chat_id_here'

message = "✅ Telegram Bot Test: Signal system is working!"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
data = {'chat_id': chat_id, 'text': message}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("✅ Message sent!")
else:
    print("❌ Failed to send:", response.text)
