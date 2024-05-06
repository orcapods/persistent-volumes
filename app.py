from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from the Python Flask App!"

@app.route('/write', methods=['POST'])
def write_file():
    data = request.form['data']
    with open('/data/persistent_data.txt', 'a') as f:
        f.write(data + '\n')
    return "Data written to file."

@app.route('/read', methods=['GET'])
def read_file():
    if os.path.exists('/data/persistent_data.txt'):
        with open('/data/persistent_data.txt', 'r') as f:
            content = f.read()
        return content
    else:
        return "No data found."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)