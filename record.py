import cv2
import datetime


def record():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter(f'recordings/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc,20.0,(640,480))
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    recording = 1
    while True:
        _, frame = cap.read()
        if recording == 1:
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"recordings/{current_time}.mp4", fourcc, 20, frame_size)
            recording =2
        out.write(frame)
        cv2.imshow("esc. to stop", frame)

        if cv2.waitKey(1) == 27:
            out.release()
            cap.release()
            cv2.destroyAllWindows()
            break
