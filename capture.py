import cv2
import numpy as np

def anime_filter(img):
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # ぼかしでノイズ低減
    edge = cv2.blur(gray, (3, 3))
    # Cannyアルゴリズムで輪郭抽出
    edge = cv2.Canny(edge, 50, 150, apertureSize=3) 
    # 輪郭画像をRGB色空間に変換
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    # 画像の領域分割
    img = cv2.pyrMeanShiftFiltering(img, 5, 20)
    # 差分を返す
    return cv2.subtract(img, edge)

def line_filter(img):
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # ぼかしでノイズ低減
    edge = cv2.blur(gray, (3, 3))
    # Cannyアルゴリズムで輪郭抽出
    edge = cv2.Canny(edge, 50, 150, apertureSize=3) 
    # 輪郭画像をRGB色空間に変換
    # edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    # 画像の領域分割
    #img = cv2.pyrMeanShiftFiltering(img, 5, 20)
    # 差分を返す
    return edge

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
        
        anime = anime_filter(frame)
        cv2.imshow('anime', anime)
        
        line = line_filter(frame)
        cv2.imshow('line', line)
        
        cv2.imshow('capture', frame)

        k = cv2.waitKey(1)
        if k == 27: #ESCで終了
            break

    # captureの解放
    cap.release()
    cv2.destroyAllWindows()

capture_camera()