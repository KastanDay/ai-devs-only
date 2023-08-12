from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print('Received data:', data)
    return 'Success', 200

if __name__ == '__main__':
    app.run(port=5000)