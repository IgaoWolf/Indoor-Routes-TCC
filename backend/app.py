from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Indoor Routes application!"

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    user_location = data.get('location')
    # Aqui você pode adicionar a lógica para lidar com a localização recebida
    print(f"Received location: {user_location}")
    return jsonify({"message": "Location received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

