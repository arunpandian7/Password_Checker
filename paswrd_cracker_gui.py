from tkinter import *
import password_cracker as pc
from PIL import Image, ImageTk
import time
import imageio
import threading


video_name = "watchdogs_loading.gif"
video = imageio.get_reader(video_name)


def stream(label, hack_flag):
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
        time.sleep(0.05)
    else:
        if hack_flag:
            hacked_pic = Image.open('hacked.jpg')
            hacked_pic.thumbnail((300, 400))
            tk_hacked_pic = ImageTk.PhotoImage(hacked_pic)
            hacked_label = Label(window, image=tk_hacked_pic, bg='black')
            hacked_label.image = tk_hacked_pic
            hacked_label.pack()
            text_message = ' Your Password has been identified as leaked or weak \n' \
                           ' Please change your password in respective website'
            message_label = Label(window, text=text_message, font=('HACKED', 14, 'bold'), bg='black', fg='white')
            message_label.pack()
        else:
            congrats_message = 'Your password is not found in the database. \n' \
                                'But we recommend you to change the \n' \
                               'password frequently to stay safe. \n' \
                                'Happy Internet :) </>'
            message_label = Label(window, text=congrats_message, font=('HACKED', 14, 'bold'), bg='black', fg='white')
            message_label.pack()


def check_button_press():
    global end
    global window
    end = False
    password = password_entry.get()
    window = Toplevel(root)
    window.configure(bg='black')
    window.geometry('600x350')
    gif_label = Label(window, bg='black')
    gif_label.place(x=0, y=0, relwidth=1, relheight=1)
    hacked = pc.cracker(password)
    thread = threading.Thread(target=stream, args=(gif_label, hacked,))
    thread.daemon = 1
    thread.start()


if __name__ == '__main__':
    # Main window Background setup
    root = Tk()
    size = (600, 450)
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
