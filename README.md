# AlertSense

AlertSense is a simple pose detector made with the help of Mediapipe framework, OpenCV, and Python language. 
It can detect whether the person who is driving a vehicle is conscious or not, even if the driver is wearing a helmet. 
The project does not rely on complex machine learning models for face detection, making it lightweight and suitable for running on machines with low computing power.
AlertSense is fast, customizable, and can be calibrated for different users.

## Deployment
### Git Clone
Clone the repository using the following command:

`git clone https://github.com/your-username/AlertSense.git`
 
 `cd AlertSens`

### Setting up the Python Environment
1. Create a Python virtual environment: `python3 -m venv env`
2. Activate the virtual environment:
   - For Windows: `env\Scripts\activate`
   - For Unix/macOS: `source env/bin/activate`

### Installing Dependencies
Install the required dependencies by running the following command:

`pip install -r requirements.txt`

use `pip3` if you are using Unix/macOS
### Running AlertSense
To run AlertSense, execute the following command:

`python AlertSense.py`

## Twilio Integration

AlertSense can be integrated with Twilio to send alerts or notifications. Follow the steps below to use Twilio with Python:

1. Sign up for a Twilio account at [Twilio website](https://www.twilio.com).
2. Obtain your Twilio Account SID and Auth Token from the Twilio console.

Replace 'your_account_sid', 'your_auth_token', 'your_twilio_phone_number', and 'recipient_phone_number' with 
your actual Twilio account details and phone numbers.
Please refer to the Twilio documentation for more information on sending SMS messages with Twilio.
