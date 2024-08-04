from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_text():
    text = request.json.get('text')
    if text:
        new_text = Text(content=text)
        db.session.add(new_text)
        db.session.commit()
        return jsonify({'message': 'Text submitted successfully'}), 200
    return jsonify({'message': 'No text provided'}), 400

@app.route('/search', methods=['GET'])
def search_text():
    query = request.args.get('query')
    if query:
        results = Text.query.filter(Text.content.contains(query)).all()
        return jsonify([text.content for text in results]), 200
    return jsonify({'message': 'No query provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)