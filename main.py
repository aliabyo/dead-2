import os
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from emotes import Emotes
from highrise.models import SessionMetadata,  GetMessagesRequest, User ,Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
from highrise.__main__ import *
import asyncio, random
import requests
from highrise import BaseBot, AnchorPosition, Position, User, TaskGroup

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token
class ResponseError(Exception):
  pass

class Counter:
    bot_id = ""
    static_ctr = 0
    usernames = ['Alionardo_']

class Bot(BaseBot):
    continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}  
    user_data: Dict[int, Dict[str, Any]] = {}
    continuous_emote_task = None
    cooldowns = {}  # Class-level variable to store cooldown timestamps
    emote_looping = False
    def __init__(self):
      super().__init__()
      self.maze_players = {}
      self.user_points = {}  # Dictionary to store user points
      self.following_username = None
      self.Emotes = Emotes
      self.should_stop = False
        
    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            
            await self.highrise.walk_to(Position(7, 0,7, "FrontRight"))
            await asyncio.sleep(3)
            await self.highrise.chat(" on duty!")
            item = await self.webapi.get_items(item_name="Top Knot") 
            item_id = item.items[0].item_id
            print(item_id)

            while True:
              await self.highrise.chat("Welcome to FIND A DATE")
              await asyncio.sleep(2)
        except Exception as e:
            print(f"error : {e}")
    async def run_bot(self, room_id, api_key) -> None:
      asyncio.create_task(self.place_bot())
      definitions = [BotDefinition(self, room_id, api_key)]
      await __main__.main(definitions)

    async def on_chat(self, user: User, message: str):
        try:

            if message == "!fit": 
               shirt = ["shirt-n_starteritems2019tankwhite", "shirt-n_starteritems2019tankblack", "shirt-n_starteritems2019raglanwhite", "shirt-n_starteritems2019raglanblack", "shirt-n_starteritems2019pulloverwhite", "shirt-n_starteritems2019pulloverblack", "shirt-n_starteritems2019maletshirtwhite", "shirt-n_starteritems2019maletshirtblack", "shirt-n_starteritems2019femtshirtwhite", "shirt-n_starteritems2019femtshirtblack", "shirt-n_room32019slouchyredtrackjacket", "shirt-n_room32019malepuffyjacketgreen", "shirt-n_room32019longlineteesweatshirtgrey", "shirt-n_room32019jerseywhite", "shirt-n_room32019hoodiered", "shirt-n_room32019femalepuffyjacketgreen", "shirt-n_room32019denimjackethoodie", "shirt-n_room32019croppedspaghettitankblack", "shirt-n_room22109plaidjacket", "shirt-n_room22109denimjacket", "shirt-n_room22019tuckedtstripes", "shirt-n_room22019overalltop", "shirt-n_room22019denimdress", "shirt-n_room22019bratoppink", "shirt-n_room12019sweaterwithbuttondowngrey", "shirt-n_room12019cropsweaterwhite", "shirt-n_room12019cropsweaterblack", "shirt-n_room12019buttondownblack", "shirt-n_philippineday2019filipinotop", "shirt-n_flashysuit", "shirt-n_SCSpring2018flowershirt", "shirt-n_2016fallblacklayeredbomber", "shirt-n_2016fallblackkknottedtee", "shirt-f_skullsweaterblack", "shirt-f_plaidtiedshirtred", "shirt-f_marchingband"]
               pant = ["shorts-f_pantyhoseshortsnavy", "pants-n_starteritems2019mensshortswhite", "pants-n_starteritems2019mensshortsblue", "pants-n_starteritems2019mensshortsblack", "pants-n_starteritems2019cuffedshortswhite", "pants-n_starteritems2019cuffedshortsblue", "pants-n_starteritems2019cuffedshortsblack", "pants-n_starteritems2019cuffedjeanswhite", "pants-n_starteritems2019cuffedjeansblue", "pants-n_starteritems2019cuffedjeansblack", "pants-n_room32019rippedpantswhite", "pants-n_room32019rippedpantsblue", "pants-n_room32019longtrackshortscamo", "pants-n_room32019longshortswithsocksgrey", "pants-n_room32019longshortswithsocksblack", "pants-n_room32019highwasittrackshortsblack", "pants-n_room32019baggytrackpantsred", "pants-n_room32019baggytrackpantsgreycamo", "pants-n_room22019undiespink", "pants-n_room22019undiesblack", "pants-n_room22019techpantscamo", "pants-n_room22019shortcutoffsdenim", "pants-n_room22019longcutoffsdenim", "pants-n_room12019rippedpantsblue", "pants-n_room12019rippedpantsblack", "pants-n_room12019formalslackskhaki", "pants-n_room12019formalslacksblack", "pants-n_room12019blackacidwashjeans", "pants-n_2016fallgreyacidwashjeans"]
               item_top = random.choice(shirt)
               item_bottom = random.choice(pant)
               xox = await self.highrise.set_outfit(outfit=[
                Item(type='clothing', amount=1, id= item_top, account_bound=False, active_palette=-1), 
                Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=65),     
                      Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                      Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                 Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                      Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),    
                Item(type='clothing', amount=1, id='freckl-n_sharpfaceshadow', account_bound=False, active_palette=-1),
                 Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                      Item(type='clothing', amount=1, id='mouth-basic2018fullpeaked', account_bound=False, active_palette=3),
                      Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderpony', account_bound=False, active_palette=1),
                      Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderpony', account_bound=False, active_palette=1),
                      Item(type='clothing', amount=1, id='eye-n_basic2018heavymascera', account_bound=False, active_palette=36),
                      Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows09', account_bound=False, active_palette=-1)
              ])
               await self.highrise.chat(f"{xox}") 

            else:
                return
        except Exception as e:
            print(f"Error : {e}")





async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)
