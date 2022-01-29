from flask import Flask, jsonify

# Initialize Flask
app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello_world():
  return jsonify({'Hello': 'World'})

if __name__ == '__main__':
    app.run(debug=True)
