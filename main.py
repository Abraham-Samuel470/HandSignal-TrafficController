#                                                 #Traffic Guard
# traffic Signal Controller

# immdiate action not waiting for the timer signal to go off
import cv2
import mediapipe as mp
import time
import trafficcontrol as cnt

time.sleep(2.0)


mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)  # This '0' will use my default camera

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = video.read()
        # Flip the image horizontally to handle the mirroring issue
        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert the camera background color to RGB
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert the camera background color back to BGR
        lmList = []

        # Get the frame dimensions
        h, w, c = image.shape

        # Define rectangle dimensions
        rect_start = (int(w * 0.3), int(h * 0.3))  # 30% from the top-left
        rect_end = (int(w * 0.7), int(h * 0.7))    # 70% from the top-left

        cv2.rectangle(image, rect_start, rect_end, (0, 255, 0), 2)  # Draw the rectangle

        hand_text = ""  # Initialize hand text

        if results.multi_hand_landmarks:
            for idx, hand_landmark in enumerate(results.multi_hand_landmarks):
                myHands = results.multi_hand_landmarks[idx]
                handedness = results.multi_handedness[idx].classification[0].label  # 'Left' or 'Right'

                for id, lm in enumerate(myHands.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

                # Update the hand text
                hand_text = handedness

            fingers = []
            if len(lmList) != 0:
                # Check if the hand is inside the rectangle
                hand_inside = any(
                    rect_start[0] <= point[1] <= rect_end[0] and
                    rect_start[1] <= point[2] <= rect_end[1]
                    for point in lmList
                )

                if hand_inside:
                    # Thumb detection logic adjusts based on hand orientation
                    if handedness == "Right":
                        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:  # Right hand thumb
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    else:  # Left hand
                        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:  # Left hand thumb
                            fingers.append(1)
                        else:
                            fingers.append(0)

                    # Other fingers remain the same for both hands
                    for id in range(1, 5):
                        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)

                    total = fingers.count(1)
                    cnt.led(total)# this will connect the arudino board with my python program and without this the program still will work
                    #it will just show the display as Go,Slow,Stop


                    # Dynamically calculate the box and text position below the rectangle
                    text_box_start = (rect_start[0], rect_end[1] + 10)  # Just below the rectangle
                    text_box_end = (rect_end[0], rect_end[1] + 60)      # Adjust the height of the text box
                    text_position = (rect_start[0] + 10, rect_end[1] + 45)  # Text position inside the box

                    if total == 0:  # Slow
                         cv2.rectangle(image, text_box_start, text_box_end, (0, 255, 255), cv2.FILLED)
                         cv2.putText(image, "   Slow  ", text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
                    elif total == 1:  # Go!!
                         cv2.rectangle(image, text_box_start, text_box_end, (0, 255, 0), cv2.FILLED)
                         cv2.putText(image, "   Go!! ", text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
                    elif total == 5:  # Stop
                         cv2.rectangle(image, text_box_start, text_box_end, (0, 0, 255), cv2.FILLED)
                         cv2.putText(image, "   Stop  ", text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)


        # Display the hand type above the rectangle
        if hand_text:
            cv2.putText(image, f"Sam's {hand_text} Hand", (rect_start[0], rect_start[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        cv2.imshow("Sam's Cam", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    