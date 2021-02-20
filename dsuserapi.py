import requests
import json
import time
import socket
import asyncio

#RelativeModder, 2021. MIT License

class Locales():
    '''All Language Locales goes here'''
    dansk="da"
    deutsch="de"
    english_gb="en-GB"
    english_us="en-US"
    english="en-US"
    spanish = "es-ES"
    french = "fr"
    horvatski = "hr"
    italian = "it"
    netherland = "nl"
    russian = "ru"
    ukrainian = "uk"
class Account():
    '''User object ~ Account Object'''
    id:int
    username:str
    avatar_id:str
    discriminator:int
    public_flags:int
class User():
    '''Discord user: id, username, avatar_id, discriminator, premium_since'''
    id:int
    username:str
    avatar_id:str
    discriminator:int
    premium_since:(None, str)
class Message():
    message_id:str
    message_type:0
    content:str
    channel_id:int
    author:Account()
    attachments:list
    embeds:list
    mentions:list
    mention_roles:list
    pinned:bool
    mention_everyone:bool
    tts:bool
    timestamp:str
    edited_timestamp:(str, None)
    flags:str
class Theme():
    '''dark or light theme'''
    dark = "dark"
    light = "light"
class ExplicitContentFilter():
    '''Filter of Explicit content:
    everyone
    friends
    noscan'''
    everyone = 2
    friends = 1
    noscan = 0
class MessageDisplay():
    '''Mode of Message displaying:
    cozy
    compact'''
    cozy = False
    compact = True
def createDM(recipient:int, token:str, debug=False):
    '''Returns DM channel ID'''
    url = "https://discord.com/api/v8/users/@me/channels"
    headers = {
        'authorization': token
    }
    payload = {
        'recipients': [recipient]
    }
    response = requests.post(url, headers=headers, json=payload)
    if(debug):
        print(response.text)
    return json.loads(response.text)["id"]
def SendMessage(channel:int ,token:str, content:str, tts=False, embed:str="", debug=False, addtitonal_fields:dict={}):
    '''Sends message to Channel'''
    headers = {
        'authorization': token
    }
    payload = {
        'content': content,
        'tts': tts,
        'embed': embed
    }
    response = requests.post("https://discord.com/api/v8/channels/"+str(channel)+"/messages", headers=headers, json=payload)
    if(debug):
        print(response.text)
    return json.loads(response.text)["id"]
def changeStatus( token:str, text:str, emoji_name="", emoji_id=0, status="online"):
    '''Changing your Discord status such as:
    status of online: idle, dnd, online, invisible
    custom text status
    custom emoji status'''
    url = "https://discord.com/api/v8/users/@me/settings"
    headers = {
        'authorization': token
    }
    payload = {
        'status': status,
        'custom_status': {'text':text, 'emoji_name':emoji_name}
    }
    response = requests.patch(url, headers=headers, json=payload)
    return response.text
def getUserInfo(token:str, user_id:int)->User:
    '''Getting info about User'''
    url = "https://discord.com/api/v8/users/"+str(user_id)+"/profile"
    headers = {
        'authorization': token
    }
    response = requests.get(url, headers=headers)
    info = json.loads(response.text)
    u = User()
    u.id = info["user"]["id"]
    u.username = info["user"]["username"]
    u.avatar_id = info["user"]["avatar"]
    u.discriminator = info["user"]["discriminator"]
    u.premium_since = info["premium_since"]
    return u
def makeFakeRPC(token:str, app_id:int):
    '''Making fake Rich Presence(in development)'''
    url="https://discord.com/api/v8/oauth2/applications"+str(app_id)+"/rpc"
    headers = {
        'authorization': token
    }
    req = requests.get(url, headers=headers)
    print(req.text)
def changeTheme(token:str, state:Theme):
    '''Changes mode of theme like: dark or light'''
    url = "https://discord.com/api/v8/users/@me/settings"
    headers = {
        'authorization': token
    }
    payload = {
        'theme': state
    }
    req = requests.patch(url, headers=headers, json=payload)
    return req
