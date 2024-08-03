from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# In-memory storage for texts
texts = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_text():
    text = request.json.get('text')
    if text:
        texts.append(text)
        return jsonify({'message': 'Text submitted successfully'}), 200
    return jsonify({'message': 'No text provided'}), 400

@app.route('/search', methods=['GET'])
def search_text():
    query = request.args.get('query')
    if query:
        results = [text for text in texts if query in text]
        return jsonify(results), 200
    return jsonify({'message': 'No query provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)