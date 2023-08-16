import threading
import queue
import sys

import requests
import time

import argparse

from termcolor import colored


q = queue.Queue()
valid_proxies = []

proxies = []


with open("proxies.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


def strawpoll_vote():

    global q
    global valid_proxies
    while not q.empty():
        starttime = int(round(time.time() * 1000))
        proxy = q.get()
        try:

            res = requests.post("http://ipinfo.io/json",
                                proxies={
                                    "http": proxy, "https": proxy
                                })


            try:
                latency = int(round(time.time() * 1000)) - starttime
                print(res.json()["ip"] + " (" + str(latency) + "ms)")
            except:
                continue
        except:
            continue




#for t in range(len(proxies)):
#    threading.Thread(target=strawpoll_vote).start()

import requests
from bs4 import BeautifulSoup

url = "https://strawpoll.com/2ayLkrRKAZ4"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

option_elements = soup.find_all(class_="strawpoll-option")

for option in option_elements:
    print("Option:", option.text.strip())