def changeExplicitContentFilter(token:str, level:ExplicitContentFilter):
    '''Changes Explicit Filter Content Level'''
    url = "https://discord.com/api/v8/users/@me/settings"
    headers = {
        'authorization': token
    }
    payload = {
        'explicit_content_filter': level
    }
    req = requests.patch(url, headers=headers, json=payload)
    return req
def changeMessageDisplay(token:str, mode:MessageDisplay):
    '''Changes Message Display Mode (cozy, compact)'''
    url = "https://discord.com/api/v8/users/@me/settings"
    headers = {
        'authorization': token
    }
    payload = {
        'message_display_compact': mode
    }
    req = requests.patch(url, headers=headers, json=payload)
    return req
def changeLocale(token:str, locale:Locales):
    '''Changes interface language'''
    url = "https://discord.com/api/v8/users/@me/settings"
    headers = {
        'authorization': token
    }
    payload = {
        'locale': locale
    }
    req = requests.patch(url, headers=headers, json=payload)
    return req
def call(token:str, voice_channel_id:int):
    '''Calls to voice channel (in development)'''
    url = "https://discord.com/api/v8/channels/"+str(voice_channel_id)+"/call"
    headers = {
        'authorization': token
    }
    response = requests.get(url, headers=headers)
    return response.text
def typing(token:str, channel:int):
    '''Making user "typing" the message'''
    url = "https://discord.com/api/v8/channels/"+str(channel)+"/typing"
    headers = {
        'authorization': token
    }
    response = requests.post(url, headers=headers)
    return response.text
def getRelationShips(token:str, user_id):
    '''Gets Mutual Friends of User'''
    url="https://discord.com/api/v8/users/"+str(user_id)+"/relationships"
    headers = {
        'authorization': token
    }
    req = requests.get(url, headers=headers)
    members=[]
    for member in req.json():
        m = Account()
        m.id=member["id"]
        m.username=member["username"]
        m.avatar_id=member["avatar"]
        m.discriminator=member["discriminator"]
        m.public_flags=member["public_flags"]
        members.append(m)
    return members
def login(login:str, password:str):
    '''Direct Auth with login and password\r\n
    Returns: token'''
    payload = {
        'captcha_key': None,
        'login': login,
        'password': password
    }
    req = requests.post("https://discord.com/api/v8/auth/login", json=payload)
    return req.json()["token"]
def deleteMessage(token:str, message_id:int, channel_id:int):
    url = "https://discord.com/api/v8/channels/"+str(channel_id)+"/messages/"+str(message_id)
    headers = {
        'authorization': token
    }
    requests.delete(url, headers=headers)
def editMessage(token:str, message_id:int, channel_id:int, content:str):
    url = "https://discord.com/api/v8/channels/"+str(channel_id)+"/messages/"+str(message_id)
    headers = {
        'authorization': token
    }
    payload = {
        'content': content
    }
    requests.patch(url, headers=headers, json=payload)
def getMessages(token:str, channel_id:int, limit:int=50):
    '''Returns Messages in channel'''
    url = "https://discord.com/api/v8/channels/"+str(channel_id)+"/messages?limit="+str(limit)
    headers = {
        'authorization': token
    }
    response = requests.get(url, headers=headers)
    messages = response.json()
    message_list = []
    for message in messages:
        model = Message()
        model.message_id = message["id"]
        model.message_type = message["type"]
        model.content = message["content"]
        model.channel_id = message["channel_id"]
        author = Account()
        author.id = message["author"]["id"]
        author.username = message["author"]["username"]
        author.avatar_id = message["author"]["avatar"]
        author.discriminator = message["author"]["discriminator"]
        author.public_flags = message["author"]["public_flags"]
        model.author = author
        model.content = message["content"]
        model.attachments = message["attachments"]
        model.embeds = message["embeds"]
        model.mentions = message["mentions"]
        model.mention_roles = message["mention_roles"]
        model.pinned = message["pinned"]
        model.mention_everyone = message["mention_everyone"]
        model.tts = message["tts"]
        model.timestamp = message["timestamp"]
        model.edited_timestamp = message["edited_timestamp"]
        model.flags = message["flags"]
        message_list.append(model)
    return message_list


def getLatest(token, dmid):
    latest_message = getMessages(token, dmid, 1)
    return latest_message[0]





#end
