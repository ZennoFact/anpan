import cv2
def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    cap = cv2.VideoCapture(1)

    while True:
        # retは画像取得成功フラグ
        ret, frame = cap.read()

        if mirror is True:
            frame = frame[:,::-1]

        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)
        
        cv2.imshow('capture', frame)

        k = cv2.waitKey(1)
        if k == 27: #ESCで終了
            break

    # captureの解放
    cap.release()
    cv2.destroyAllWindows()

capture_camera()