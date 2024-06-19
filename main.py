from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    timer_txt.config(text='Timer')
    canvas.itemconfig(time_txt,text='00:00')
    checkmark.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1 
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_txt.config(text='Long Break',fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_txt.config(text='Short Break',fg=PINK)
    else:
        count_down(work)
        timer_txt.config(text='Focus',fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(time_txt,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ''
        work_done = math.floor(reps/2)
        for _ in range(work_done):
            marks += '✔'
        checkmark.config(text=marks)    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
# window.minsize(width=600,height=600)
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file = 'pomodoro/tomato.png')
canvas.create_image(100,112,image=photo)
time_txt = canvas.create_text(100,130,text='00:00', fill='white', font=('Comic Sans',20,'bold'))
canvas.grid(column=1,row=1)

timer_txt = Label(text='Timer', bg=YELLOW, font=('Comic Sans',25,'bold'), fg=GREEN)
timer_txt.grid(column=1,row=0)

checkmark = Label(bg=YELLOW, font=('Comic Sans',15,'bold'), fg=GREEN)
checkmark.grid(column=1,row=3)

start = Button(text='START',highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

reset = Button(text='RESET',highlightthickness=0,command=reset_time)
reset.grid(column=2,row=2)


window.mainloop()