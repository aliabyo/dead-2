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
moderator = ['babyJmia', 'Alionardo_','MikeyArkham']
co_mod = ['Alionardo_','MikeyArkham','babyJmia']

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

class MyBot(BaseBot):
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
            
            await self.highrise.walk_to(Position(15, 0,9, "FrontRight"))
            await asyncio.sleep(3)
            await self.highrise.chat(" on duty!")
            item = await self.webapi.get_items(item_name="Top Knot") 
            item_id = item.items[0].item_id
            print(item_id)
        except Exception as e:
            print(f"error : {e}")

    async def send_continuous_emote(self, emote_text ,user_id,emote_time):
      try:
          while True:                    
                tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user_id))]
                await asyncio.wait(tasks)
                await asyncio.sleep(emote_time)
                await asyncio.sleep(1)
      except Exception as e:
                print(f"{e}")

  
    async def stop_continuous_emote(self, user_id: int):
      if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
          task = self.continuous_emote_tasks[user_id]
          task.cancel()
          with contextlib.suppress(asyncio.CancelledError):
              await task
          del self.continuous_emote_tasks[user_id]
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        try:     
            await self.highrise.send_whisper(user.id,f"Hey {user.username}\nwelcome to ️420BUNNIES VIBE/TIPS \nMake sure to follow @babyJmia , your host & your amazing dj!\nVIP is 100g to bot! \n• !list or -list or -help :To check commands, \n for bots pm @Alionardo_")
        except Exception as e:
            print(f"error : {e}")
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
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem) -> None:
            print(f"{sender.username} tipped {receiver.username} an amount of {tip.amount}")
            await self.highrise.chat(f"Our {sender.username} tipped {receiver.username} amount of {tip.amount}𝐆𝐎𝐋𝐃")

            if receiver.id  == Counter.bot_id:
              if tip.amount == 100:
                   await self.highrise.teleport(sender.id, Position(15.5,8.5,2.5))
  
    async def follow_user(self, target_username: str):
      while self.following_username == target_username:

          response = await self.highrise.get_room_users()
          target_user_position = None
          for user_info in response.content:
              if user_info[0].username.lower() == target_username.lower():
                  target_user_position = user_info[1]
                  break

          if target_user_position:
              nearby_position = Position(target_user_position.x + 1.0, target_user_position.y, target_user_position.z)
              await self.highrise.walk_to(nearby_position)

              await asyncio.sleep(2)
    async def get_emote_E(self, target) -> None: 

     try:
        emote_info = self.Emotes.get(target)
        return emote_info
     except ValueError:
        pass
    async def on_whisper(self, user: User, message: str ) -> None:

        if message == "!h":
            if user.username in moderator:
                response = await self.highrise.get_room_users()
                users = [content for content in response.content]
                for u in users:
                    if u[0].id == user.id:
                        try:
                            await self.highrise.teleport(Counter.bot_id,Position((u[1].x),(u[1].y),(u[1].z),"FrontRight"))


                            break
                        except:

                            pass
       
        if message.startswith("!s"):
             if user.username in moderator :
                text = message.replace("!s", "").strip()
                await self.highrise.chat(text)

   
         

        elif message.startswith("!c"):
           if user.username in moderator :
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

        elif message.lower().startswith("!f"):
         
            target_username = message.split("@")[1].strip()

            if target_username.lower() == self.following_username:
                await self.highrise.send_whisper(user.id,"I am already following.")
            elif message.startswith("say"):
              if user.username.lower() in self.moderators:
                  text = message.replace("say", "").strip()
                  await self.highrise.chat(text)
            else:
                self.following_username = target_username
                await self.highrise.chat(f"hey {target_username}.")
            
                await self.follow_user(target_username)
        elif message.lower() == "stop following":
            self.following_username = None
          
            await self.highrise.walk_to(Position(15,0,9,"FrontLeft"))
    async def stop_all_loops(self):
      user_ids = [user.id for user, _ in (await self.highrise.get_room_users()).content]
      user_ids.append(Counter.bot_id)
      for user_id in user_ids:
        if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
            task = self.continuous_emote_tasks[user_id]
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task
            del self.continuous_emote_tasks[user_id]
      self.continuous_emote_tasks = {}
    async def stop_continuous_emote(self, user_id: int):
          if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
              task = self.continuous_emote_tasks[user_id]
              task.cancel()
              with contextlib.suppress(asyncio.CancelledError):
                  await task
              del self.continuous_emote_tasks[user_id]
    async def on_chat(self, user: User, message: str):
        try:
            if message.lower().lstrip().startswith(("-list", "!list","-help")):
                await self.highrise.chat("\\commands you can use:\n• !emotes or -emotes\n• !loops or -loops \n• -buy or !buy for \n 🎫VIP Tickets🎫 \n• !rules or -rules")
            if message.lower().lstrip().startswith(("-buy" , "!buy")):
                await self.highrise.chat(f"\n  vip = 100g for vip 🎫 \nTip 100 to bot you will be teleported instantly. ")
         
            if message.lower().lstrip().startswith(("-emotes", "!emotes")):
                await self.highrise.send_whisper(user.id, "\n• Emote can be used by NUMBERS")
                await self.highrise.send_whisper(user.id, "\n• For loops say -loop or !loop then the emote number.")         
            if message.lower().lstrip().startswith(("!loops","-loops")):
                await self.highrise.send_whisper(user.id,"\n• loops\n ____________________________\nMention loop before the emote numer\n ____________________________")
            if message.lower().lstrip().startswith(("-teleport", "!teleport")):
                    await self.highrise.chat(f"\n • Teleports\n ____________________________\n-g : Ground floor \n-dj : DJ setup (only mods and dj)  \n-vip or -v : (vip only), make sure you have 🎫VIP Tickets 🎫 \n• type -buy or !buy for details ")
            if message.lower().lstrip().startswith(("!rules", "-rules")):
                   await self.highrise.chat(f"\n\n        RULES\n ____________________________\n 1. NO UNDERAGE \n 2. No advertising\n 3. No hate speech \n 4. No begging (those trash will be immediately banned 🚫) \n 5. No spamming ")
            if message.startswith("-v")and user.username in co_mod:                              
              await self.highrise.teleport(user.id, Position(15.5,8.5,2.5))
            if message.startswith("-dj")and user.username in co_mod:                    
              await self.highrise.teleport(user.id, Position(16.5,1,1.5)) 
            if message.startswith("-g"):           
              await self.highrise.teleport(user.id, Position(15,0, 9)) 
        
            if message.startswith("!all v")and user.username in co_mod: 
               roomUsers = (await self.highrise.get_room_users()).content
               for roomUser, _ in roomUsers:
                  await self.highrise.teleport( roomUser.id,Position(15.5,8.5,2.5))
            if message.startswith("!all dj")and user.username in co_mod: 
               roomUsers = (await self.highrise.get_room_users()).content
               for roomUser, _ in roomUsers:
                  await self.highrise.teleport( roomUser.id,Position(16.5,1,1.5))
            if message.startswith("!all g")and user.username in co_mod: 
               roomUsers = (await self.highrise.get_room_users()).content
               for roomUser, _ in roomUsers:
                  await self.highrise.teleport( roomUser.id,Position(15,0,9))
            if message.lstrip().startswith(("!v","!g","!dj","!h")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]
                user_name = next((u.username.lower() for u in users if u.username.lower() == args[0][1:].lower()), None)
                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Kullanım: !{parçalar[0]} <@Alionardo_>")
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
                try:
                    
                    if message.startswith("!h")and user.username in co_mod: 
                           target_username = user_name
                           await self.teleport_user_next_to(target_username, user)
                    if message.startswith("!v")and user.username in co_mod:                              
                        await self.highrise.teleport(user_id, Position(15.5,8.5,2.5))
                    if message.startswith("!dj")and user.username in co_mod:                    
                        await self.highrise.teleport(user_id, Position(16.5,1,1.5))
                    if message.startswith("!g")and user.username in co_mod:           
                        await self.highrise.teleport(user_id, Position(15,0, 9)) 

                except Exception as e:
                    print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")

            if message.lower().startswith("loop"):
               parts = message.split()
               E = parts[1]
               E = int(E)
               emote_text, emote_time = await self.get_emote_E(E)
               emote_time -= 1
               user_id = user.id  
               if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                  await self.stop_continuous_emote(user.id)
                  task = asyncio.create_task(self.send_continuous_emote(emote_text,user_id,emote_time))
                  self.continuous_emote_tasks[user.id] = task
               else:
                  task = asyncio.create_task(self.send_continuous_emote(emote_text,user_id,emote_time))
                  self.continuous_emote_tasks[user.id] = task  

            elif message.lower().startswith("stop"):
               if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                  await self.stop_continuous_emote(user.id)
                  await self.highrise.chat("Continuous emote has been stopped.")
               else:
                  await self.highrise.chat("You don't have an active loop_emote.")
            elif message.lower().startswith("users"):
                room_users = (await self.highrise.get_room_users()).content
                await self.highrise.chat(f"There are {len(room_users)} users in the room")
        
            if  message.isdigit() and 1 <= int(message) <= 91:
                parts = message.split()
                E = parts[0]
                E = int(E)
                emote_text, emote_time = await self.get_emote_E(E)    
                tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user.id))]
                await asyncio.wait(tasks)
            
            
            if message == "!tip1":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_1")

            elif message == "!tip5":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_5")

            elif message == "!tip10":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_10")

            elif message == "!tip50":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_50")


            if message.lower().startswith(("!wallet","-wallet","wallet")):
                if user.username in moderator:
                  wallet = (await self.highrise.get_wallet()).content
                  await self.highrise.send_whisper(user.id, f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

            if message.lower().startswith("-loop all") and user.username  in moderators:
              parts = message.split()
              if len(parts) < 2:
                await self.highrise.chat("Please provide an emote ID.")
                return
              try:
               E = int(parts[2])
              except ValueError:
                await self.highrise.chat("Invalid emote ID.")
                return
              emote_text, emote_time = await self.get_emote_E(E)
              emote_time -= 1
              roomUsers = (await self.highrise.get_room_users()).content
              await self.highrise.chat("All looping.")
              for roomUser, _ in roomUsers:
                 if roomUser.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[roomUser.id].cancelled():
                    await self.stop_continuous_emote(roomUser.id)
               
                 task = asyncio.create_task(self.send_continuous_emote(emote_text, roomUser.id, emote_time))
                 self.continuous_emote_tasks[roomUser.id] = task

            elif message.lower().startswith("-stop all"):
              if user.username in moderators:
                 room_users = (await self.highrise.get_room_users()).content
                 user_count = len(room_users)
                 await self.highrise.chat("All looping emotes have been stopped.")
                 for _ in range(user_count):
                     await self.stop_all_loops()
            if message == "!fit0077": 
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
