import can
import queue
from tkinter import *
from threading import Thread
from datetime import *

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()

q = queue.Queue()
AcceptedNodes = [0x584, 0x604]


def can_rx_queue():
    while True:
        can_data = bus.recv()
        q.put(can_data)


def queue_read():
    while True:
        if q.empty() is False:
            message = q.get()
            if message.arbitration_id in AcceptedNodes:
                d = '|{0}|{1:x}|{2:x}|'.format(datetime.fromtimestamp(message.timestamp),
                                               message.arbitration_id,
                                               message.dlc)
                h = '{:x}:{:x}:{:x}:{:x}|'.format(message.data[0], message.data[1],
                                                  message.data[2], message.data[3])
                b = '{:x}:{:x}:{:x}:{:x}|'.format(message.data[4], message.data[5],
                                                  message.data[6], message.data[7])
                print('{}{}{}\r\n'.format(d, h, b))


t_can = Thread(target=can_rx_queue)
t_can.start()
t_queue = Thread(target=queue_read)
t_queue.start()


def can_send():
    msg = can.Message(arbitration_id=0x604,
                      data=[0x40, int(b1Entry.get(), 16), int(b2Entry.get(), 16),
                            int(b3Entry.get(), 16), 0x00, 0x00, 0x00, 0x00],
                      extended_id=False)
    bus.send(msg)


def can_stop():
    print("Tryk CTRL+C for at afslutte script")
    root.destroy()


root = Tk()
b1Label = Label(root, text="Byte 1")
b2Label = Label(root, text="Byte 2")
b3Label = Label(root, text="Byte 3")
b1Entry = Entry(root)
b2Entry = Entry(root)
b3Entry = Entry(root)
sendButton = Button(root, text="Send", command=can_send)
stopButton = Button(root, text="Stop", command=can_stop)

b1Label.grid(row=0, column=0)
b2Label.grid(row=0, column=1)
b3Label.grid(row=0, column=2)
b1Entry.grid(row=1, column=0)
b2Entry.grid(row=1, column=1)
b3Entry.grid(row=1, column=2)
sendButton.grid(row=3, column=0)
stopButton.grid(row=3, column=2)

root.mainloop()
