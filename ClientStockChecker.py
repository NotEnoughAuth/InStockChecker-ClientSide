import time
import tkinter
import tkinter as tk
import threading
import websocket

ws = None
allStop = False


def searchingDisplay():
    global allStop
    while not allStop:
        time.sleep(1)
        lbl_search["text"] = "Searching."
        time.sleep(1)
        lbl_search["text"] = "Searching.."
        time.sleep(1)
        lbl_search["text"] = "Searching..."


def search():
    global ws
    ws = websocket.create_connection("ws://localhost:44932/")
    lbl_search["text"] = "Testing Connection..."
    ws.send('ping')
    if ws.recv() == 'pong':
        lbl_search["text"] = "Connection Successful!"
        time.sleep(0.5)
        lbl_search["text"] = "Sending URLs to Server..."
        urls = txt_urls.get(1.0, tkinter.END).splitlines()
        for url in urls:
            ws.send(url)
        ws.send("EndOfURLTransmission")
        lbl_search["text"] = ws.recv()
        t1 = threading.Thread(target=searchingDisplay)
        t1.start()

def on_closing():
    global allStop
    if ws is not None:
        ws.close()
    allStop = True
    window.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    window.title("OPPrototyping Stock Checker")

    txt_urls = tk.Text(window)
    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_SearchFor = tk.Button(frm_buttons, text="Search URLs", command=search)
    lbl_search = tk.Label(text="")

    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure(1, minsize=50, weight=1)

    btn_SearchFor.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    lbl_search.grid(row=1, column=0, sticky="ew", padx=5)
    frm_buttons.grid(row=0, column=0, sticky="ns")
    txt_urls.grid(row=0, column=1, sticky="nsew")

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
