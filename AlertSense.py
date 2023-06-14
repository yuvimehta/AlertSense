import cv2
from postestimationModule import PoseDetector
import mediapipe
import numpy as np
from twilio.rest import Client
from sklearn.linear_model import LinearRegression

account_sid = 'AC63b5f7aa037797d221ee3db9396a6856'
auth_token = '4fa9febc4f282d48f9b3119588aa6e2f'
from_number = '+14302337412'
to_number = '+919041862600'



# here I have used a test data without proper measurments #
# You can use data set with more and accurtae values for more precise detetcion #
# This Distance from camera is in cm, While calibrating you can use any dimensions #
distance_between_points = np.array(
    [250, 300, 333, 370, 382, 420, 470, 500, 520, 610])
distance_from_camera = np.array([69, 65, 63, 51, 53, 50, 43, 39, 36, 27])
threshold_dis = 50
#########################


def estimate_distance_from_camera(mark, distance_between_points, distance_from_camera):
    # Extract the coordinates of left and right shoulder points
    left_shoulder = np.array(mark[11][1:])  # [x, y] of left shoulder
    right_shoulder = np.array(mark[12][1:])  # [x, y] of right shoulder

    # Calculate the distance between the shoulder points
    shoulder_distance = np.linalg.norm(left_shoulder - right_shoulder)

    # Perform linear regression on the calibration data
    X = np.array(distance_between_points).reshape(-1, 1)
    y = np.array(distance_from_camera)
    regression_model = LinearRegression().fit(X, y)

    # Estimate the distance from the camera using the regression model
    estimated_distance = regression_model.predict([[shoulder_distance]])

    return estimated_distance, shoulder_distance


def send_sms_twilio(account_sid, auth_token, from_number, to_number, message):
    # Create a Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Send the SMS message
        response = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print('SMS sent successfully!')
    except Exception as e:
        print('An error occurred while sending the SMS:', e)


def main():

    # Use 0 for the default webcam, or change it to the appropriate device index
    cap = cv2.VideoCapture(0)
    pose_detector = PoseDetector()
    sms_sent = False
    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame = pose_detector.findPose(frame, status=False)
        mark = pose_detector.find_marks(frame)

        if len(mark) != 0:
            # add your code to use marks( cordinates of human pose) #

            # Here For testing I am sending a SMS message as a SOS #
            camera_distance, shoulder = estimate_distance_from_camera(
                mark, distance_between_points, distance_from_camera)
            camera_distance = int(camera_distance)
            print("Estimated distance from camera:", camera_distance)
            # print("Estimated distance between shoulders:", shoulder)

            if camera_distance < threshold_dis and not sms_sent:
                message = "Alert: Maintain distance!"
                send_sms_twilio(account_sid, auth_token,
                                from_number, to_number, message)
                print("message sent")
                sms_sent = True

        cv2.imshow('Video Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
