import time
import random
import sqlite3
import logging
import os
from datetime import datetime
from tkinter import *
#from tkinter.ttk import *

from binance_api import Binance

root = Tk() #tk - base class
root.title("myBot")
root.geometry("800x400")

bot = Binance(
    API_KEY='KfYHa2xsSrN4KiboFtz9vMb2yZqDFluAs95T70LSoCKxlibDhRuClNKd5dic30Fc',
    API_SECRET='cKnaQpzLDU46ZS0VPZhSnL9BMCgkkbdb8XhzilyZXNGFU6ChtyN6qfrL5rYbRPtL'
)

currency_labels = {
    'EUR': StringVar(root),
    'USD': StringVar(root),
    'CHF': StringVar(root),
    'GBP': StringVar(root)
}

bye = 'Goodbye'
def update_text():
    text2=bot.time()
    text.set(text2)

mess = bot.depth(
    symbol='BNBBTC',
    limit=5
)

text = StringVar()
local_time = int(time.time())
text.set(local_time)

lvar1 = 888888
lbl01 = Label(root, text="Time Stamp").grid(row=0, column=0)
lbl02 = Label(root, textvariable=text, width=30).grid(row=0, column=1)

lb01 = Listbox(root,width=10)
lb01.grid(row=0, column=2)

lb01.insert(END, 'tttttttt')

btn = Button(root, text="Click Me", width=30, command=update_text).grid(row=1,column=0)

print('account', bot.account())
print(bot.ping())
print(local_time)

root.mainloop()