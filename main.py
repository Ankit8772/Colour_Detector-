# import cv2
# from PIL import Image

# from util import get_limits


# yellow = [0, 255, 255]  # yellow in BGR colorspace
# cap = cv2.VideoCapture(2)
# while True:
#     ret, frame = cap.read()

#     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     lowerLimit, upperLimit = get_limits(color=yellow)

#     mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

#     mask_ = Image.fromarray(mask)

#     bbox = mask_.getbbox()

#     if bbox is not None:
#         x1, y1, x2, y2 = bbox

#         frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()

# cv2.destroyAllWindows()







# import cv2

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open camera.")
#     exit()

# while True:
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Error: Couldn't read frame.")
#         break
    
#     cv2.imshow('Camera Feed', frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()






import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)  # Verify if index 2 is valid; try 0 if needed

if not cap.isOpened():
    print("Error: Could not open video capture device.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Failed to grab frame, skipping...")
        continue  # or break out of the loop

    try:
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    except cv2.error as e:
        print("Error in cvtColor:", e)
        continue

    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # For debugging: show the mask
    cv2.imshow('mask', mask)

    # Use PIL to find the bounding box of nonzero mask pixels
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
