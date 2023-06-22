import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font
import datetime
from simple_facerec import SimpleFacerec

face_detection1 = False

def collect_data():
	
    print("Here after entering Name your face id will be recorded automatically: ")
    name = input("Enter name of person : ")

    count = 1

    cap = cv2.VideoCapture(0)

    while True:
        _, frm = cap.read()

        cv2.imwrite(f"images/{name}.jpg", frm)
        count = count + 1

        cv2.imshow("identify", frm)

        if count > 2:
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                cap.release()
                # train()
                break


def identify():
    # Encode faces from a folder
	sfr = SimpleFacerec()
	sfr.load_encoding_images("images/")

	# Load Camera
	cap = cv2.VideoCapture(0)


	while True:
		ret, frame = cap.read()

		# Detect Faces
		face_locations, face_names = sfr.detect_known_faces(frame)
		for face_loc, name in zip(face_locations, face_names):
			y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
			if name != "unknown":
				cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
				cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)
                face_detection1 = False
                	
			else:
				cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
				cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

		cv2.imshow("Frame", frame)

		key = cv2.waitKey(1)
		if key == 27:
			break

	cap.release()
	cv2.destroyAllWindows()


def maincall():
    root = tk.Tk()

    root.geometry("480x100")
    root.title("identify")

    label = tk.Label(root, text="Select below buttons ")
    label.grid(row=0, columnspan=2)
    label_font = font.Font(size=35, weight='bold', family='Helvetica')
    label['font'] = label_font

    btn_font = font.Font(size=25)

    button1 = tk.Button(root, text="Add Member ", command=collect_data, height=2, width=20)
    button1.grid(row=1, column=0, pady=(10, 10), padx=(5, 5))
    button1['font'] = btn_font

    button2 = tk.Button(root, text="Start with known ", command=identify, height=2, width=20)
    button2.grid(row=1, column=1, pady=(10, 10), padx=(5, 5))
    button2['font'] = btn_font
    root.mainloop()

    return


