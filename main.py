from flask import Flask, request, jsonify

app = Flask(__name__)

# This would store the location data; in a real app, you'd use a database
locations = {}

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    device_id = data.get('device_id')
    location = data.get('location')  # Expecting a dict with 'latitude' and 'longitude'
    
    if device_id and location:
        # Store or update the device's location
        locations[device_id] = location
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'error': 'Invalid data'}), 400

@app.route('/get_location/<device_id>', methods=['GET'])
def get_location(device_id):
    location = locations.get(device_id)
    if location:
        return jsonify(location), 200
    else:
        return jsonify({'error': 'Device not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
