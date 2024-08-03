from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for texts
texts = []

# Load default data from a file
def load_default_texts(filename):
    print(f"Attempting to load default texts from {filename}...")
    try:
        with open(filename, 'r') as file:
            print(f"File {filename} opened successfully.")
            for line in file:
                texts.append(line.strip())
                print(f"Loaded line: {line.strip()}")
        print(f"Finished loading default texts from {filename}.")
    except FileNotFoundError:
        print(f"Warning: {filename} not found. No default texts loaded.")

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
    print(f"start app")
    print("Your debug message here")
    load_default_texts('default_texts.txt')
    app.run(debug=True)