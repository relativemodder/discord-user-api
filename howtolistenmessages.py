import dsuserapi as ds
import time
import asyncio
import os
tok = "Put token here :)"

dmid = 83982479282 #Fake ID, put the real one

def on_message_new(message:ds.Message):
    print(message.author.username, " написал(а): ", message.content)
def getLatest(token, dmid):
    latest_message = ds.getMessages(token, dmid, 1)
    return latest_message[0]

async def listen_messages(token, dmid):
    lid = getLatest(token, dmid)
    while True:
        i = getLatest(token, dmid)
        if(i.message_id!=lid.message_id):
            on_message_new(i)
            print(i.author.username, "wrote:", i.content) # On new message it prints username and content of the new message
            lid = i
        time.sleep(0.1)
def start_listen_messages(token, dmid):
    asyncio.run(listen_messages(token, dmid))
start_listen_messages(tok, dmid)
