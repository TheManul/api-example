from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate():
    try:
        with open('example.txt', 'r') as file:
            urls = file.readlines()
        
        url = random.choice(urls).strip()
    except FileNotFoundError:
        data = {'message': 'Invalid path'}
        return jsonify(data), 404
    
    data = {'url': url}
    return jsonify(data)


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
