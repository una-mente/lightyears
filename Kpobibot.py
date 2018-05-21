# -*- coding: utf-8 -*-
"""
Created on Thu May 17 15:38:22 2018

@author: KPOBI
"""

import requests
import emoji


url = "https://api.telegram.org/bot593981601:AAEY_vRx5gqHmttHmJFHpgX2lHFQMNhY8-E/"

update_id=[]

text = """. 
:white_flag::white_flag:GHLOYALS:white_flag::white_flag: 
GHLOYALS IS A PEER TO PEER PLATFORM WHERE MEMBERS CARE AND HELP EACH OTHER FINANCIALLY.
WE BELIEVE IN TRANSPARENCY AND ANY LOYAL MEMBER ON THIS PLATFORM SHOULD BE FREE FINANCIALLY.

✍✍ HOW GHLOYALS WORKS

:white_check_mark: A CENTRAL VAULT WILL BE PROVIDED WHEN LAUNCHING IS DUE.

:white_check_mark:ALL TRANSACTIONS WILL BE DONE BY MANAGER WITH THE HELP OF ASSISTANT AND A VOLUNTEERED MEMBER ( who will be representing all members)

:white_check_mark:ROI (Return of investment)IS 70% OF PH (pledge Help) OR AMOUNT PLEDGE

:white_check_mark:MATURITY IS 5DAYS

:white_check_mark:MINIMUM PH IS 100

:white_check_mark:MAXIMUM PH IS 200

:white_check_mark:RECOMMITMENT IS 100% OF PH. REMEMBER ON THIS PLATFORM, WE RECOMMIT BY SENDING MONEY AND NOT BY MOUTH!

:white_check_mark:20% SUSTAINABLE FEE OF EVERY PH OR RECOMMITMENT IS COMPULSORY.

This fee is to make sure the system works efficiently and effectively, and also to make sure that members can recover their money:moneybag: in case of any eventually.

:pushpin::pushpin:NOTE!!

NO WEBSITE WILL BE USED NOR CREATED.
EVERYTHING IS "MANUAL " WITH A COMPUTERIZED SYSTEM TO MONITOR ALL TRANSACTIONS EFFICIENTLY.

:heart:WE BELIEVE IN 100% TRANSPARENCY :heart:

:white_check_mark: PLEASE LET'S KEEP ON INVITING MORE FRIENDS AND LET TAKE TIME TO EXPLAIN THE SYSTEM TO THEM

:key:HOWEVER, REMEMBER WE NEED A SIZEABLE NUMBER TO START AND MAKE IT JUICY AND SUSTAINABLE TO ALL OF US.:grin:

THANK YOU AND GOD BLESS US ALL:pray:

:pray::pray:GOD BLESS GHLOYALS :pray:

Join GHLoyals through this link
:point_down::point_down::point_down::point_down::point_down:

https://t.me/joinchat/IE906g9tJWwlchuXSFaKgg

KIND REGARDS,
MANAGEMENT
contact:0552707677
"""
def bot():
    while True:
        response = requests.get(url + 'getUpdates')
        all_response = response.json()
        result = all_response['result'][-1]
            
        if result['message']['chat']['type'] == 'group':
            if result['update_id'] not in update_id:
                update_id.append(result['update_id'])
                try:
                    if result['message']['new_chat_members']:
                        print (result['message']['new_chat_members'][0]['last_name'])
                        chat_id = result['message']['chat']['id']
                        gtitle = result['message']['chat']['title']
                        name = result['message']['new_chat_members'][0]['last_name']
                        params = {'chat_id': chat_id, 'text': emoji.emojize('Hi '+ name +
                        ', Welcome to '+ gtitle + text, use_aliases=True)}
                        response = requests.post(url + 'sendMessage', data=params)
                except:
                    continue
                
try:
    bot()
    
except:
    pass
