from flask import Flask, request, jsonify
import uuid
import validate
import calculate

app = Flask(__name__)

# Define an in-memory dictionary to store receipts
receipts = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        data = request.json
        validate.validate_receipt(data)

        # Generate a unique ID for the receipt
        receipt_id = str(uuid.uuid4())

        # Store the receipt in memory
        receipts[receipt_id] = data

        response = {"id": receipt_id}
        return jsonify(response), 200
    except Exception as e:
        return str(e), 400

@app.route('/receipts/<string:receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    try:
        if receipt_id not in receipts:
            return "No receipt found for that id", 404

        receipt = receipts[receipt_id]
        calculations = calculate.calculate_points(receipt)
        points=calculations[0]
        #points = calculate.calculate_points(receipt)
        breakdown = calculations[1]
        #breakdown = breakdown_points.create_breakdown(receipt, points)
        response = {"points": points, "breakdown": breakdown}

        # Print the response to the console
        print(breakdown)
        
        return jsonify(response), 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)