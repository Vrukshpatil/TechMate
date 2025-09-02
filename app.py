# from flask import Flask, render_template, request, jsonify
# import google.generativeai as genai
# import os

# app = Flask(__name__)

# # Configure your API key
# genai.configure(api_key="AIzaSyBLsgQFIkjEZCRFuv_8wozeKxA0azh3_O0")
# model = genai.GenerativeModel("gemini-1.5-flash")

# @app.route("/")
# def index():
#     return render_template("chat.html")

# @app.route("/get", methods=["POST"])
# def get_bot_response():
#     user_input = request.json["message"]
#     response = model.generate_content(user_input)
#     return jsonify({"reply": response.text})

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import google.generativeai as genai
# import os

# app = Flask(__name__)

# # Configure Gemini with API key (set it as ENV variable in Render/Heroku)
# genai.configure(api_key="AIzaSyBLsgQFIkjEZCRFuv_8wozeKxA0azh3_O0")
# model = genai.GenerativeModel("gemini-1.5-flash")

# @app.route("/")
# def home():
#     return render_template("chat.html")

# @app.route("/get", methods=["POST"])
# def get_bot_response():
#     user_msg = request.json.get("message")
#     response = model.generate_content(user_msg)
#     return jsonify({"reply": response.text})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)



from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("🚨 Missing GEMINI_API_KEY! Please set it in Render environment variables.")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json.get("message")
    response = model.generate_content(user_msg)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

