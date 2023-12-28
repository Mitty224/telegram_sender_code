from telethon.sync import TelegramClient
import time

user_id_2 = '' # your telegram id
api_id = 0  # your telegram api id
api_hash = "" # your telegram api hash (you can get it on https://my.telegram.org)
send_id = '' # the person who you send
message = '' 
repeat = 1 # how many times you want send message
shedule = 0 # if repeat > 1 with Time you can send message every given seconds

sender = TelegramClient(user_id_2, api_id, api_hash)

async def main():
    for i in range(repeat):
        await sender.send_message(send_id, message=message)
        time.sleep(shedule)

with sender:
    sender.loop.run_until_complete(main())
