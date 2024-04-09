import random
import time
from highrise import BaseBot, Position, User, AnchorPosition, GetMessagesRequest
import asyncio, random
from highrise.__main__ import *
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re

from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from highrise import BaseBot, Position
from highrise import __main__
from highrise.models import Item
from asyncio import run as arun
from highrise.models import AnchorPosition
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import BaseBot
from collections import UserDict
from highrise.models import SessionMetadata, User
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
import random
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task
from typing import Union
import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *

import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (
    AnchorPosition,
    Item,
    Position,
    SessionMetadata,
    User,
)
from highrise.models import (
    CurrencyItem,
    GetMessagesRequest,
    Item,
    SessionMetadata,
)
import random
import requests
import os
import importlib
import asyncio
import contextlib
import logging
from highrise import BaseBot, AnchorPosition, Position, User, TaskGroup

moderators = ['Arv.Moon','TOMY_X']

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
    usernames = ['TOMY_X','Arv.Moon']

class MyBot(BaseBot):

    continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}  
    user_data: Dict[int, Dict[str, Any]] = {}
    EMOTE_DICT = {
      "angry"           : "emoji-angry",
      "bow"             : "emote-bow",
      "casual"          : "idle-dance-casual",
      "charging"        : "emote-charging",
      "confusion"       : "emote-confused",
      "cursing"         : "emoji-cursing",
      "curtsy"          : "emote-curtsy",
      "cutey"           : "emote-cutey",
      "dont"            : "dance-tiktok2",
      "emotecute"       : "emote-cute",
      "energyball"      : "emote-energyball",
      "enthused"        : "idle-enthusiastic",
      "fashionista"     : "emote-fashionista",
      "flex"            : "emoji-flex",
      "flirtywave"      : "emote-lust",
      "float"           : "emote-float",
      "frog"            : "emote-frog",
      "gravedance"      : "dance-weird",
      "gravity"         : "emote-gravity",
      "greedy"          : "emote-greedy",
      "hello"           : "emote-hello",
      "hot"             : "emote-hot",
      "icecream"        : "dance-icecream",
      "kiss"            : "emote-kiss",
      "kpop"            : "dance-blackpink",
      "lambi"           : "emote-superpose",
      "laugh"           : "emote-laughing",
      "letsgo"          : "dance-shoppingcart",
      "maniac"          : "emote-maniac",
      "model"           : "emote-model",
      "no"              : "emote-no",
      "ogdance"         : "dance-macarena",
      "pennydance"      : "dance-pennywise",      
      "pose1"           : "emote-pose1",
      "pose2"           : "emote-pose3",
      "pose3"           : "emote-pose5",
      "pose4"           : "emote-pose7",
      "pose5"           : "emote-pose8",
      "punkguitar"      : "emote-punkguitar",
      "raisetheroof"    : "emoji-celebrate",
      "russian"         : "dance-russian",
      "sad"             : "emote-sad",
      "savage"          : "dance-tiktok8",
      "shuffle"         : "dance-tiktok10",
      "shy"             : "emote-shy",
      "singalong"       : "idle_singing",
      "sit"             : "idle-loop-sitfloor",
      "snowangel"       : "emote-snowangel",
      "snowball"        : "emote-snowball",
      "swordfight"      : "emote-swordfight",
      "telekinesis"     : "emote-telekinesis",
      "teleport"        : "emote-teleporting",
      "thumbsup"        : "emoji-thumbsup",
      "tired"           : "emote-tired",
      "tummyache"       : "emoji-gagging",
      "viral"           : "dance-tiktok9",
      "wave"            : "emote-wave",
      "weird"           : "dance-weird",
      "worm"            : "emote-snake",
      "wrong"           : "dance-wrong",
      "yes"             : "emote-yes",
      "zombierun"       : "emote-zombierun",
      "ANGRY"           : "emoji-angry",
      "BOW"             : "emote-bow",
      "CASUAL"          : "idle-dance-casual",
      "CHARGING"        : "emote-charging",
      "CONFUSION"       : "emote-confused",
      "CURSING"         : "emoji-cursing",
      "CURTSY"          : "emote-curtsy",
      "CUTEY"           : "emote-cutey",
      "DONT"            : "dance-tiktok2",
      "EMOTECUTE"       : "emote-cute",
      "ENERGYBALL"      : "emote-energyball",
      "ENTHUSED"        : "idle-enthusiastic",
      "FASHIONISTA"     : "emote-fashionista",
      "FLEX"            : "emoji-flex",
      "FLIRTYWAVE"      : "emote-lust",
      "FLOAT"           : "emote-float",
      "FROG"            : "emote-frog",
      "GRAVEDANCE"      : "dance-weird",
      "GRAVITY"         : "emote-gravity",
      "GREEDY"          : "emote-greedy",
      "HELLO"           : "emote-hello",
      "HOT"             : "emote-hot",
      "ICECREAM"        : "dance-icecream",
      "KISS"            : "emote-kiss",
      "KPOP"            : "dance-blackpink",
      "LAMBI"           : "emote-superpose",
      "LAUGH"           : "emote-laughing",
      "LETSGO"          : "dance-shoppingcart",
      "MANIAC"          : "emote-maniac",
      "MODEL"           : "emote-model",
      "NO"              : "emote-no",
      "OGDANCE"         : "dance-macarena",
      "PENNYDANCE"      : "dance-pennywise",
      "POSE1"           : "emote-pose1",
      "POSE2"           : "emote-pose3",
      "POSE3"           : "emote-pose5",
      "POSE4"           : "emote-pose7",
      "POSE5"           : "emote-pose8",
      "PUNKGUITAR"      : "emote-punkguitar",
      "RAISETHEROOF"    : "emoji-celebrate",
      "RUSSIAN"         : "dance-russian",
      "SAD"             : "emote-sad",
      "SAVAGE"          : "dance-tiktok8",
      "SHUFFLE"         : "dance-tiktok10",
      "SHY"             : "emote-shy",
      "SINGALONG"       : "idle_singing",
      "SIT"             : "idle-loop-sitfloor",
      "SNOWANGEL"       : "emote-snowangel",
      "SNOWBALL"        : "emote-snowball",
      "SWORDFIGHT"      : "emote-swordfight",
      "TELEKINESIS"     : "emote-telekinesis",
      "TELEPORT"        : "emote-teleporting",
      "THUMBSUP"        : "emoji-thumbsup",
      "TIRED"           : "emote-tired",
      "TUMMYACHE"       : "emoji-gagging",
      "VIRAL"           : "dance-tiktok9",
      "WAVE"            : "emote-wave",
      "WEIRD"           : "dance-weird",
      "WORM"            : "emote -snake",
      "WRONG"           : "dance-wrong",
      "YES"             : "emote-yes",
      "ZOMBIERUN"       : "emote-zombierun",  
      "Angry"           : "emoji-angry",
      "Bow"             : "emote-bow",
      "Casual"          : "idle-dance-casual",
      "Charging"        : "emote-charging",
      "Confusion"       : "emote-confused",
      "Cursing"         : "emoji-cursing",
      "Curtsy"          : "emote-curtsy",
      "Cutey"           : "emote-cutey",
      "Dont"            : "dance-tiktok2",
      "Emotecute"       : "emote-cute",
      "Energyball"      : "emote-energyball",
      "Enthused"        : "idle-enthusiastic",
      "Fashionista"     : "emote-fashionista",
      "Flex"            : "emoji-flex",
      "Flirtywave"      : "emote-lust",
      "Float"           : "emote-float",
      "Frog"            : "emote-frog",
      "Gravedance"      : "dance-weird",
      "Gravity"         : "emote-gravity",
      "Greedy"          : "emote-greedy",
      "Hello"           : "emote-hello",
      "Hot"             : "emote-hot",
      "Icecream"        : "dance-icecream",
      "Kiss"            : "emote-kiss",
      "Kpop"            : "dance-blackpink",
      "Lambi"           : "emote-superpose",
      "Laugh"           : "emote-laughing",
      "Letsgo"          : "dance-shoppingcart",
      "Maniac"          : "emote-maniac",
      "Model"           : "emote-model",
      "No"              : "emote-no",
      "Ogdance"         : "dance-macarena",
      "Pennydance"      : "dance-pennywise",
      "Pose1"           : "emote-pose1",
      "Pose2"           : "emote-pose3",
      "Pose3"           : "emote-pose5",
      "Pose4"           : "emote-pose7",
      "Pose5"           : "emote-pose8",
      "Punkguitar"      : "emote-punkguitar",
      "celebrate"       : "emoji-celebrate",
      "Russian"         : "dance-russian",
      "Sad"             : "emote-sad",
      "Savage"          : "dance-tiktok8",
      "Shuffle"         : "dance-tiktok10",
      "Shy"             : "emote-shy",
      "Singalong"       : "idle_singing",
      "Sit"             : "idle-loop-sitfloor",
      "Snowangel"       : "emote-snowangel",
      "Snowball"        : "emote-snowball",
      "Swordfight"      : "emote-swordfight",
      "Telekinesis"     : "emote-telekinesis",
      "Teleport"        : "emote-teleporting",
      "Thumbsup"        : "emoji-thumbsup",
      "Tired"           : "emote-tired",
      "Tummyache"       : "emoji-gagging",
      "wing"            : "emote-wings",
      "Viral"           : "dance-tiktok9",
      "Wave"            : "emote-wave",
      "Weird"           : "dance-weird",
      "Worm"            : "emote-snake",
      "Wrong"           : "dance-wrong",
      "Yes"             : "emote-yes",
      "Zombierun"       : "emote-zombierun",
      "sayso"           : "idle-dance-tiktok4",
      "Sayso"           : "idle-dance-tiktok4",
      "SAYSO"           : "idle-dance-tiktok4",
      "uwu"             : "idle-uwu",
      "UWU"             : "idle-uwu",
      "bash"            : "emote-shy2",
      "Zero"            : "emote-astronaut",
      "zero"            : "emote-astronaut",
      "bashfull"            : "emote-shy2",
      "Bashfull"         : "emote-shy2",
      "anime"            : "dance-anime",
      "Anime"            : "dance-anime",
      "airguitar"        : "idle-guitar",
      "Airguitar"        : "idle-guitar",
      "revelations"      : "emote-headblowup",
      "revelation"      : "emote-headblowup",
      "Revelations"      : "emote-headblowup",
      "creepy"           : "dance-creepypuppet",
      "Creepy"           : "dance-creepypuppet",
      "creepycute"       : "emote-creepycute",
      "Creepycute"       : "emote-creepycute",
      "penguin" : "dance-pinguin",
      "Penguin" : "dance-pinguin",
      "sleigh" : "emote-sleigh",
      "Sleigh" : "emote-sleigh",
      "hyped" : "emote-hyped",
      "Hyped" : "emote-hyped",
      "jingle" : "dance-jinglebell", 
      "Jingle" : "dance-jinglebell", 
      "nervous" : "idle-nervous",
      "Nervous" : "idle-nervous",
      "gottago" : "idle-toilet",
      "Gottago" : "idle-toilet",
      "Timejump" : "emote-timejump",
      "timejump" : "emote-timejump",
      "repose" : "sit-relaxed",
      "Repose" : "sit-relaxed",
      "kawaii" : "dance-kawai" , 
      "Kawaii" : "dance-kawai" , 
      "scritchy" : "idle-wild" ,
      "Scritchy" : "idle-wild" ,
      "skating" : "emote-iceskating",
      "Skating " : "emote-iceskating",
      "touch" : "dance-touch",
      "Touch" : "dance-touch"
    }
    continuous_emote_task = None

   # Define your available items list

    def __init__(self):
      super().__init__()
      self.load_moderators()
      self.load_temporary_vips()
      self.maze_players = {}
      self.user_points = {}  # Dictionary to store user points




    def load_temporary_vips(self):
      try:
          with open("temporary.json", "r") as file:
              self.temporary_vips = json.load(file)
      except FileNotFoundError:
          self.temporary_vips = {}

    def save_temporary_vips(self):
      with open("temporary.json", "w") as file:
          json.dump(self.temporary_vips, file)

    def load_moderators(self):
      try:
          with open("moderators.json", "r") as file:
              self.moderators = json.load(file)
      except FileNotFoundError:
          self.moderators = []

      # Add default moderators here
      default_moderators =['TOMY_X','Arv.Moon']
      for mod in default_moderators:
          if mod.lower() not in self.moderators:
              self.moderators.append(mod.lower())

    def save_moderators(self):
      with open("moderators.json", "w") as file:
          json.dump(self.moderators, file)















    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
      response = await self.highrise.get_messages(conversation_id)
      message = "" 

      response = await self.highrise.get_messages(conversation_id)
      if isinstance(response, GetMessagesRequest.GetMessagesResponse):
          message = response.messages[0].content
      print (message)
      if message == "You got a tip!":
          await self.highrise.send_message(conversation_id, "tysm for tip i wish you enjoy in this party")

      if isinstance(response, GetMessagesRequest.GetMessagesResponse):
          if response.messages:
              message = response.messages[0].content
              print(f"Received message: {message}")

      if message:
          print("Condition met: message is not empty")

          if message.lower() == "hello":
            print("Message is 'Hello', responding with commands...")

            response = [
      "HI! 🤗",
      "Thankyou for messaging 💓",
      "Type !help for more info..."
    ]

            for command in response:
                  print(f"Sent command: {command}")
                  await self.highrise.send_message(conversation_id, command)





          elif message.lower() == "emotelist":
              print("Message is 'emotelist', responding with emotelist...")

              emotelist = "Here is the emotelist...\n" \
                      "angry, bow, casual, raisetheroof, charging, confusion, cursing, curtsy, cutey, dont, " \
                      "emotecute, energyball, enthused, fashionista, flex, flirtywave, float, frog, gravedance, " \
                      "gravity, greedy, hello, hot, icecream, kiss, kpop, lambi, laugh, letsgo, maniac, model, no, " \
                      "ogdance, pennydance, pose1, pose2, pose3, pose4, pose5, punkguitar, russian, sad, savage, " \
                      "shuffle, shy, singalong, sit, snowangel, snowball, swordfight, telekinesis, teleport, " \
                      "thumbsup, tired, tummyache, viral, wave, weird, worm, yes, zombierun, airguitar, revelations, " \
                      "creepy, creepycute, penguin, sleigh, hyped, jingle, nervous, gottago, repose, kawaii, scritchy, " \
                      "skating "
              await self.highrise.send_message(conversation_id, emotelist)

          elif message.lower() == "!help":
              print("Message is '!help', responding...")

              commands = [
              "Here is the list of commands...",
              "list",
              "Emotelist"
              ]


              for command in commands:
                  await self.highrise.send_message(conversation_id, command)

    async def on_user_move(self, user: User, pos: Position) -> None:

         if user.username == "TOMY_X":
           print(pos)





    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
      try:
        if receiver.username == "MANNAT_WATCHMEN" and tip.amount >= 1:
          await self.highrise.teleport(sender.id, Position(1, 0, 1, "FrontRight"))
      except Exception as e:
        print(f"An exception occurred: {e}")

      if tip.amount <= 10:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Boooooooooo!!!!!! {sender.username} ")
          tip_message = f" tysm for tip  ,{sender.username}"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount <= 100:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Cheapskate!!!{sender.username} ")
          tip_message=f" tysm for 100 g {sender.username}"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount <= 500:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Good Grief!!!{sender.username} ")
          tip_message = f" tysm for 500g ,{sender.username}"
          await self.highrise.chat(f"{tip_message}") 

      elif tip.amount <= 1000:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Dayummmmmmm{sender.username} ")
          tip_message = f"tysm for 1000   ,{sender.username}"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount <= 5000:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g -  {sender.username} ")
          tip_message = f" tysm for 5000,{sender.username}"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount >=10000:
        print(f"[TIP ] {sender.username} tipped {tip.amount} - ohhhhhhhhhhh")
        tip_message = [f"\n {sender.username} tipped {tip.amount} - ohhhhhhhhhh",

        ]
        random_word = random.choice(tip_message)
        await self.highrise.chat(f"{random_word}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
      print(f"{user.username} emoted: {emote_id}")

    async def on_whisper(self, user: User, message: str) -> None:
     print(f"{user.username} whispered: {message}")
     if "$_top" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(9, 20, 5))
        except Exception as e:
            print("error 3:", e)
     elif "$_middle" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(5, 15, 2))
        except Exception as e:
            print("error 3:", e)
     elif "$_bottom" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(1, 0, 10))
        except Exception as e:
            print("error 3:", e)
     elif "$_up" in message.lower():
        try: 
            await self.highrise.teleport(f"{user.id}", Position(15, 17 ,30))
        except Exception as e:
            print("error 3:", e)
     elif "$_out" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(15, 0, 23.5))
        except Exception as e:
            print("error 3:", e)
     elif "$_door" in message.lower():
        try: 
            await self.highrise.teleport(f"{user.id}", Position(18, 0 ,8))
        except Exception as e:
            print("error 3:", e)
     elif "$_get" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(-5, 0, 3))
        except Exception as e:
            print("error 3:", e)
     elif "$_end" in message.lower():
        try: 
            await self.highrise.teleport(f"{user.id}", Position(-5, 0 ,18.5))
        except Exception as e:
            print("error 3:", e)
     elif "$_center" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(10.5, 0, 10.5))
        except Exception as e:
            print("error 3:", e)
     elif "$_stair" in message.lower():
        try: 
            await self.highrise.teleport(f"{user.id}", Position(13.5, 9 ,9.5))
        except Exception as e:
            print("error 3:", e)
     elif "$_air" in message.lower():
        try: 
            await self.highrise.teleport(f"{user.id}", Position(3, 9 ,10.5))
        except Exception as e:
            print("error 3:", e)






















    


    async def delayed_message_command(self, message, command):
        # Implementation of delayed_message_command goes here
        pass













   












    async def teleport_user_next_to(self, target_username: str, requester_user: User):
        room_users = await self.highrise.get_room_users()
        requester_position = None

        for user, position in room_users.content:
          if user.id == requester_user.id:
              requester_position = position
              break
        for user, position in room_users.content:
          if user.username.lower() == target_username.lower(): 
            z = requester_position.z 
            new_z = z + 1 

            user_dict = {
              "id": user.id,
              "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
            }
            await self.highrise.teleport(user_dict["id"], user_dict["position"])





    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}:{message}")
        if message in self.EMOTE_DICT:
            emote_id = self.EMOTE_DICT[message]
            await self.highrise.send_emote(emote_id, user.id)
        if message.startswith("Loop"):
            emote_name = message[5:].strip()

            if emote_name in self.EMOTE_DICT:
                emote_id = self.EMOTE_DICT[emote_name]
                delay = 3
                if " " in emote_name:
                    emote_name, delay_str = emote_name.split(" ")
                    if delay_str.isdigit():
                        delay = float(delay_str)

                if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                    await self.stop_continuous_emote(user.id)

                task = asyncio.create_task(self.send_continuous_emote(emote_id, user.id,delay))
                self.continuous_emote_tasks[user.id] = task

        if message.lower().startswith("/getitem"):
          outfit_response = await self.highrise.get_my_outfit()
          fifth_item = outfit_response.outfit[4].id
          item_response = await self.webapi.get_item(item_id=fifth_item)
          print (item_response)

        if message.startswith("-heart all"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
               await self.highrise.react("heart", roomUser.id)

#tip 5


        



        if message.startswith("!kick"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !kick @username")
                  return

              mention = parts[1]
              username_to_kick = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_kick.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_kick.lower())
                  user_id_to_kick = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_kick, "kick")
                  await self.highrise.chat( f"Kicked {mention}.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!mute"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !mute @username")
                  return

              mention = parts[1]
              username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_mute.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                  user_id_to_mute = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_mute, "mute",3600)  # Mute for 1 hour
                  await self.highrise.chat(f"Muted {mention} for 1 hour.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!unmute"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !mute @username")
                  return

              mention = parts[1]
              username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_mute.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                  user_id_to_mute = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_mute, "mute",1)  # Mute for 1 hour
                  await self.highrise.chat(f"{mention} Unmuted.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!ban"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !ban @username")
                  return

              mention = parts[1]
              username_to_ban = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_ban.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_ban.lower())
                  user_id_to_ban = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_ban, "ban", 3600)  # Ban for 1 hour
                  await self.highrise.chat(f"Banned {mention} for 1 hour.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")




        if message.startswith("!time"):
          parts = message.split()
          if len(parts) == 2:
              target_mention = parts[1]

              # Remove the "@" symbol if present
              target_user = target_mention.lstrip('@')

              # Check if the target user has temporary VIP status
              remaining_time = self.remaining_time(target_user.lower())
              await self.highrise.send_whisper(user.id, f"Remaining time for {target_mention}'s temporary VIP status: {remaining_time}")
          else:
              await self.highrise.send_whisper(user.id, "Usage: !time @username")


        if message.startswith("react"):
            await self.highrise.react("wave", user.id)

        if message.lower().startswith("/getoutfit"):
            response = await self.highrise.get_my_outfit()
            for item in response.outfit:
                await self.highrise.chat(item.id)







        
                return




        if message.startswith("!help"):
                help_message = (
                    "Available Commands:\n"
                    "\commands you can use:\n \nemotelist  \n sayso @username\n fight @username\n uwu @username\n Example: fight @tomy_x"


                    # ... (other commands)
                )

                # Chunk the message to avoid exceeding message length limits
                chunk_size = 250
                for i in range(0, len(help_message), chunk_size):
                    chunk = help_message[i : i + chunk_size]
                    await self.highrise.send_whisper(user.id, chunk)

        



        




        if message.lower().startswith("/item "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.chat("Invalid command")
                return
            item_name = ""
            for part in parts[1:]:
                item_name += part + " "
            item_name = item_name[:-1]
            print (item_name)
            try:
                response = await self.webapi.get_items(item_name=item_name)
                print (response)
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")


        if  message.startswith("Wallet"):
            if user.username in moderators :

                  wallet = (await self.highrise.get_wallet()).content
                  await self.highrise.send_whisper(user.id, f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

            else: 
                await  self.highrise.send_whisper(user.id, f"Only Moderators Can View the Wallet")

        if message == "-gg":
          shirt = ["shirt-f_punklace"]
          pant = ["skirt-n_room12019pleatedskirtblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullpeaked', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2018wavypulledback', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018wavyhighpony', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_whitedans', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),


                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),


                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"good {xox}")




        if message.lower().startswith("/getinventory"):
            inventory = await self.highrise.get_inventory()
            print (inventory)


        if message.lower().startswith("/buy "):
            parts = message.split(" ")
            if len(parts) != 2:
                return "Invalid command"
            item_id = parts[1]
            try:
                response = await self.buy_item(item_id)
                return f"Item bought: {response}"
            except Exception as e:
                return f"Error: {e}"

# Example usage
            highrise_instance = Highrise()
            result = await highrise_instance.chat("/buy shirt-n_starteritems2019tankwhite")
            print(result)



        if message.lower().startswith(
        "delayed_message") and user.username in self.allowed_usernames:
                 await self.delayed_message_command(Message)

        elif message.lower(
    ) == "stop_delayed_message" and user.username in self.allowed_usernames:
                 await self.stop_delayed_messages()









        elif message.startswith("!stop"):
            if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                await self.stop_continuous_emote(user.id)

                await self.highrise.chat("Continuous emote has been stopped.")
            else:
                await self.highrise.chat("You don't have an active loop_emote.")


        elif message.startswith("/come")and user.username in self.allowed_usernames:
                response = await self.highrise.get_room_users()
                your_pos = None
                for content in response.content:
                    if content[0].id == user.id:
                        if isinstance(content[1], Position):
                            your_pos = content[1]
                            break
                if not your_pos:
                    await self.highrise.send_whisper(user.id, "Invalid coordinates!")
                    return
                await self.highrise.chat(f"@{user.username} I'm coming ..")
                await self.highrise.walk_to(your_pos)

        elif message.startswith("❤"):
            await self.highrise.react("heart", user.id)

        

        elif message.lower().startswith("users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")

        elif message.lower().startswith("outfit"):  
            print(await self.highrise.get_user_outfit(user.id))

        if "List" in message or "list" in message:
            await self.highrise.send_whisper(user.id, "\nEmotes -> Loop emotename, \nEmote list -> Emotelist, \nLove percentage -> Lovepercentage, \nHate percentage -> Hatepercentage, \nIQ -> Iq")
            await self.highrise.send_whisper(user.id, "\nRoast -> Roastme, \nRizz - Rizz, \nPoeticrizz -> Poeticrizz, \nJokes -> Joke, \nFun facts -> Funfact, \nCHECK MESSAGE REQUEST TO RE-READ TY ")

        if "Emotelist" in message or "emotes" in message or "Emotes" in message or "emotelist" in message:
            await self.highrise.send_whisper(user.id,
"\nangry,\nbow,\ncasual,\nraisetheroof,\ncharging,\nconfusion,\ncursing,\ncurtsy,\ncutey,\ndont,\nemotecute,\nenergyball,\nenthused,\nflex,\nflirtywave,\nfloat,\nfrog,\ngreedy,\nhello,\nhot,\nkiss,\nkpop,\nlambi,\nlaugh,\nletsgo,\nmaniac,\nmodel,\nno,\nogdance,")
            await self.highrise.send_whisper(user.id,"\npennydance,\npose1,\npose2,\npose3,\npose4,\npose5,\nrussian,\nsad,\nsavage,\nshuffle,\nshy,\nsingalong,\nsit,\nsnowangel,\nsnowball,\nswordfight,\ntelekinesis,\nteleport,\nthumbsup,\ntired,\ntummyache,\nviral,\nwave,\nweird,\nworm,\nyes")
            await self.highrise.send_whisper(user.id,"\nfashionista,\ngravedance,\ngravity,\nicecream,\npunkguitar,\nsayso,\nuwu,\nzombierun,\nPenguin,\nCreepycute,\nCreepy,\nAirguitar,\nanime")
            await self.highrise.send_whisper(user.id,"\nNEW EMOTES💓\nsleigh,\nhyped, \njingle, \nnervous, \ngottago, \ntimeJump ,\nrepose, \nkawaii, \nscritchy,\nskating, \ntouch \n-\n MORE COMING SOON") 








        

        if "Rizz" in message:
            pickuplines = random.choice(["Do you believe in love at first sight, or should I walk by again?","Is your name Google? Because you have everything I've been searching for.","Are you a magician? Whenever I look at you, everyone else disappears.","Do you have a map? I keep getting lost in your eyes.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","I must be a snowflake because I've fallen for you.","Excuse me, but I think you dropped something: my jaw.","Do you have a Band-Aid? Because I just scraped my knee falling for you.","Is your dad a boxer? Because you're a knockout!","Do you have a map? I keep getting lost in your eyes.","Is your name Google? Because you've got everything I've been searching for.","Do you have a name, or can I call you mine?","Are you a magician? Whenever I look at you, everyone else disappears.","Is your name Wi-Fi? Because I'm feeling a connection.","Do you have a sunburn, or are you always this hot?","Excuse me, but I think you dropped something: my jaw.","Is your dad a boxer? Because you're a knockout!","If you were a vegetable, you'd be a cute-cumber.","I must be a snowflake because I've fallen for you.","Is your name Google? Because you've got everything I've been searching for.","Do you have a map? Because I keep getting lost in your eyes.","Are you a magician? Every time I look at you, everyone else disappears.","Do you believe in love at first sight, or should I walk by again?","Excuse me, but I think you dropped something: my jaw.","Is your name Wi-Fi? Because I'm feeling a connection.","If you were a vegetable, you'd be a cute-cumber.","Can I follow you home? Cause my parents always told me to follow my dreams.","Is your dad a boxer? Because you're a knockout!","Do you have a name, or can I call you mine?", "I hope you know CPR, because you just took my breath away!","So, aside from taking my breath away, what do you do for a living?" , " I ought to complain to Spotify for you not being named this week’s hottest single." , "Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.","Is your name Google? Because you've got everything I've been searching for.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you believe in love at first sight, or should I walk by again?","If you were a vegetable, you'd be a cute-cumber.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because every time I look at you, everyone else disappears.","Excuse me, but I think you dropped something: my jaw.","If you were a triangle, you'd be acute one.","Can I take you out for coffee, or do you prefer to brew it yourself?","Are you made of copper and tellurium? Because you're Cu-Te.","Are you a camera? Because every time I look at you, I smile.","Do you have a name, or can I call you mine?","Do you have a map? Because I keep getting lost in your eyes.","I must be a snowflake because I've fallen for you.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a Wi-Fi signal? Because I'm feeling a connection.","Do you believe in fate? Because I think we were meant to meet.","Are you a time traveler? Because I can see you in my future.","Do you have a name, or can I call you mine?","Can I borrow a kiss? I promise I'll give it back.","I must be a snowflake because I've fallen for you.","If you were a vegetable, you'd be a cute-cumber.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because whenever I look at you, everyone else disappears.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you have a name, or can I call you mine?","Are you an interior decorator? When I saw you, the entire room became beautiful.","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because whenever I look at you, everyone else disappears.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you have a name, or can I call you mine?","Are you an interior decorator? When I saw you, the entire room became beautiful.","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","If you hate me don't read this...Ok done it means you love me and I love you too congratulations we are in relationship...","i may not be a dentist but...I'll surely take care of that smile of yours","I don't have many pick up lines because I'm not trynna pick you up but pin you down","i love people with humor but i love hu-mor (humor rizz)","Are you a piano? Because I wanna use my fingers to play with you until you make beautiful noise!!!!!!!","Texting isn't enough I need you sitting on My lap facing me","Are you other peoples opinion? Cause I can't stop thinking about you (Social anxiety rizz)","Are u lamp of Aladin bcoz i wanna rub u down there and get all my wishes complete","Im glad you dad didn't pull out you're kinda Cool","The word of the day is 'LEGS' So why don't you come over and we can spread the word","I just wish I had more money instead of this massive cock.","Do yk the difference between history and you? History is the past & you are my future (History Rizz)","Are u the clock at school? Because I be lookin at u all day. (School clock rizz)","Are you a painting? Because i'd like to pin you against my wall (artist rizz)","Are you a box of chocolates? Cause I want to take your top off and eat you all night.","Math is incorrect they keep talking about x and y instead of u and i (algebraic rizz)","Why does everything have to be a relationship, We can't kiss and be friends?","In honor of pride month maz How about you let me She/Them T!ddies","I just say 'night' because if it was goodnight you'd be in my bed","You look kinda ill, you must be suffering from a lack of 'Vitamin ME'","Did you know that sleeping next to the person you like helps you fall asleep faster, reduces depression and makes you live longer so why aren't you here every night?"])
            await self.highrise.chat(f": {user.username} - {pickuplines}")

        if "Joke" in message or "joke" in message:
            joke = random.choice(["Yo mama's so fat, when she goes camping, the bears hide their food.", "Your mama's so fat she falls both sides of the bed" , "I wont tell ya lol", "Your mama's so stupid she studied for COVID test","Your mama so ugly when she goes to the dentist they make her lay face down","Your mama's so stupid she used a ruler to see how long she slept","Your mama's so fat her belt size is the size of the equator","Your mama's so ugly when she falls of the car, the driver gets arrested for littering" , "I told my wife she was drawing her eyebrows too high. She looked surprised.","Why don't scientists trust atoms? Because they make up everything.","What do you call fake spaghetti? An impasta.","Why don't skeletons fight each other? They don't have the guts.","I used to play piano by ear, but now I use my hands.","I'm on a whiskey diet. I've lost three days already.","What do you call a bear with no teeth? A gummy bear.","I told my wife she was drawing her eyebrows too low. She looked surprised.","The early bird might get the worm, but the second mouse gets the cheese.","Parallel lines have so much in common. It's a shame they'll never meet.","Why don't seagulls fly over the bay? Because then they'd be bagels.","How do you organize a space party? You planet.","Did you hear about the kidnapping at the playground? They woke up.","My boss told me to have a good day, so I went home.","Joke? Your whole life","i just found out if two girls are close, their period dates can change to be at the same time, tf kinda bluetooth is that","Remember if there's ever a person you like and are talking to, you should just cut off contact and block them because it's never gonna work","Nah cuz why tf do girls make code names for boys. Like who tf is 'Pineapple'"])
            await self.highrise.chat(f": {user.username} - {joke}")

        





        if message.lower().lstrip().startswith(("fight", "hug", "flirt", "stars", "gravity", "uwu", "zero","fashion", "icecream", "punk", "wrong", "sayso", "zombie", "cutey", "pose1", "pose3", "pose5", "pose7", "pose8", "dance", "shuffle", "viralgroove", "weird", "russian", "curtsy", "snowball", "sweating", "snowangel", "cute", "worm", "lambi", "sing", "frog", "energyball", "maniac", "teleport", "float", "telekinesis", "enthused", "confused", "charging", "shopping", "bow", "savage", "kpop", "model", "dontstartnow", "pennydance", "flex", "gagging", "greedy", "cursing", "kiss", "wing", "bashfull", "anime", "airguitar", "revelation", "penguin", "creepycute", "creepy", "sleigh", "hyped", "jingle", "nervous", "gottago", "timejump", "repose", "kawaii", "scritchy", "skating", "touch" )):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Usage: {parts[0]} <@username>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return

                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return


                if message.lower().lstrip().startswith("fight"):
                        await self.highrise.chat(f"\n🥷 @{user.username} And @{args[0][1:]} are in fight 🤬⚔️🔥")
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)

                elif message.lower().lstrip().startswith("hug"):
                        await self.highrise.chat(f"\n🫂 @{user.username} And @{args[0][1:]} in love ❤️")
                        await self.highrise.send_emote("emote-hug", user.id)
                        await self.highrise.send_emote("emote-hug", user_id)

                elif message.lower().lstrip().startswith("flirt"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} so cool 🤭🫣❤️")
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                elif message.lower().lstrip().startswith("stars"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)


                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} fly in the moon😰😧👨🏻‍🚀")
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("gravity"):
                        await self.highrise.send_emote("emote-gravity", user.id)
                        await self.highrise.send_emote("emote-gravity", user_id)

                elif message.lower().lstrip().startswith("uwu"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} shyyy🤭🫣❤️")
                        await self.highrise.send_emote("idle-uwu", user.id)
                        await self.highrise.send_emote("idle-uwu", user_id)

                elif message.lower().lstrip().startswith("fashion"):
                        await self.highrise.send_emote("emote-fashionista", user.id)
                        await self.highrise.send_emote("emote-fashionista", user_id)

                elif message.lower().lstrip().startswith("icecream"):
                        await self.highrise.send_emote("dance-icecream", user.id)
                        await self.highrise.send_emote("dance-icecream", user_id)

                elif message.lower().lstrip().startswith("punk"):
                        await self.highrise.send_emote("emote-punkguitar", user.id)
                        await self.highrise.send_emote("emote-punkguitar", user_id)

                elif message.lower().lstrip().startswith("wrong"):
                        await self.highrise.send_emote("dance-wrong", user.id)
                        await self.highrise.send_emote("dance-wrong", user_id)

                elif message.lower().lstrip().startswith("sayso"):
                        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
                        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

                elif message.lower().lstrip().startswith("zombie"):
                        await self.highrise.send_emote("emote-zombierun", user.id)
                        await self.highrise.send_emote("emote-zombierun", user_id)

                elif message.lower().lstrip().startswith("cutey"):
                        await self.highrise.send_emote("emote-cutey", user.id)
                        await self.highrise.send_emote("emote-cutey", user_id)

                elif message.lower().lstrip().startswith("pose5"):
                        await self.highrise.send_emote("emote-pose5", user.id)
                        await self.highrise.send_emote("emote-pose5", user_id)

                elif message.lower().lstrip().startswith("pose3"):
                        await self.highrise.send_emote("emote-pose3", user.id)
                        await self.highrise.send_emote("emote-pose3", user_id)

                elif message.lower().lstrip().startswith("pose1"):
                        await self.highrise.send_emote("emote-pose1", user.id)
                        await self.highrise.send_emote("emote-pose1", user_id)

                elif message.lower().lstrip().startswith("pose7"):
                        await self.highrise.send_emote("emote-pose7", user.id)
                        await self.highrise.send_emote("emote-pose7", user_id)

                elif message.lower().lstrip().startswith("pose8"):
                        await self.highrise.send_emote("emote-pose8", user.id)
                        await self.highrise.send_emote("emote-pose8", user_id)

                elif message.lower().lstrip().startswith("dance"):
                        await self.highrise.send_emote("idle-dance-casual", user.id)
                        await self.highrise.send_emote("idle-dance-casual", user_id)

                elif message.lower().lstrip().startswith("shuffle"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                elif message.lower().lstrip().startswith("weird"):
                        await self.highrise.send_emote("emote-weird", user.id)
                        await self.highrise.send_emote("emote-weird", user_id)

                elif message.lower().lstrip().startswith("viralgroove"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                elif message.lower().lstrip().startswith("cute"):
                        await self.highrise.send_emote("emote-cute", user.id)
                        await self.highrise.send_emote("emote-cute", user_id)

                elif message.lower().lstrip().startswith("frog"):
                        await self.highrise.send_emote("emote-frog", user.id)
                        await self.highrise.send_emote("emote-frog", user_id)

                elif message.lower().lstrip().startswith("lambi"):
                        await self.highrise.send_emote("emote-superpose", user.id)
                        await self.highrise.send_emote("emote-superpose", user_id)

                elif message.lower().lstrip().startswith("sing"):
                        await self.highrise.send_emote("idle-singing", user.id)
                        await self.highrise.send_emote("idle-singing", user_id)

                elif message.lower().lstrip().startswith("worm"):
                        await self.highrise.send_emote("emote-snake", user.id)
                        await self.highrise.send_emote("emote-snake", user_id)

                elif message.lower().lstrip().startswith("bow"):
                        await self.highrise.send_emote("emote-bow", user.id)
                        await self.highrise.send_emote("emote-bow", user_id)

                elif message.lower().lstrip().startswith("energyball"):
                        await self.highrise.send_emote("emote-energyball", user.id)
                        await self.highrise.send_emote("emote-energyball", user_id)

                elif message.lower().lstrip().startswith("maniac"):
                        await self.highrise.send_emote("emote-maniac", user.id)
                        await self.highrise.send_emote("emote-maniac", user_id)

                elif message.lower().lstrip().startswith("teleport"):
                        await self.highrise.send_emote("emote-teleporting", user.id)
                        await self.highrise.send_emote("emote-teleporting", user_id)

                elif message.lower().lstrip().startswith("float"):
                        await self.highrise.send_emote("emote-float", user.id)
                        await self.highrise.send_emote("emote-float", user_id)

                elif message.lower().lstrip().startswith("telekinesis"):
                        await self.highrise.send_emote("emote-telekinesis", user.id)
                        await self.highrise.send_emote("emote-telekinesis", user_id)

                elif message.lower().lstrip().startswith("enthused"):
                        await self.highrise.send_emote("idle-enthusiastic", user.id)
                        await self.highrise.send_emote("idle-enthusiastic", user_id)

                elif message.lower().lstrip().startswith("confused"):
                        await self.highrise.send_emote("emote-confused", user.id)
                        await self.highrise.send_emote("emote-confused", user_id)

                elif message.lower().lstrip().startswith("shopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                elif message.lower().lstrip().startswith("charging"):
                        await self.highrise.send_emote("emote-charging", user.id)
                        await self.highrise.send_emote("emote-charging", user_id)

                elif message.lower().lstrip().startswith("snowangel"):
                        await self.highrise.send_emote("emote-snowangel", user.id)
                        await self.highrise.send_emote("emote-snowangel", user_id)

                elif message.lower().lstrip().startswith("sweating"):
                        await self.highrise.send_emote("emote-hot", user.id)
                        await self.highrise.send_emote("emote-hot", user_id)

                elif message.lower().lstrip().startswith("snowball"):
                        await self.highrise.send_emote("emote-snowball", user.id)
                        await self.highrise.send_emote("emote-snowball", user_id)

                elif message.lower().lstrip().startswith("curtsy"):
                        await self.highrise.send_emote("emote-curtsy", user.id)
                        await self.highrise.send_emote("emote-curtsy", user_id)

                elif message.lower().lstrip().startswith("russian"):
                        await self.highrise.send_emote("dance-russian", user.id)
                        await self.highrise.send_emote("dance-russian", user_id)

                elif message.lower().lstrip().startswith("pennywise"):
                        await self.highrise.send_emote("dance-pennywise", user.id)
                        await self.highrise.send_emote("dance-pennywise", user_id)

                elif message.lower().lstrip().startswith("dont"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                elif message.lower().lstrip().startswith("kpop"):
                        await self.highrise.send_emote("dance-blackpink", user.id)
                        await self.highrise.send_emote("dance-blackpink", user_id)

                elif message.lower().lstrip().startswith("model"):
                        await self.highrise.send_emote("emote-model", user.id)
                        await self.highrise.send_emote("emote-model", user_id)

                elif message.lower().lstrip().startswith("savage"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                elif message.lower().lstrip().startswith("flex"):
                        await self.highrise.send_emote("emoji-flex", user.id)
                        await self.highrise.send_emote("emoji-flex", user_id)

                elif message.lower().lstrip().startswith("gagging"):
                        await self.highrise.send_emote("emoji-gagging", user.id)
                        await self.highrise.send_emote("emoji-gagging", user_id)

                elif message.lower().lstrip().startswith("greedy"):
                        await self.highrise.send_emote("emote-greedy", user.id)
                        await self.highrise.send_emote("emote-greedy", user_id)

                elif message.lower().lstrip().startswith("cursing"):
                        await self.highrise.send_emote("emoji-cursing", user.id)
                        await self.highrise.send_emote("emoji-cursing", user_id)

                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("kiss"):
                        await self.highrise.send_emote("emote-kiss", user.id)
                        await self.highrise.send_emote("eote-kiss", user_id)
                elif message.lower().lstrip().startswith("anime"):
                        await self.highrise.send_emote("dance-anime", user.id)
                        await self.highrise.send_emote("dance-anime", user.id)
                elif message.lower().lstrip().startswith("airguitar"):
                        await self.highrise.send_emote("idle-guitar", user.id)
                        await self.highrise.send_emote("idle-guitar", user_id)
                elif message.lower().lstrip().startswith("revelations"):
                        await self.highrise.send_emote("emote-headblowup", user.id)
                        await self.highrise.send_emote("emote-headblowup", user_id)
                elif message.lower().lstrip().startswith("creepy"):
                        await self.highrise.send_emote("dance-creepypuppet", user.id)
                        await self.highrise.send_emote("dance-creepypuppet", user_id)
                elif message.lower().lstrip().startswith("creepycute"):
                        await self.highrise.send_emote("emote-creepycute", user.id)
                        await self.highrise.send_emote("emote-creepycute", user.id)
                elif message.lower().lstrip().startswith("penguin"):
                        await self.highrise.send_emote("dance-pinguin", user.id)
                        await self.highrise.send_emote("dance-pinguin", user.id)
                elif message.lower().lstrip().startswith("sleigh"):
                        await self.highrise.send_emote("emote-sleigh", user.id)
                        await self.highrise.send_emote("emote-sleigh", user.id)
                elif message.lower().lstrip().startswith("hyped"):
                        await self.highrise.send_emote("emote-hyped", user.id)
                        await self.highrise.send_emote("emote-hyped", user.id)
                elif message.lower().lstrip().startswith("jingle"):
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                elif message.lower().lstrip().startswith("nervous"):
                        await self.highrise.send_emote("idle-nervous", user.id)
                        await self.highrise.send_emote("idle-nervous", user.id)
                elif message.lower().lstrip().startswith("toilet"):
                        await self.highrise.send_emote("idle-toilet", user.id)
                        await self.highrise.send_emote("idle-toilet", user.id)
                elif message.lower().lstrip().startswith("timejump"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user.id)
                elif message.lower().lstrip().startswith("skating"):
                        await self.highrise.send_emote("dance-skating", user.id)
                        await self.highrise.send_emote("dance-skating", user.id)
                elif message.lower().lstrip().startswith("repose"):
                        await self.highrise.send_emote("sit-relaxed", user.id)
                        await self.highrise.send_emote("sit-relaxed", user.id)
                elif message.lower().lstrip().startswith("kawaii"):
                        await self.highrise.send_emote("dance-kawai", user.id)
                        await self.highrise.send_emote("dance-kawai", user.id)
                elif message.lower().lstrip().startswith("scritchy"):
                        await self.highrise.send_emote("idle-wild", user.id)
                        await self.highrise.send_emote("idle-wild", user.id)
                elif message.lower().lstrip().startswith("skating"):
                        await self.highrise.send_emote("emote-iceskating", user.id)
                        await self.highrise.send_emote("emote-iceskating", user.id)

                elif message.lower().lstrip().startswith("touch"):
                        await self.highrise.send_emote("dance-touch", user.id)
                        await self.highrise.send_emote("dance-touch", user.id)

        if message.startswith("0"):
          await self.highrise.send_emote("emote-float", user.id)
        if message.startswith("2"):
          await self.highrise.send_emote("dance-tiktok2", user.id)   
        if message.startswith("3"):
          await self.highrise.send_emote("emote-pose1", user.id)
        if message.startswith("4"):
          await self.highrise.send_emote("dance-shoppingcart", user.id)
        if message.startswith("5"):
          await self.highrise.send_emote("dance-russian", user.id)
        if message.startswith("6"):
          await self.highrise.send_emote("idle_singing", user.id)
        if message.startswith("7"):
          await self.highrise.send_emote("idle-enthusiastic", user.id)   
        if message.startswith("8"):
          await self.highrise.send_emote("idle-dance-casual", user.id)   
        if message.startswith("9"):
          await self.highrise.send_emote("idle-loop-sitfloor", user.id)
        if message.startswith("10"):
          await self.highrise.send_emote("emote-lust", user.id)
        if message.startswith("11"):
          await self.highrise.send_emote("emote-greedy", user.id)
        if message.startswith("12"):
          await self.highrise.send_emote("emote-bow", user.id)
        if message.startswith("13"):
          await self.highrise.send_emote("emote-curtsy", user.id)
        if message.startswith("14"):
          await self.highrise.send_emote("emote-snowball", user.id)
        if message.startswith("15"):
          await self.highrise.send_emote("emote-snowangel", user.id)
        if message.startswith("16"):
          await self.highrise.send_emote("emote-confused", user.id)
        if message.startswith("17"):
          await self.highrise.send_emote("emote-teleporting", user.id)
        if message.startswith("18"):
          await self.highrise.send_emote("emote-swordfight", user.id)
        if message.startswith("19"):
          await self.highrise.send_emote("emote-energyball", user.id)
        if message.startswith("20"):
          await self.highrise.send_emote("dance-tiktok8", user.id)
        if message.startswith("21"):
          await self.highrise.send_emote("dance-blackpink", user.id)
        if message.startswith("22"):
          await self.highrise.send_emote("emote-model", user.id)
        if message.startswith("23"):
          await self.highrise.send_emote("dance-pennywise", user.id)
        if message.startswith("24"):
          await self.highrise.send_emote("dance-tiktok10", user.id)
        if message.startswith("25"):
          await self.highrise.send_emote("emote-telekinesis", user.id)
        if message.startswith("26"):
          await self.highrise.send_emote("emote-hot", user.id)
        if message.startswith("27"):
          await self.highrise.send_emote("dance-weird", user.id)
        if message.startswith("28"):
          await self.highrise.send_emote("emote-pose7", user.id)
        if message.startswith("29"):
          await self.highrise.send_emote("emote-pose8", user.id)
        if message.startswith("30"):
          await self.highrise.send_emote("emote-pose3", user.id)
        if message.startswith("31"):
          await self.highrise.send_emote("emote-pose5", user.id)  
        if message.startswith("32"):
          await self.highrise.send_emote("emote-pose5", user.id)  
        if message.startswith("31"):
          await self.highrise.send_emote("emote-pose5", user.id)  
        if message.startswith("31"):
          await self.highrise.send_emote("emote-pose5", user.id)


        if message.startswith("-heart all"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
               await self.highrise.react("heart", roomUser.id)

        if message.startswith("p1"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-float", roomUser.id)

        if message.startswith("p2"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)

        if message.startswith("p3"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)



        if message.startswith("p5"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)

        if message.startswith("p4"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id)



        if message.startswith("p5"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

        if message.startswith("p6"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-flex", roomUser.id)

        if message.startswith("p7"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)


        if message.startswith("p8"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

        if message.startswith("p9"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)

        if message.startswith("p10"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)



        if message.startswith("p11"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)

        if message.startswith("p12"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)

        if message.startswith("p13"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)

        if message.startswith("p14"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)

        if message.startswith("p15"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)

        if message.startswith("p16"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

        if message.startswith("p17"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

        if message.startswith("p18"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)

        if message.startswith("p19"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

        if message.startswith("p20"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

        if message.startswith("p21"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)

        if message.startswith("p22"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)





        if message.startswith("p23"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)

        if message.startswith("p24"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-swordfight", roomUser.id)

        if message.startswith("p25"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

        if message.startswith("p26"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

        if message.startswith("p27"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

        if message.startswith("p28"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gravity", roomUser.id)



        if message.startswith("p29"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)

        if message.startswith("p30"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-frog", roomUser.id)

        if message.startswith("p31"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)

        if message.startswith("p32"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)

        if message.startswith("p33"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)

        if message.startswith("p34"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)

        if message.startswith("p35"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hearteyes", roomUser.id)

        if message.startswith("p36"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-exasperatedb", roomUser.id)

        if message.startswith("p37"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)

        if message.startswith("p38"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)

        if message.startswith("p39"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)


        if "Charging" in message:
          try:
            emote_id = "emote-charging"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Sing" in message:
          try:
            emote_id = "idle_singing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Wise" in message:
          try:
            emote_id = "dance-pennywise"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Tiktok2" in message:
          try:
            emote_id = "dance-tiktok2"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Virgalrove" in message:
          try:
            emote_id = "dance-tiktok9"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Weird" in message:
          try:
            emote_id = "dance-weird"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Telekinesis" in message:
          try:
            emote_id = "emote-telekinesis"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Tiktok8" in message:
          try:
            emote_id = "dance-tiktok8"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Maniac" in message:
          try:
            emote_id = "emote-maniac"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Zombie" in message:
          try:
            emote_id = "emote-zombierun"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Relaxing" in message:
          try:
            emote_id = "emote-Relaxing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Gravity" in message:
          try:
            emote_id = "emote-gravity"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Fashon" in message:
          try:
            emote_id = "emote-fashionista"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Pose7" in message:
          try:
            emote_id = "emote-pose7"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Pink" in message:
          try:
            emote_id = "dance-blackpink"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Kiss" in message:
          try:
            emote_id = "emote-kiss"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Hello" in message:
          try:
            emote_id = "emote-hello"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Tiktok8" in message:
          try:
            emote_id = "dance-tiktok8"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Weird" in message:
          try:
            emote_id = "dance-weird"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "هاي" in message:
          try:
            emote_id = "emote-kiss"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "شكرا" in message:
          try:
            emote_id = "emote-kiss"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "تو" in message:
          try:
            emote_id = "idle-dance-casual"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")


        if "Model" in message:
          try:
            emote_id = "emote-model"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "no" in message:
          try:
            emote_id = "emote-no"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")



        if "Confused" in message:
          try:
            emote_id = "emote-confused"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "cute" in message:
          try:
            emote_id = "emote-cute"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "Curtsy" in message:
          try:
            emote_id = "emote-curtsy"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Tiktok4 " in message:
          try:
            emote_id = "idle-dance-tiktok4"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Uwu" in message:
          try:
            emote_id = "idle-uwu"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Kpop" in message:
          try:
            emote_id = "dance-blackpink"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Energyball" in message:
          try:
            emote_id = "emote-energyball"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Float" in message:
          try:
            emote_id = "emote-float"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Frog" in message:
          try:
            emote_id = "emote-frog"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Teleport" in message:
          try:
            emote_id = "emote-teleporting"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sword" in message:
          try:
            emote_id = "emote-swordfight"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Casual" in message:
          try:
            emote_id = "idle-dance-casual"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Cutey" in message:
          try:
            emote_id = "idle-dance-cutey"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "You got a tip!" in message:
          try:
            emote_id = "dance-tiktok2"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sing" in message:
          try:
            emote_id = "idle_singing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Greedy" in message:
          try:
            emote_id = "emote-greedy"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sweating" in message:
          try:
            emote_id = "emote-hot"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Pose1" in message:
          try:
            emote_id = "emote-superpose"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Russian dance" in message:
          try:
            emote_id = "dance-russian"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Snake" in message:
          try:
            emote_id = "emote-snake"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Lust" in message:
          try:
            emote_id = "emote-lust"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Wise" in message:
          try:
            emote_id = "dance-pennywise"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Bow" in message:
          try:
            emote_id = "emote-bow"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Gagging" in message:
          try:
            emote_id = "emoji-gagging"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Rest" in message:
          try:
            emote_id = "idle-loop-sitfloor"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Enthused" in message:
          try:
            emote_id = "idle-enthusiastic"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Snow ball" in message:
          try:
            emote_id = "emote-snowball"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Snow angel" in message:
          try:
            emote_id = "emote-snowangel"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Flex" in message:
          try:
            emote_id = "emoji-flex"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Laugh" in message:
          try:
            emote_id = "emote-laughing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Yes" in message:
          try:
            emote_id = "emote-yes"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Guitar" in message:
          try:
            emote_id = "emote-punkguitar"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "ولكم" in message:
          try:
            emote_id = "emote-bow"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Anime" in message:
          try:
            emote_id = "dance-anime"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Penguin" in message:
          try:
            emote_id = "dance-pinguin"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Airguitar " in message:
          try:
            emote_id = "idle-guitar"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Head" in message:
          try:
            emote_id = "emote-headblowup"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Creepy" in message:
          try:
            emote_id = "emote-creepycute"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sad" in message:
          try:
            emote_id = "emote-sad"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Zero" in message:
          try:
            emote_id = "emote-astronaut"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sayso" in message:
          try:
            emote_id = "idle-dance-tiktok4"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "باي" in message:
          try:
            emote_id = "emote-astronaut"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "سيو" in message:
          try:
            emote_id = "emote-shy2"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Shy" in message:
          try:
            emote_id = "emote-shy2"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "Sleigh" in message:
          try:
            emote_id = "emote-sleigh"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Hyped" in message:
          try:
            emote_id = "emote-hyped"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Jingle" in message:
          try:
            emote_id = "dance-jinglebell"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Nervous" in message:
          try:
            emote_id = "idle-nervous"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "Timejump" in message:
          try:
            emote_id = "emote-timejump"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Skating" in message:
          try:
            emote_id = "dance-skating"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Repose" in message:
          try:
            emote_id = "sit-relaxed"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("shgjgkfjfutfgjghfjfhgghfh")          

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("oahsjsbsskxj")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("kshxdskkwnsbzj")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("uwjshssbssmk")             
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("twısjdndxnbznsns")           
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("ısudksnsbd")          

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("wodjdnxnz")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jsıxısmnskd")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("xıpsksndnx")                
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jxospwlsldndnd")    
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("shgjgkfjfutfgjghfjfhgghfh")    

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("oahsjsbsskxj")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("kshxdskkwnsbzj")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("uwjshssbssmk")             
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("twısjdndxnbznsns")           
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("ısudksnsbd")          

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("wodjdnxnz")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jsıxısmnskd")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("xıpsksndnx")                
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jxospwlsldndnd")    
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("shgjgkfjfutfgjghfjfhgghfh")          

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("oahsjsbsskxj")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("kshxdskkwnsbzj")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("uwjshssbssmk")             
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("twısjdndxnbznsns")           
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("ısudksnsbd")          

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("wodjdnxnz")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jsıxısmnskd")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("xıpsksndnx")                
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jxospwlsldndnd")    
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("shgjgkfjfutfgjghfjfhgghfh")    

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("oahsjsbsskxj")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("kshxdskkwnsbzj")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("uwjshssbssmk")             
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("twısjdndxnbznsns")           
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("ısudksnsbd")          

        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("wodjdnxnz")            
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jsıxısmnskd")              
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("xıpsksndnx")                
        if message.lower().lstrip().startswith(("-random", "!random")):
          await self.highrise.chat("jxospwlsldndnd")




        if message.startswith("users"):
                room_users = (await self.highrise.get_room_users()).content
                await self.highrise.chat(f"There are {len(room_users)} users in the room")

        if message == "-boy":
          shirt = ["shirt-n_room22109plaidjacket"]
          pant = ["pants-n_room12019blackacidwashjeans"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  
                  Item(type='clothing', amount=1, id='eye-m_12b', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairlower16', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='shoes-n_converse_black', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='freckle-n_tomsbandage', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='hair_front-m_23', account_bound=False, active_palette=0),

                  Item(type='clothing', amount=1, id='hair_back-m_23', account_bound=False, active_palette=-1),
                 


          ]) 
          await self.highrise.chat(f"good {xox}")

        if message.lower().startswith("/getoutfit"):
                response = await self.highrise.get_my_outfit()
                for item in response.outfit:
                    await self.highrise.chat(item.id)

        if message.startswith("❤️"):
          try:
            # Get the count of heart reactions from the user's message
            count = int(message[2:].strip())
            if count <= 0:
              await self.highrise.chat(
                "Please enter a valid number greater than 0.")
              return

            # Send heart reactions 'count' number of times with a small delay in between
            for _ in range(count):
              await self.highrise.react("heart", user.id)
              await asyncio.sleep(0.1)  # Adjust the delay duration if needed

          except ValueError:
            await self.highrise.chat("Please enter a valid number after ❤️.")

        if message.startswith("👏"):
          try:

            count = int(message[2:].strip())
            if count <= 0:
              await self.highrise.chat(
                "Please enter a valid number greater than 0.")
              return

            for _ in range(count):
              await self.highrise.react("clap", user.id)
              await asyncio.sleep(0.1)

          except ValueError:
            await self.highrise.chat("Please enter a valid number after 👏.")

        if message.startswith("😉"):
          try:

            count = int(message[2:].strip())
            if count <= 0:
              await self.highrise.chat(
                "Please enter a valid number greater than 0.")
              return

            for _ in range(count):
              await self.highrise.react("wink", user.id)
              await asyncio.sleep(0.1)

          except ValueError:
            await self.highrise.chat("Please enter a valid number after 🌚.")

        if message == "-dr":
          shirt = ["shirt-n_room12019buttondownblack"]
          pant = ["pants-n_room12019formalslacksblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018poutfullpeaked', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=5),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=5),
                  Item(type='clothing', amount=1, id='hat-n_room22019fluffballears_1', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='shoes-n_drstompsbootsyellow', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),



          ]) 
          await self.highrise.chat(f"good {xox}")

        if message == "-dress90":
          shirt = ["shirt-n_room32019longlineteesweatshirtgrey"]
          pant = ["pants-n_starteritems2019cuffedjeansblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='nose-n_basic2018newnose04', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018whistlemouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_04', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"{xox}")

        if message == "-dress56":
          shirt = ["shirt-n_starteritems2019femtshirtwhite"]
          pant = ["skirt-n_starteritems2018whiteskirt"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018wavymed', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_basic2018newnose04', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2019wavyflipdroop', account_bound=False, active_palette=39),

                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='blush-n_salonshop2018blush', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2018conversewhite', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018fullround', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"{xox}")


        elif message.startswith("emotesmod"):
                emotes_message = (
                    "Available Emote Commands for mod:\n"
                    "fly , tele , shy , kawaii , punk , jingle , eyes, flex , push , anime , wild ,\n"
                    "timejump , iceskating , touch , repose , hyped , zero , sayso , zombie ,\n"
                    "wrong , viral , flirt , sword , sing , cele , weird , gravity , creepy , frog , gift , boxer ,\n"
                    "fashion, casual , enthu , hot , toilet \n"

                )

                # Chunk the message to avoid exceeding message length limits
                chunk_size = 250
                for i in range(0, len(emotes_message), chunk_size):
                    chunk = emotes_message[i: i + chunk_size]
                    await self.highrise.send_whisper(user.id, chunk)


        if message.startswith("!commands"):
                help_message = (
                    "Available Commands:\n"
                    "!time @username - Check remaining time for temporary VIP status\n"
                    "!kick @username - Kick a user from the room\n"
                    "!mute @username - Mute a user in the room for 1 hour\n"
                    "!unmute @username - Unmute a muted user\n"
                    "!ban @username - Ban a user from the room for 1 hour\n"


                    "Wallet - View the bot's wallet (moderators only)\n"
                    




                    # ... (other commands)
                )

                # Chunk the message to avoid exceeding message length limits
                chunk_size = 250
                for i in range(0, len(help_message), chunk_size):
                    chunk = help_message[i : i + chunk_size]
                    await self.highrise.send_whisper(user.id, chunk)


        if message.startswith("!commands"):
          help_message = (

              "❤️ this reaction make user mod in code permanent (Modrators)\n"
              "😉 this reaction make user mod in code 24h (Modrators)\n"
              "👏  this reaction remove user from  mod in code (Modrators)\n"
              "👏  this reaction remove user from  mod in code (Modrators)\n"
              "👍 This reaction getir any user in any place (moderators)\n"



              # ... (other commands)
          )

          # Chunk the message to avoid exceeding message length limits
          chunk_size = 250
          for i in range(0, len(help_message), chunk_size):
              chunk = help_message[i : i + chunk_size]
              await self.highrise.send_whisper(user.id, chunk)

        if message == "-dresss":
          shirt = ["shirt-n_starteritems2019femtshirtwhite"]
          pant = ["skirt-n_starteritems2018whiteskirt"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018wavymed', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2019wavyflipdroop', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='blush-f_blush01', account_bound=False, active_palette=-1),


                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2018conversewhite', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018fullround', account_bound=False, active_palette=24),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"{xox}")


        if "Deathyear" in message or "deathyear" in message:
            death_year = random.randint(2023, 2100)
            await self.highrise.chat(f" {user.username} IDK when you would die but maybe around: {death_year}")

        if "Iq" in message or "iq" in message:
            iq = random.randint(0, 100)
            if iq <= 10:
               await self.highrise.chat(f" @{user.username} your iq is {iq}% ,Bro you are dumb asf ,lol ")
            elif iq >= 90:
               await self.highrise.chat(f" @{user.username} your iq is {iq}% ,You are clever than most of other dumb in this room")
            elif iq >10 and iq <90:              
               await self.highrise.chat(f"Your ( {user.username} ) iq is : {iq}%")

        if "Lovepercentage" in message or "lovepercentage" in message:
            love_percentage = random.randint(0, 100)
            if love_percentage == 100:
                await self.highrise.chat(f" {user.username} {love_percentage}% Everyone loves ya")
            elif love_percentage == 0:
                await self.highrise.chat(f" {user.username} {love_percentage}% No one loves ya,Go cry in that corner ")
            elif love_percentage <100 or love_percentage >0:
                await self.highrise.chat(f" {user.username} Only {love_percentage}% People loves ya!!")

        if "Hatepercentage" in message or "hatepercentage" in message:
            hate_percentage = random.randint(0, 100)
            if hate_percentage == 0:
                await self.highrise.chat(f" {user.username} {hate_percentage}% No one hates ya")
            elif hate_percentage == 100:
                await self.highrise.chat(f" {user.username} {hate_percentage}% Everyone hates ya,Go cry in that corner ")
            elif hate_percentage < 100 or hate_percentage > 0:
                await self.highrise.chat(f" {user.username} Only {hate_percentage}% people hates ya")

        if "Straightmeter" in message or "straightmeter" in message:
            straight_metre = random.randint(0,100)
            if straight_metre <=10:
                await self.highrise.chat(f"{user.username} {straight_metre}% Why are you Gay?? ")
            elif straight_metre <50:
                await self.highrise.chat(f"{user.username} {straight_metre}%  YOU ARE GAY!!!")
            elif straight_metre ==50:
                await self.highrise.chat(f"{user.username} {straight_metre}%  OMG,YOU ARE Bi!!!")
            elif straight_metre <=90:
                await self.highrise.chat(f"{user.username} {straight_metre}%  You are normal ")
            elif straight_metre >=90  :
                await self.highrise.chat(f"{user.username} {straight_metre}% You are straighter than my programming code ")

    async def stop_continuous_emote(self, user_id: int):
        if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
            task = self.continuous_emote_tasks[user_id]
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task
            del self.continuous_emote_tasks[user_id]



    async def on_start(self, session_metadata: SessionMetadata) -> None:

        Counter.bot_id = session_metadata.user_id
        print("is booting ...")
        pass












        self.highrise.tg.create_task(self.highrise.walk_to(Position(x=13.5, y=7.0, z=1.5, facing='FrontLeft')))
        self.load_temporary_vips()

        while True:
            await asyncio.sleep(5)
            await self.highrise.chat("💰Welcome in the GIVEAWAY 💰\n\n❗️Check post @Arv.Moon if you want to take part in the 10k g draw❗️\n💕Follow @Arv.Moon💕\n🫶🏻Like and comment post and tag Your 3 friends!🫶🏻\n👑100g to jar = x10 lottery tickets👑\n\n💥GOOD LUCK TO EVERYONE💥\n")
            await self.highrise.send_emote(
         random.choice(['dance-anime']))
      
           




    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
     try:





      if user.username == "Arv.Moon" or user.username == "TOMY_X" or user.username in moderators :
        if reaction == "heart":
          await self.highrise.chat(f"{receiver.username} is now a 👑Permanent👑 VIP, given by {user.username}")

          receiver_username = receiver.username.lower()
          if receiver_username not in self.moderators:
                self.moderators.append(receiver_username)
                self.save_moderators()

      if reaction =="thumbs"and user.username in moderators:
         target_username = receiver.username
         if target_username not in moderators:
            await self.teleport_user_next_to(target_username, user)
      if reaction =="thumbs"and user.username in moderators:
         target_username = receiver.username
         if target_username not in ['Arv.Moon','Arv.Moon']:
            await self.teleport_user_next_to(target_username, user)

      if reaction =="thumbs"and user.username in moderators:
         target_username = receiver.username
         if target_username not in ['TOMY_x','TOMY_X']:
            await self.teleport_user_next_to(target_username, user)

      

      if user.username == "Arv.Moon" or user.username == "TOMY_X" :
          if reaction == "wink":
              await self.highrise.chat(f"{receiver.username} is now a 🎩Temporary🎩 VIP, given by {user.username}")

              receiver_username = receiver.username.lower()
              if receiver_username not in self.temporary_vips:
                    self.temporary_vips[receiver_username] = int(time.time()) + 24 * 60 * 60  # VIP for 24 hours
                    self.save_temporary_vips()


      if user.username in ["Arv.Moon", "TOMY_X"] and reaction == "clap":
            await self.highrise.chat(f"{receiver.username} is remove from the commands by {user.username}")

            receiver_username = receiver.username.lower()

            # Remove user from moderators list
            if receiver_username in self.moderators:
                self.moderators.remove(receiver_username)
                self.save_moderators()

            # Add user to temporary VIPs list
            if receiver_username not in self.temporary_vips:
                self.temporary_vips[receiver_username] = int(time.time()) + 24 * 60 * 60  # VIP for 24 hours
                self.save_temporary_vips()

      if user.username.lower() in self.moderators and reaction == "wave":
            await self.highrise.moderate_room(receiver.id, "kick")
            await self.highrise.chat(f"{receiver.username} is Kicked by {user.username}")


     except Exception as e:
            print(f"An exception occured: {e}")



    def remaining_time(self, username):
        if username in self.temporary_vips:
            remaining_seconds = self.temporary_vips[username] - int(time.time())
            if remaining_seconds > 0:
                return str(timedelta(seconds=remaining_seconds))
        return "Not a temporary VIP."

    async def on_user_join(self, user: User, position: Union[Position, AnchorPosition]) -> None:
      privileges = await self.highrise.get_room_privilege(user.id)
      print(f"{user.username} joined the room with the privileges {privileges}")
      await asyncio.sleep(5)
      
      await self.highrise.send_whisper(user.id, f"Heyo @{user.username}! Welcome in the GIVEAWAY!")
      



    async def send_continuous_emote(self, emote_id: str, user_id: int, delay: float):
        try:
            while True:
                await self.highrise.send_emote(emote_id, user_id)
                await asyncio.sleep(delay)
        except ConnectionResetError:
           if message.lower().lstrip().startswith("loop"):
            parts = message.split("6 ")
            if len(parts) < 2:
                await self.highrise.chat("Invalid command format. Usage: loop<emote_name> ")
                return

            emote_name = parts[1]

            if len(parts) >= 3:
                try:
                    float(parts[2])
                except ValueError:
                    await self.highrise.chat("Invalid delay value. The delay must be a valid number in seconds.")
                    return
            else:
                pass  # Default delay of 7.5 seconds




    async def command_handler(self, user: User, message: str):
      pass

async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)

                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)

        # If no matching function is found
        return








async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)
