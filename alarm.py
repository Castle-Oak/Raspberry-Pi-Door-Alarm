#!/usr/bin/env python3

import boto3
from gpiozero import Button
import time
from datetime import datetime
import http.client
import urllib
import sys

button = Button(2)
last_known_state = "closed"
secret_name = sys.argv[1]
timer_start = 0


def get_secrets(secret):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret)

    return eval(response['SecretString'])


def pushover(token, user, message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                urllib.parse.urlencode({
                    "token": token,
                    "user": user,
                    "message": message,
                }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()

secrets_dict = get_secrets(secret_name)

init_time = datetime.now().isoformat()
init_message = "Door Alarm Online\n{}".format(init_time)
pushover(secrets_dict['token'],
         secrets_dict['user'],
         init_message
         )

print("Waiting for input")

while True:
    if not button.is_pressed and last_known_state == "closed":
        timer_start = time.time()
        current_time = datetime.now().isoformat()
        message = "Door OPENED at {}".format(current_time)
        print(message)
        pushover(secrets_dict['token'],
                 secrets_dict['user'],
                 message
                 )
        last_known_state = "open"
        time.sleep(1)

    if button.is_pressed and last_known_state == "open":
        timer_end = time.time()
        elapsed_time = int(timer_end - timer_start)
        current_time = datetime.now().isoformat()
        message = (
                "Door CLOSED at {}\n"
                "Elapsed time ajar: {} seconds".format(current_time, elapsed_time)
                )
        print(message)
        pushover(secrets_dict['token'],
                 secrets_dict['user'],
                 message
                 )
        last_known_state = "closed"
        time.sleep(1)
