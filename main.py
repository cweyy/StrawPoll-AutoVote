import threading
import queue

import requests
import time

import argparse

from termcolor import colored


version = "1.0"
author = "cweyy"


parser = argparse.ArgumentParser(description="Poll voter")
parser.add_argument("--threads", type=int, help="Thread count")
parser.add_argument("--poll", type=str, help="Poll Value", required=True)  # Make --poll required
parser.add_argument("--vote", type=str, help="Vote Value", required=True)  # Make --vote required
parser.add_argument("--proxies", type=str, help="Proxies File", required=True)  # Make --proxies required

args = parser.parse_args()


q = queue.Queue()
valid_proxies = []

proxies = []

proxies_file = args.proxies


with open(proxies_file, "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

vote_id = args.vote
poll_id = args.poll
thread_amount = len(proxies)
if args.threads is not None:
    thread_amount = args.threads


watermark = colored("""


  ___ _                   ___     _ _ 
 / __| |_ _ _ __ ___ __ _| _ \___| | |
 \__ \  _| '_/ _` \ V  V /  _/ _ \ | |
 |___/\__|_|_\__,_|\_/\_/|_|_\___/_|_|
   /_\ _  _| |_ __\ \ / /__| |_ ___   
  / _ \ || |  _/ _ \ V / _ \  _/ -_)  
 /_/ \_\_,_|\__\___/\_/\___/\__\___| """ + colored("v" + version, "red") + " " + colored("-", "blue") + " " + colored(str(len(proxies)) + " proxies", "yellow") + """



""", "blue")




print(watermark)





def get_session(proxy):
    global poll_id
    res = requests.get("https://strawpoll.com/" + poll_id,
                       proxies={
                           "http": proxy, "https": proxy
                       }
                       )


    return str(res.cookies.get("session"))



def strawpoll_vote():

    global poll_id
    global vote_id

    global q
    global valid_proxies
    while not q.empty():
        starttime = int(round(time.time() * 1000))
        proxy = q.get()
        try:

            session = get_session(proxy)

            url = "https://api.strawpoll.com/v3/polls/" + poll_id + "/vote"

            headers = {
                "authority": "api.strawpoll.com",
                "method": "POST",
                "path": "/v3/polls/" + poll_id + "/vote",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                "Content-Length": "230",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "__utma=71717073.1551429603.1692118352.1692118352.1692118352.1; __utmc=71717073; __utmz=71717073.1692118352.1.1.utmcsr=support.fandom.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=212004932.905166849.1692120748.1692120748.1692120748.1; __utmc=212004932; __utmz=212004932.1692120748.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=212004932.1.10.1692120748; __utmt=1; session=" + session + "; __utmb=71717073.44.10.1692118352",
                "Origin": "https://strawpoll.com",
                "Referer": "https://strawpoll.com/",
                "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"macOS\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            }

            post_body = {
                "v": {
                    "id": "",
                    "name": "",
                    "pollVotes": [
                            {
                                "id": vote_id,
                                "value": 1
                            }
                    ],
                    "voteType": "add",
                    "token": "",
                    "isEmbed": False,
                    "opfp1": 1700665210,
                    "opfp2": 2279472876
                },
                "h": False,
                "ht": False,
                "token": None
            }

            res = requests.post(url,
            proxies={
                "http": proxy, "https": proxy
            },
            headers=headers,
            json=post_body)

        except Exception as e:
            print(e)
            continue

        latency = int(round(time.time() * 1000)) - starttime

        if("error" not in res.json()):
            print(colored(proxy, "green") + "   " + colored("(" + str(latency) + "ms)", "yellow"))
        else:
            print(colored(proxy, "red") + "   " + colored("(" + str(latency) + "ms)", "yellow"))


def add_proxy_to_file(proxy):
    filename = "valid_http_proxies.txt"

    try:
        with open(filename, 'r') as file:
            existing_proxies = file.read()
    except FileNotFoundError:
        with open(filename, 'w') as file:
            existing_proxies = ""

    if proxy not in existing_proxies:
        with open(filename, 'a') as file:
            file.write(proxy + '\n')
            return
    else:
        return


for t in range(thread_amount):
    threading.Thread(target=strawpoll_vote).start()
