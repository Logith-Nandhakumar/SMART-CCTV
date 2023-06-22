from itertools import count
import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font
import datetime
import time
import face_recognition
import glob


def collect_data():
    print("Here after entering Name your face id will be recorded automatically: \n After pressing esc your face data will be captured")
    print('Please make sure your face is visible when pressing esc')
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
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    detection = None
    detection_stopped_time = 0.0
    timer_started = False
    detection_stopped_time1 = 0.0
    something_detected = None
    current_time = None
    count5 = 0
    count1 = 0
    count3 = 0
    count2 = 0
    count4 = 0
    global detectTime
    detectTime = 0
    

    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        
        
        
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            if name != "Unknown":
                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)
                something_detected = True
                if detectTime:
                    
                    detectTime = 0


            elif name == "Unknown":
                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                something_detected = True
                count5 += 1

                if detection_stopped_time == 0.0 and count5 == 5:
                    
                    detection_stopped_time = time.time()
                    detectTime = detection_stopped_time

            if name == "Unknown" and (int(time.time() - detection_stopped_time) == 3):
                
                if count3 == 0:
                    count3 = 1

                if count3 == 1:
                    detection = True
                    print("Started Recording!")
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                    global out
                    out = cv2.VideoWriter(f"authorize/{current_time}.mp4", fourcc, 20, frame_size)
                    print(current_time)
                    count3 = 2

            if detection:
                out.write(frame)
            
        if something_detected and len(face_locations) == 0:
            count1 += 1
            if (int(time.time() - detectTime) >= 3) and detectTime:
                out.write(frame)
            if detection_stopped_time1 == 0.0 and count1 >= 10:
                if count2 == 0:
                    count2 = 1
                if count2 == 1:
                    detection_stopped_time1 = time.time()
                    
                    count2 = 2
                    detection = False
        
        if detection is False and (int(time.time() - detection_stopped_time1) == 5):
            print(time.time() - detection_stopped_time1)
            if count4 == 0:
                count4 = 1
            if count4 == 1:
                detection_stopped_time = 0.0
                detection_stopped_time1 = 0.0
                something_detected = None
                count5 = 0
                count1 = 0
                count3 = 0
                detectTime = 0
                out.release()
                print('Stop Recording!')
                count4 = 2
               
            
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names



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


