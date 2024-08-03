import random
import time
import requests
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
from emotes import Dance_Floor
import asyncio
from random import choice
import os
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata,  GetMessagesRequest, User ,Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
from highrise.__main__ import *
import asyncio, random
from emotes import Emotes
from emotes import Dance_Floor

class BotDefinition:
    
      
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token
        self.following_username = None

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
        self.load_membership()
        self.load_moderators()
        self.load_temporary_vips()
        self.following_username = None
        self.maze_players = {}
        self.user_points = {}  # Dictionary to store user points
        self.Emotes = Emotes
        self.should_stop = False
        self.announce_task = None
        #conversation id var
        self.convo_id_registry = []
        #dance floor position
        min_x = 1.5
        max_x = 6.5
        min_y = 8
        max_y = 9
        min_z = 11.5
        max_z = 26.5

        self.dance_floor_pos = [(min_x, max_x, min_y, max_y, min_z, max_z)]

        #dancer variable
        self.dancer = []

        #dance floor emotes var
        self.emotesdf = Dance_Floor
        #conversation id var
        self.convo_id_registry = []

      
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
        default_moderators = ['alionardo_']
        for mod in default_moderators:
            if mod.lower() not in self.moderators:
                self.moderators.append(mod.lower())
       
    def load_membership(self):
     try:
        with open("membership.json", "r") as file:
            self.membership = json.load(file)
     except FileNotFoundError:
        self.membership = []
    def save_membership(self):
     with open("membership.json", "w") as file:
        json.dump(self.membership, file)

  
    def save_moderators(self):

      with open("moderators.json", "w") as file:
            json.dump(self.moderators, file)

    async def dance_floor(self):

        while True:

            try:
                if self.dance_floor_pos and self.dancer:
                    ran = random.randint(1, 73)
                    emote_text, emote_time = await self.get_emote_df(ran)
                    emote_time -= 1

                    tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user_id)) for user_id in self.dancer]

                    await asyncio.wait(tasks)

                    await asyncio.sleep(emote_time)

                await asyncio.sleep(1)

            except Exception as e:
                print(f"{e}")
    async def get_emote_df(self, target) -> None:

        try:
            emote_info = self.emotesdf.get(target)
            return emote_info      
        except ValueError:
            pass

    async def spam(self):
     while True:
            await self.highrise.chat("Welcome to FIND A DATE")
            await asyncio.sleep(20)
    async def on_start(self, session_metadata: SessionMetadata) -> None:
      try:
         asyncio.create_task(self.dance_floor())
         Counter.bot_id = session_metadata.user_id
         print("Ali is booting ...")
         asyncio.creat_task(self.spam())
         self.highrise.tg.create_task(self.highrise.walk_to(Position(7,0,7, facing='FrontRight')))
         await asyncio.sleep(10)
         await self.highrise.chat(f"Deployed")
         if Counter.bot_id not in self.dancer:
           self.dancer.append(Counter.bot_id)
         
      except Exception as e:
          print(f"An exception occured: {e}")  
    async def on_emote(self, user: User ,emote_id : str , receiver: User | None )-> None:
      print (f"{user.username} , {emote_id}")
    async def on_user_leave(self, user: User) -> None:
        if user.id in self.dancer:
                self.dancer.remove(user.id)
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:

      try:
                 await self.highrise.send_emote('emote-salute')
   
          
      except Exception as e:
            print(f"An error on user_on_join: {e}")
    
   
  
    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions) 
 


   
          
  
    

   




    
