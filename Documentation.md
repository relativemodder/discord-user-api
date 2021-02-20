# Docs of DiScord User Api

*This library need for interacting with Discord from user's account*

## ONLY EDUCATIONAL PURPOSES!

Let's begin with a couple of classes!


# *Classes in dsuserapi*


### class Locales():

_All Language Locales goes here_

♦ dansk

♦ deutsch

♦ english_gb

♦ english_us

♦ english

♦ spanish

♦ french

♦ horvatian

♦ italian

♦ netherland

♦ russian

♦ ukrainian


### Account or User()

>  id - *The id of User()*
  
>  username - *Username of User()*
  
>  avatar_id - *Asset id of user's avatar*
  
>  discriminator - *Discriminator of user, example: RelativeModder<b>#5090</b>*
  
>  public_flags - *Public flags of user*

### Message()

> message_id - *ID of message*
> 
> message_type - *Number of a type of message*
> 
> content - *Content of message*
> 
> channel_id - *Channel_id of message, where it was sent*
> 
> author - *Account() of sender*
> 
> attachments - *List of attachments*
> 
> embeds - *List of embeds*
> 
> mentions - *list of mentions*
> 
> mention_roles - *list of role(s) mention(s)
> 
> pinned - *is pinned (bool)*
> 
> mention_everyone - *is message mentioned everyone*
> 
> tts - *is message using TTS (Text-to-Speech) (bool)*
> 
> timestamp - *timestamp of the message, idk how to parse it .-.
> 
> edited_timestamp - *timestamp of the edit*
> 
> flags - *message flags (idk what is it)


## Theme

### Oh, it's simple!

Theme():

>dark - *dark theme*
>
>light - *light theme*
>


## ExplicitContentFilter

>everyone - *Scan NSFW content from all members*
>
>friends - *Scan NSFW content only from friends*
>
>noscan - *My friends are good!*
>

## MessageDisplay

>cozy - *cozy message displaying*
>
>compact - *compact message displaying*
>

### And now...

# Methods!

## createDM(recepient_user_id, token)

**Returns channel_id of user**

## SendMessage(channel_id, token, content, tts=False, embed={})

**Sends Message() and returns ID**

## change_status(token, text, emoji_name, status="online")

>statuses: online, idle, dnd, invisible
>
**Returns: None**

## change_theme(token, theme)

>theme - Theme() state
>
**Returns: None**

## getUserInfo(token, user_id)

**Returns: User()**

## changeExplicitContentFilter(token, level:ExplicitContentFilter)

**Returns: None

## typing(token, channel_id)

>Now you are typing! Wow!
>

## getRelationShips(token, user_id)

**Returns: list of Account() of mutual friends


## login(email_or_phone, password) -> Direct Authorization

**Returns: **
