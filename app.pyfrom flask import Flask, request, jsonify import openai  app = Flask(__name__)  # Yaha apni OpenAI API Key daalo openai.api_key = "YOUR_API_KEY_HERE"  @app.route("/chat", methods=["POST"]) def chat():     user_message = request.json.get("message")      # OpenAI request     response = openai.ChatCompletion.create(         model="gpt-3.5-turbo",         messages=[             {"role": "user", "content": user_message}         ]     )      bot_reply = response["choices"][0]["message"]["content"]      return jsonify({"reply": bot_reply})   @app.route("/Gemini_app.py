from flask import Flask, request, jsonify
# Gemini AI के लिए library
from google import genai
import os 

app = Flask(__name__)

# --- 1. API Key Setup ---
# Gemini Client को initialize करें
try:
    # Key को environment variable (GEMINI_API_KEY) से पढ़ना सुरक्षित अभ्यास है
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Warning: GEMINI_API_KEY environment variable not set.")
        # अगर आप अभी टेस्टिंग के लिए सीधे Key डालना चाहते हैं, तो 'YOUR_GEMINI_API_KEY_HERE' बदलें
        gemini_api_key = "YOUR_GEMINI_API_KEY_HERE"
        
    client = genai.Client(api_key=gemini_api_key)
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    client = None

@app.route("/chat", methods=["POST"])
def chat():
    if not client:
        return jsonify({"reply": "Error: Gemini client not initialized."}), 500

    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"reply": "Error: 'message' field is required."}), 400

        # --- 2. Call Gemini API ---
        # generate_content method का उपयोग करें
        response = client.models.generate_content(
            model='gemini-2.5-flash',  # या 'gemini-2.5-pro'
            contents=user_message,
        )

        bot_reply = response.text
        return jsonify({"reply": bot_reply})
        
    except Exception as e:
        print(f"An error occurred during API call: {e}")
        return jsonify({"reply": f"An internal error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
