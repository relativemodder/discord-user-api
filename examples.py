import dsuserapi as ds
import time
import asyncio
import os
tok = "DISCORD TOKEN GOES HERE"

dmid = ds.createDM(948280942804829, tok) #FAKE USER ID, PUT THE REAL ONE

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
            if("/embed" in i.content):
                titleofembed = i.content.split('"')[1]
                colorofembed = i.content.split('"')[2]
                ds.deleteMessage(tok, int(i.message_id), dmid)
                ds.SendMessage(dmid, tok, "", embed={'title': titleofembed, 'color': int(colorofembed, 16)})
            lid = i
        time.sleep(0.1)
def start_listen_messages(token, dmid):
    asyncio.run(listen_messages(token, dmid))
start_listen_messages(tok, dmid)
