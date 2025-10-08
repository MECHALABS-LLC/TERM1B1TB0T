import websocket
import json
import datetime

BTC_TO_USD = 29000  # Static rate
THRESHOLD = 1000

def on_message(ws, message):
    data = json.loads(message)

    if 'x' in data:
        tx = data['x']
        tx_hash = tx.get('hash')
        total_satoshis = sum(out['value'] for out in tx['out'])
        btc_value = total_satoshis / 1e8
        usd_value = btc_value * BTC_TO_USD

        if usd_value > THRESHOLD:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] Transaction: {tx_hash} | BTC: {btc_value:.4f} | USD: ${usd_value:,.2f}")
            with open("high_value_btc_tx.log", "a") as log_file:
                log_file.write(f"[{timestamp}] {tx_hash} - BTC: {btc_value:.4f}, USD: ${usd_value:,.2f}\n")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("Connected to Blockchain WebSocket. Tracking high-value BTC transactions...\n")
    ws.send(json.dumps({"op": "unconfirmed_sub"}))

if __name__ == "__main__":
    socket = "wss://ws.blockchain.info/inv"
    ws = websocket.WebSocketApp(socket,
                                 on_open=on_open,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close)
    ws.run_forever()
