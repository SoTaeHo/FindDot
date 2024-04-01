import numpy as np
import cv2 as cv

# The given video and calibration data
# video_file = './chessboard.avi'
video_file = './mycheckerboard.mp4'

# K = np.array([[432.7390364738057, 0, 476.0614994349778],
#               [0, 431.2395555913084, 288.7602152621297],
#               [0, 0, 1]]) # Derived from `calibrate_camera.py`
# dist_coeff = np.array([-0.2852754904152874, 0.1016466459919075, -0.0004420196146339175, 0.0001149909868437517, -0.01803978785585194])

K = np.array([[1.10720575e+03, 0.00000000e+00, 3.73698488e+02],
 [0.00000000e+00, 1.10754107e+03, 6.28213566e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]) # Derived from `calibrate_camera.py` using mycheckerboard.mp4

dist_coeff = np.array([0.19376008, -0.40065903, -0.00453955,  0.00636741, -2.032309])

# Open a video
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given input, ' + video_file

# Run distortion correction
show_rectify = True
map1, map2 = None, None
while True:
    # Read an image from the video
    valid, img = video.read()
    if not valid:
        break

    # Rectify geometric distortion (Alternative: `cv.undistort()`)
    info = "Original"
    if show_rectify:
        if map1 is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
        img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
        info = "Rectified"
    cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # Show the image and process the key event
    cv.imshow("Geometric Distortion Correction", img)
    key = cv.waitKey(10)
    if key == ord(' '):     # Space: Pause
        key = cv.waitKey()
    if key == 27:           # ESC: Exit
        break
    elif key == ord('\t'):  # Tab: Toggle the mode
        show_rectify = not show_rectify

video.release()
cv.destroyAllWindows()