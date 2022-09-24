#============================================================================================================================

# imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import imutils
import argparse


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Real Time Human Detection") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "REAL  TIME  HUMAN\nDETECTION", font=("Arial", 50,"underline"), fg="magenta") # same way bg
start1.place(x = 160, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =130 , y =570 )

# image on the main window
path1 = "Images/front2.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img2 = ImageTk.PhotoImage(Image.open(path1))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel1 = tk.Label(window, image = img2)
panel1.place(x = 90, y = 250)

# image on the main window
path = "Images/front1.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 380, y = 180)

# # image on the main window
# path2 = "Images/front2.png"
# # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
# img3 = ImageTk.PhotoImage(Image.open(path2))
# # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
# panel2 = tk.Label(window, image = img3)
# panel2.place(x = 700, y = 190)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 570 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Real Time Human Detection") # title given is "DICTIONARY"
window1.geometry('1000x700')

# -------------------------------- for detecting images ------------------------------------------
def open_img():
    global filename1
    filename1 = filedialog.askopenfilename(title="Select Image file")
    # print(filename)
    path_text1.delete("1.0", "end")
    path_text1.insert(END, filename1)

def det_img():
    global filename1

    image_path = filename1
    print('[INFO] Opening Image from path.')
    detectByPathImage(image_path)

def detect_img(frame):
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('Detected Image', frame)

    # return frame

def detectByPathImage(path):
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(800, image.shape[1]))
    detect_img(image)
    # cv2.imshow("Detected Image",result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# -------------------------------------------- for detecting videos -------------------------------------------
def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
    arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
    arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
    arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(arg_parse.parse_args())

    return args

def open_vid():
    global filename2
    filename2 = filedialog.askopenfilename(title="Select VIdeo file")
    # print(filename)
    path_text2.delete("1.0", "end")
    path_text2.insert(END, filename2)

def det_vid():
    global filename2

    video_path = filename2
    args = argsParser()
    writer = None
    if args['output'] is not None:
        writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))

    print('[INFO] Opening Video from path.')
    detectByPathVideo(video_path, writer)

def detect_vid(frame):
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('Detected Video', frame)

    return frame

def detectByPathVideo(path, writer):
    video = cv2.VideoCapture(path)
    check, frame = video.read()
    if check == False:
        print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
        return

    print('Detecting people...')
    while video.isOpened():
        # check is True if reading was successful
        check, frame = video.read()

        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            frame = detect_vid(frame)

            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()

# for detecting through camera -----------------------------------------------
def open_cam():
    args = argsParser()
    writer = None
    if args['output'] is not None:
        writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))
    if True:
        print('[INFO] Opening Web Cam.')
        detectByCamera(writer)

def detect_cam(frame):
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)

    return frame

def detectByCamera(writer):
    video = cv2.VideoCapture(0)
    print('Detecting people...')

    while True:
        check, frame = video.read()

        frame = detect_cam(frame)
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()



# # top label
# start1 = tk.Label(text = "VIDEO  TO  IMAGES", font=("Arial", 55, "underline"), fg="magenta") # same way bg
# start1.place(x = 140, y = 10)

# for images ----------------------
lbl1 = tk.Label(text="Detect from Image...", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=80, y=20)
lbl2 = tk.Label(text="Selected Image", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=80)
path_text1 = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text1.place(x=80, y = 140)

# for videos ---------------------------
lbl1 = tk.Label(text="Detect from Video...", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=80, y=250)
lbl2 = tk.Label(text="Selected Video", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=310)
path_text2 = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text2.place(x=80, y = 370)

# for camera ---------------------------
lbl1 = tk.Label(text="Detect from Camera...", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=80, y=480)
# Select Button
selectb=Button(window1, text="OPEN CAMERA",command=open_cam,  font=("Arial", 17), bg = "light green", fg = "blue")
selectb.place(x = 710, y = 488)

# info1 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
# info1.place(x=80, y=400)
#
# info2 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
# info2.place(x=80, y=480)

# Select Button
selectb=Button(window1, text="SELECT",command=open_img,  font=("Arial", 17), bg = "light green", fg = "blue")
selectb.place(x = 660, y = 80)
# Select Button
selectb=Button(window1, text="DETECT",command=det_img,  font=("Arial", 17), bg = "light green", fg = "blue")
selectb.place(x = 790, y = 80)

# Select Button
selectb=Button(window1, text="SELECT",command=open_vid,  font=("Arial", 17), bg = "light green", fg = "blue")
selectb.place(x = 660, y = 310)
# Select Button
selectb=Button(window1, text="DETECT",command=det_vid,  font=("Arial", 17), bg = "light green", fg = "blue")
selectb.place(x = 790, y = 310)


def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 780, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()
