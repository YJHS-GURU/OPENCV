# pip install opencv-python
import cv2

# 웹캠을 열기
cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미합니다. 다른 카메라를 사용하려면 1, 2 등을 사용할 수 있습니다.

# 웹캠이 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 프레임을 화면에 표시
    cv2.imshow('Webcam', frame)

    # 'q' 키를 누르면 루프를 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 작업이 끝나면 리소스를 해제하고 창을 닫습니다.
cap.release()
cv2.destroyAllWindows()
