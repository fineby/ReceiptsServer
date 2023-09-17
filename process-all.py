import requests
import json
import os

#Generate input-output for all JSON receipts at the directory 
 
# Load all files from directory '/receipts' to list
def load_all():
    all_reciepts=[]
    path = './receipts'
    fileList = os.listdir(path)
    for file in fileList:
        with open(f"./receipts/{file}") as json_file:   
            all_reciepts.append(json.load(json_file))          
    return all_reciepts


# Load and input all JSON files from directory /receipts
for input_json in load_all():

# Send POST request to submit the receipt
    response = requests.post('http://localhost:5000/receipts/process', json=input_json)

    # Check if the POST request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Extract the receipt ID from the response JSON
        receipt_id = response.json().get('id')

        # Check if a receipt ID was obtained
        if receipt_id:
            # Use the receipt ID to construct the URL for the GET request
            get_url = f'http://localhost:5000/receipts/{receipt_id}/points'

            # Send GET request to retrieve points
            get_response = requests.get(get_url)

            # Print the JSON response
            print(get_response.status_code)
            print(get_response.json())
        else:
            print("No receipt ID found in the POST response.")
    else:
        print("POST request failed with status code:", response.status_code)

