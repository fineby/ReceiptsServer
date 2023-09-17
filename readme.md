Task:
Build a webservice that fulfills the documented API file api.yml.

API Specification:
Endpoint: Process Receipts
Path: /receipts/process
Method: POST
Payload: Receipt JSON
Response: JSON containing an id for the receipt.

The ID returned is the ID that should be passed into /receipts/{id}/points to get the number of points the receipt was awarded.

Endpoint: Get Points
Path: /receipts/{id}/points
Method: GET
Response: A JSON object containing the number of points awarded.

Rules:
These rules collectively define how many points should be awarded to a receipt.
One point for every alphanumeric character in the retailer name.
50 points if the total is a round dollar amount with no cents.
25 points if the total is a multiple of 0.25.
5 points for every two items on the receipt.
If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
6 points if the day in the purchase date is odd.
10 points if the time of purchase is after 2:00pm and before 4:00pm.

SOLUTION

Structure and main file:
The program used Python and Flask for server side. POST and GET methods from the main module are ised to work with the server. Validation and calculation modules executed from the main module for appropriate operations. Separate file used to display to the console all receipts from receipts directory (‘./receipts’).

Validation file:
Validation is checking the schema builded in accordance with api.yml from the task. In case of errors the error displays to the console.

Calculation file:
The file implements business logic in accordance with the task rules, adding print strings for each valid rule for the further print to the console.

Process-all file:
The code loads all files from the directory, generates POST and GET requests for each file and displays those requests and points breakdown for them.

Process for one receipt:
To process one receipt from the Bash terminal make following commands:
POST request (name.json is  a name for the file at the directory ./receipts):
curl -X POST -H "Content-Type: application/json" -d @./name.json  http://localhost:5000/receipts/process

GET request (id is unique code for the receipts generated after POST request execution):  curl http://localhost:5000/receipts/{id}/points

Installation and execution:
The environment could be created via requirements.txt at the VSCode or via Docker with execution Dockerfile.
To run the program at the Powershell terminal execute command from the program root directory: python main.py, which starts the local server and will begin to display at those windows all console outputs.
To process all receipts from the directory run another Powershell terminal and execute command from the program root directory: python process-all.py, which starts to display all requests and breakdown to the output console.
To process separate commands (POST, GET) run a command from Powershell terminal.