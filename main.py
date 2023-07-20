from tkinter import *
import serial


ser = serial.Serial(
    port='COM5',
    baudrate=9600,
    timeout=1
)
ser.close()
ser.open()
ser.isOpen()


def send(number):
    number = number - 1
    ser.write(bytes(str(number), 'utf-8'))


root = Tk()

root.title('Jogo do Galo')

buttons = []
frames = []

k = 1

frames.append(Frame(root))
frames[-1].pack()
buttons.append(Button(frames[-1], text="1", width=10, height=4, command=lambda: send(1)))
buttons[-1].pack(side=LEFT)
buttons.append(Button(frames[-1], text="2", width=10, height=4, command=lambda: send(2)))
buttons[-1].pack(side=LEFT)
buttons.append(Button(frames[-1], text="3", width=10, height=4, command=lambda: send(3)))
buttons[-1].pack(side=LEFT)
frames.append(Frame(root))
frames[-1].pack()
buttons.append(Button(frames[-1], text="4", width=10, height=4, command=lambda: send(4)))
buttons[-1].pack(side=LEFT)
buttons.append(Button(frames[-1], text="5", width=10, height=4, command=lambda: send(5)))
buttons[-1].pack(side=LEFT)
buttons.append(Button(frames[-1], text="6", width=10, height=4, command=lambda: send(6)))
buttons[-1].pack(side=LEFT)
frames.append(Frame(root))
frames[-1].pack()
buttons.append(Button(frames[-1], text="7", width=10, height=4, command=lambda: send(7)))
buttons[-1].pack(side=LEFT)
buttons.append(Button(frames[-1], text="8", width=10, height=4, command=lambda: send(8)))
buttons[-1].pack(side=LEFT)
buttons.append(Button(frames[-1], text="9", width=10, height=4, command=lambda: send(9)))
buttons[-1].pack(side=LEFT)


resetButton = Button(root, text="Reset", width=33, height=4, command=lambda: send(10))
resetButton.pack()


def read():
    if ser.inWaiting() == 0:
        return
    received = ser.readline().strip().decode("utf-8")
    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    root.after(1000, read)


root.after(1000, read)
root.mainloop()

ser.close()
