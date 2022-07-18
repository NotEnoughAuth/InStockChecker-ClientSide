import time
import tkinter as tk
import threading
import websocket
from websocket import create_connection

def searchingDisplay():
    while True:
        time.sleep(1)
        lbl_search["text"] = "Searching."
        time.sleep(1)
        lbl_search["text"] = "Searching.."
        time.sleep(1)
        lbl_search["text"] = "Searching..."

def search():
    ws = create_connection("ws://localhost:44932/websocket")
    lbl_search["text"] = "Testing Connection..."
    ws.send('ping')
    if ws.recv() == 'pong':
        lbl_search["text"] = "Connection Successful!"
    t1 = threading.Thread(target=searchingDisplay)
    t1.start()



window = tk.Tk()
window.title("OPPrototyping Stock Checker")

txt_urls = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_SearchFor = tk.Button(frm_buttons, text="Search URLs",command=search)
lbl_search = tk.Label(text="")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(1, minsize=50, weight=1)

btn_SearchFor.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
lbl_search.grid(row=1, column=0, sticky="ew", padx=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_urls.grid(row=0, column=1, sticky="nsew")
window.mainloop()
