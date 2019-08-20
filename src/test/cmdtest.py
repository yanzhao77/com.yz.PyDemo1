# import jpype
import tkinter as tk
from multiprocessing import Process, Pipe, Queue
import sys
import os


def func(event):
    cmd = input_var.get()
    e0.config(state=tk.NORMAL)
    e0.insert(tk.END, cmd + "\n")
    e0.config(state=tk.DISABLED)
    input_var.set("")
    conn2.send(cmd)


class Piao(Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe

    # def execute_cmd(selfself):
    def run(self):
        while True:
            exec(self.pipe.recv())


if __name__ == '__main__':
    window = tk.Tk()
    # 设置标题
    window.title("cmdTest")
    # 设置窗口大小
    window.geometry('500x350')
    # 保持窗口不变
    window.resizable(False, False)

    e0 = tk.Text(window, width=70, height=25, state=tk.DISABLED)
    e0.pack()

    input_var = tk.StringVar()
    e1 = tk.Entry(window, textvariable=input_var, width=70)
    e1.pack()
    window.bind("<Return>", func)
    window.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

    # 进程间通信管道
    conn1, conn2 = Pipe(duplex=False)
    # 创建并启动子进程并传递参数
    # p=Process(target=execute_cmd,args=(conn1,conn2))
    p = Piao(conn1)
    p.daemon = True
    p.start()

    window.mainloop()
    p.join()

