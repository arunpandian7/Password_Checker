from tkinter import *
import password_cracker as pc
from PIL import Image, ImageTk
import time
import imageio
import threading


video_name = "watchdogs_loading.gif" #This is your video file path
video = imageio.get_reader(video_name)


def stream(label):
    global end
    for image in video.iter_data():
        time.sleep(0.05)
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
    else:
        end = True


def check_button_press():
    global end
    end = False
    password = password_entry.get()
    hacked, attempts, time_taken = pc.cracker(password)
    window = Toplevel(root)
    window.configure(bg='black')
    window.geometry('600x300')
    gif_label = Label(window, bg='black')
    gif_label.place(x=0, y=0, relwidth=1, relheight=1)
    thread = threading.Thread(target=stream, args=(gif_label,))
    thread.daemon = 1
    thread.start()
    if hacked:
        while not end:
            continue
        else:
            hacked_pic = Image.open('hacked.jpg')
            tk_hacked_pic = ImageTk.PhotoImage(hacked_pic)
            hacked_label = Label(window, image=tk_hacked_pic)
            hacked_label.pack()
















if __name__ == '__main__':
    # Main window Background setup
    root = Tk()
    size = (600, 400)
    root.geometry('600x300')
    bg_img = Image.open('DEDSEC_2560x1440.jpg')
    bg_img.thumbnail(size)
    tk_bg_img = ImageTk.PhotoImage(bg_img)
    background = Label(root, image=tk_bg_img)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # # Frames

    topFrame = Frame(root, height=100, width=400)
    topFrame.pack(side=TOP)


    # Top Frame
    title = Label(topFrame, text='Password Checker', font=('MS Sans Serif', 14, 'bold'), bg='black', fg='Grey')
    title.pack(side=TOP)

    # Middle Frame
    frame = Frame(root, bg='black')
    frame.pack(side=TOP)
    password_entry = Entry(frame, show='*')
    password_entry.grid(row=2, column=2)
    text_prompt = Label(frame, text='Enter the Password', font=('Monospace', 12), bg='black', fg='Grey')
    text_prompt.grid(row=1, column=2)
    submit_button = Button(frame, text='Check', font=('Monospace', 12), bg='Grey', fg='Black',command=check_button_press)
    submit_button.grid(row=3, column=2)




    root.title('Password Checker')
    root.mainloop()