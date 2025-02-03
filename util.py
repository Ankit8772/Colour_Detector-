import numpy as np
import cv2

def get_limits(color):
    """
    Convert a BGR color to its HSV limits for color detection.

    :param color: List of BGR values (e.g., [0, 255, 255] for yellow).
    :return: Tuple (lowerLimit, upperLimit) in HSV space.
    """
    c = np.uint8([[color]])  # Convert to NumPy array
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # Convert to HSV
    hue = hsvC[0][0][0]  # Extract Hue

    # Define the saturation and value range
    sat_min, val_min = 100, 100  # Avoid very dark/white colors
    sat_max, val_max = 255, 255

    if hue >= 170 or hue <= 10:  # Red hue wraps around at 180
        lowerLimit1 = np.array([0, sat_min, val_min], dtype=np.uint8)
        upperLimit1 = np.array([hue + 10, sat_max, val_max], dtype=np.uint8)

        lowerLimit2 = np.array([hue - 10, sat_min, val_min], dtype=np.uint8)
        upperLimit2 = np.array([180, sat_max, val_max], dtype=np.uint8)

        return (lowerLimit1, upperLimit1), (lowerLimit2, upperLimit2)
    else:
        lowerLimit = np.array([hue - 10, sat_min, val_min], dtype=np.uint8)
        upperLimit = np.array([hue + 10, sat_max, val_max], dtype=np.uint8)

        return (lowerLimit, upperLimit)
