import can
import queue
from tkinter import *
from tkinter import messagebox
from threading import Thread, Event
from datetime import *
import time

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()

q = queue.Queue()
AcceptedNodes = [0x584, 0x604]


class bThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.can_run = Event()
        self.term = Event()
        self.can_run.set()
        self.term.clear()   
    
    def pause(self):
        self.can_run.clear()

    def resume(self):
        self.can_run.set()

    def terminate(self):
        self.term.set()


class can_rx_queue(bThread):
    def run(self):
        while True:
            if self.can_run.is_set():
                can_data = bus.recv()
                q.put(can_data)

            if self.term.is_set():
                break


class queue_read(bThread):
    def run(self):
        while True:
            if self.can_run.is_set():
                if q.empty() is False:
                    message = q.get()
                    if message.arbitration_id in AcceptedNodes:
                        d = '|{}|'.format(datetime.fromtimestamp(message.timestamp).time())
                        h = '{:x}:{:x}:{:x}:{:x}|'.format(message.data[0], message.data[1],
                                                          message.data[2], message.data[3])
                        b = '{:x}:{:x}:{:x}:{:x}|'.format(message.data[4], message.data[5],
                                                          message.data[6], message.data[7])
                        w1 = '{}+{}={}|'.format(message.data[4], message.data[5], (message.data[5] << 8) + message.data[4])
                        w2 = '{}+{}={}|'.format(message.data[6], message.data[7], (message.data[7] << 8) + message.data[6])
                        dw = '{}|'.format((message.data[7] << 24) + (message.data[6] << 16) +
                                          (message.data[5] << 8) + message.data[4])
                        print('{}{}{}{}{}{}\r'.format(d, h, b, w1, w2, dw))
            
            if self.term.is_set():
                break


class can_send(bThread):
    def __init__(self):
        bThread.__init__(self)
        self.can_run.clear()
        
    def run(self):
        while True:
            if self.can_run.is_set():
                msg = can.Message(arbitration_id=0x604,
                                  data=[0x40, int(b1Entry.get(), 16), int(b2Entry.get(), 16),
                                        int(b3Entry.get(), 16), 0x00, 0x00, 0x00, 0x00],
                                  extended_id=False)
                bus.send(msg)
                time.sleep(1)
            
            if self.term.is_set():
                break


def can_ctrl(cmd):
    if cmd == 1 and not len(b1Entry.get()) == 0 and not len(b2Entry.get()) == 0 and not len(b3Entry.get()) == 0:
        s_can.resume()
        b1Entry.config(state='readonly')
        b2Entry.config(state='readonly')
        b3Entry.config(state='readonly')
    if len(b1Entry.get()) == 0 or len(b2Entry.get()) == 0 or len(b3Entry.get()) == 0:
        messagebox.showinfo('Indtastnings fejl', 'Du mangler at indtaste data i en af byte felterne.')
    if cmd == 0:
        s_can.pause()
        b1Entry.config(state='normal')
        b2Entry.config(state='normal')
        b3Entry.config(state='normal')


def stop_GUI():
    s_can.terminate()
    t_can.terminate()
    t_queue.terminate()
    root.destroy()
    exit()

root = Tk()

root.title('Pelle TX GUI')
b1Label = Label(root, text="Byte 1")
b2Label = Label(root, text="Byte 2")
b3Label = Label(root, text="Byte 3")
b1Entry = Entry(root)
b2Entry = Entry(root)
b3Entry = Entry(root)
sendButton = Button(root, text="CAN - Start", command=lambda: can_ctrl(1))
stopButton = Button(root, text="CAN - stop", command=lambda: can_ctrl(0))
endButton = Button(root, text="Terminate GUI", command=lambda: stop_GUI())

b1Label.grid(row=0, column=0)
b2Label.grid(row=0, column=1)
b3Label.grid(row=0, column=2)
b1Entry.grid(row=1, column=0)
b2Entry.grid(row=1, column=1)
b3Entry.grid(row=1, column=2)
sendButton.grid(row=3, column=0)
stopButton.grid(row=3, column=1)
endButton.grid(row=3, column=2)

t_can = can_rx_queue()
t_queue = queue_read()
s_can = can_send()


def main():
    t_can.start()
    t_queue.start()
    s_can.start()
    root.mainloop()


if __name__ == '__main__':
    main()
