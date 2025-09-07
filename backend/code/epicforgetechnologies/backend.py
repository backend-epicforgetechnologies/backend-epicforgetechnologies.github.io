# backend.py
from flask import Flask, request, jsonify
import random
import numpy as np

app = Flask(__name__)

# -------------------------------
# Simple placeholder AI logic
# This is version 1.0
# -------------------------------

class SimpleAI:
    def __init__(self):
        # For now, we simulate dynamic responses with a small pattern generator
        self.responses_seed = [
            "I see! Can you tell me more?",
            "Interesting, let me think...",
            "Epic Forge Technologies is amazing, isn't it?",
            "I'm learning more every day!",
            "Can you clarify that for me?"
        ]
    
    def generate_response(self, user_input):
        # Here you can replace this with a real neural network later
        # For now, we return a random dynamic-seeming response
        return random.choice(self.responses_seed)

# Initialize AI
ai = SimpleAI()

# -------------------------------
# API route for frontend or external requests
# Example:
# /api/ai/?epicforgetechnologiesaiver=1.0&source=ai-epicforgetechnologies.github.io/ai/?request_from=api-epicforgetechnologies.github.io
# -------------------------------

@app.route("/api/ai/", methods=["GET", "POST"])
def ai_api():
    user_input = request.args.get("request") or request.json.get("request", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    response = ai.generate_response(user_input)
    
    return jsonify({
        "input": user_input,
        "response": response,
        "version": "1.0"
    })

# -------------------------------
# Run locally
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
