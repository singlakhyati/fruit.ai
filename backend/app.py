from flask import Flask, request, jsonify
from flask_cors import CORS
from models import faqs

app = Flask(__name__)
CORS(app)

@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

@app.route('/faqs', methods=['POST'])
def create_faq():
    new_faq = request.json
    faqs.append(new_faq)
    return jsonify(new_faq), 201

@app.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    faq = next((f for f in faqs if f['id'] == faq_id), None)
    if faq:
        faq.update(request.json)
        return jsonify(faq)
    return jsonify({'error': 'FAQ not found'}), 404

@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    global faqs
    faqs = [f for f in faqs if f['id'] != faq_id]
    return jsonify({'result': 'FAQ deleted'})

if __name__ == '__main__':
    app.run(debug=True)
