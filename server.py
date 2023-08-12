from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    from webhook_processor import process_data

# Process the data
process_data(data)
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)