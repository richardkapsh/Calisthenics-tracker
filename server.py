from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder ="frontend")

# In-memory DB
progress_data = {}

@app.route("/")
def home():
    return send_from_directory("frontend", "frontend.html")

@app.route("/progress", methods=["GET", "POST"])
def handle_progress():
    user_id = request.args.get("userId")

    if not user_id:
        return jsonify({"error": "userId required"}), 400

    if request.method == "POST":
        data = request.json
        
        if user_id not in progress_data:
            progress_data[user_id] = []
        
        progress_data[user_id].append(data)
        return jsonify({"status": "added"}), 200

    # GET
    return jsonify(progress_data.get(user_id, []))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
