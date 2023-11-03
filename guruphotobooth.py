import cv2
import time
import os

# 웹캠을 열기
cap = cv2.VideoCapture(0)  #카메라 연동



# 이미지 파일 경로
output_path = "images/"

#파일 없으면 생성
if not os.path.exists(output_path):
    os.makedirs(output_path)

image_counter = 0

while True:
    # 프레임 인식
    ret, frame = cap.read()

    # 10초마다 캡처
    if image_counter % 30 == 0:  # 30프레임/초 * 10초 = 300프레임
        image_filename = f"{output_path}capture_{int(time.time())}.png"
        cv2.imwrite(image_filename, frame)
        print(f"이미지 캡처: {image_filename}")
        
        # 타이머
        timer_text = f"Time: {int(image_counter / 30)}s"
        cv2.putText(frame, timer_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    image_counter += 1

    # ui표시
    cv2.imshow('Webcam', frame)

    # q키 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()
