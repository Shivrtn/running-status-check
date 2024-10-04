from flask import Flask, jsonify
import time

from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Record the time when the server starts
start_time = time.time()

# Route to return the current value of 'c' based on time passed
@app.route('/get_counter', methods=['GET'])
def get_counter():
    current_time = time.time()
    # Calculate the number of increments (every 15 seconds)
    c = int((current_time - start_time) // 15)
    return jsonify({"counter": c})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
