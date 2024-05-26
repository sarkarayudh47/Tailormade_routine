from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all origins during development

@app.route('/')
def index():
  return "Hello from Flask!"
# Route to handle form submission
@app.route('/submit-form', methods=['POST'])
def submit_form():
  if request.method == 'OPTIONS':
    response = app.make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins for development
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'  # Allow POST and OPTIONS
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'  # Allow Content-Type header
    return response

  try:
    # Get form data from request body (assuming JSON format)
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    print(name, email, message)
    if not name or not email or not message:
      return jsonify({"error": "All fields are required"}), 400

    # Process the data (replace with your actual logic)
    # For example, persisting data to a database:
    # ... your implementation here ...

    return jsonify({"message": "Form data received successfully"}), 200

  except Exception as e:
    print(f"Error processing form submission: {e}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
  app.run(debug=True, port=8080)
  