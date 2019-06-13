import tkinter as tk
import threading
import imageio
import time
from PIL import Image, ImageTk

video_name = "watchdogs_loading.gif" #This is your video file path
video = imageio.get_reader(video_name)




for image in video.iter_data():
    time.sleep(0.05)
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
    label.config(image=frame_image)
    label.image = frame_image



if __name__ == "__main__":

    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()