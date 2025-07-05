import random
import time
import requests

bot_token = 'your_token_here'
chat_id = 'your_chat_id_here'

def send_telegram(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)

def generate_fake_signal():
    pairs = ['EURUSD', 'GBPUSD', 'XAUUSD', 'XAGUSD']
    directions = ['BUY', 'SELL']
    pair = random.choice(pairs)
    direction = random.choice(directions)
    price = round(random.uniform(1.0, 2000.0), 4)
    signal = f"{direction} signal for {pair} at {price}"
    return signal

while True:
    signal = generate_fake_signal()
    print("Sending signal:", signal)
    send_telegram(f"📡 Simulated Signal:
{signal}")
    time.sleep(60)  # Sends a new signal every minute
