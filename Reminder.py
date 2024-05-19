om tkinter import *
import tkinter as tk
import time
from plyer import notification

class ReminderApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        label_text = "I wrote this for myself\n\nThis is my little application" \
                     "\n\nNOTE: I am new to Python." \
                     "\n\nKeep in mind the math you need to know:" \
                     "\n\n0.1 = 10%, 0.5 = 50%" \
                     "\n\n6 seconds is 10 percent"

        label = tk.Label(self, text=label_text)
        label.place(x=0, y=40)

        Proceed = Button(self, text="Accept", command=self.show_reminder_app)
        Proceed.place(x=40, y=300)

        exitButton = Button(self, text="No", command=self.clickExitButton)
        exitButton.place(x=240, y=300)

    def clickExitButton(self):
        exit()

    def show_reminder_app(self):
        self.master.destroy()  # Hide the first GUI
        self.reminder_app = ReminderApp(self.master)

root = Tk()
app = ReminderApp(root)
root.wm_title("Read Me!")
root.geometry("350x350")
root.mainloop()


def set_reminder_hour():
    hour = reminder_text.get().lower()
    local_time = float(reminder_timehr.get())
    local_time = local_time * 3600

    root.destroy()

    while True:
        time.sleep(local_time)
        notification.notify(
            title="Reminder Hour/Loop",
            message=hour,
            timeout=10
        )

def set_reminder():
    txt = reminder_text.get().lower()
    local_time = float(reminder_time.get())
    local_time = local_time * 60

    root.destroy()

    while True:
        time.sleep(local_time)
        notification.notify(
            title="Reminder Minute/Loop",
            message=txt,
            timeout=10  # Adjust as needed
        )

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Reminder")

    # Create and pack a label widget
    label = tk.Label(root, text="What do you need to do today?")
    label.grid(row=0, column=0, columnspan=2)  # Use grid to span two columns

    # Create and pack an entry widget for reminder text
    reminder_text = tk.Entry(root)
    reminder_text.grid(row=1, column=0, columnspan=2, pady=10)  # Use grid to span two columns

    label_txt_rmdr = tk.Label(root, text="Set the time in minutes or hours:")
    label_txt_rmdr.grid(row=2, column=0, columnspan=2)  # Use grid to span two columns

    spacer = tk.Label(root, text="")  # Create an empty label as spacer
    spacer.grid(row=3, column=0, columnspan=2, pady=10)  # Use grid to span two columns

    # Create and pack a label widget for reminder time
    label_time = tk.Label(root, text="Minutes")
    label_time.grid(row=4, column=0)

    reminder_time = tk.Entry(root)
    reminder_time.grid(row=4, column=1, pady=10)  # Place reminder_time in the next column

    label_timehr = tk.Label(root, text="Hours")
    label_timehr.grid(row=5, column=0)

    reminder_timehr = tk.Entry(root)
    reminder_timehr.grid(row=5, column=1, pady=10)  # Place reminder_timehr in the next column

    label_help = tk.Label(root, text="The amount of time, in this, can use a decimal number")
    label_help.grid(row=6, column=0, columnspan=2)  # Use grid to span two columns

    label_help2 = tk.Label(root, text="(ie: 0.1 (6 seconds), 0.5 (30 seconds), 0.9 (54 seconds) hours should be similar")
    label_help2.grid(row=7, column=0, columnspan=2)  # Use grid to span two columns

    spacer1 = tk.Label(root, text="")
    spacer1.grid(row=9, column=1, columnspan=2, pady=10)

    label_before = tk.Label(root, text="Where you apply the Hours/Minutes you have imput:")
    label_before.grid(row=10, column=0, columnspan=2)

    spacer2 = tk.Label(root, text="")
    spacer2.grid(row=11, column=1, columnspan=2, pady=1)

    label_reminder = tk.Label(root, text="Remember, Hour and Minues are calculated with decimalpoints as well. Don't forget that 0.1=10%, 0.5=50%, and 0.9=90%")
    label_reminder.grid(row=12, column=0, columnspan=2)

    # Create and pack buttons using grid
    start_button = tk.Button(root, text="Start Reminder (Minutes)", command=set_reminder)
    start_button.grid(row=13, column=0, pady=10)

    start_button_hr = tk.Button(root, text="Start Reminder (Hours)", command=set_reminder_hour)
    start_button_hr.grid(row=13, column=1, pady=10) # Place start_button_hr in the next column

    label_eg = tk.Label(root, text="Errors can occur, and if they do? This simple reminder can be fixed easily. NOTE:")
    label_eg.grid(row=14, column=0, columnspan=2)

    label_eg2 = tk.Label(root, text="You *may* have to fix the notifcation area in the code for both the Hour, and Minute set.")
    label_eg2.grid(row=15, column=0, columnspan=2)

    label_eg3 = tk.Label(root, text="sudo apt install 'notifier'. As in, look for the 'notify' app on the internet, depending on distribution")
    label_eg3.grid(row=16, column=0, columnspan=2)

    # Start the GUI main loop
    root.mainloop()
