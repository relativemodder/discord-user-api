import dsuserapi
from dsuserapi import Theme
from dsuserapi import ExplicitContentFilter as ECF
from dsuserapi import MessageDisplay as MD
from dsuserapi import Locales as L

tok = "Your Discord Token"

dsuserapi.changeLocale(tok, L.russian) #Changes language


dsuserapi.changeStatus(tok, "Hi! It's my custom status!", status="idle") #Sets your own status


dsuserapi.changeTheme(tok, Theme.light) #Sets theme


dsuserapi.changeExplicitContentFilter(tok, ECF.friends) #Sets explicit content filter level