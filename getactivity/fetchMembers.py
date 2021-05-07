import requests
import json
import pandas as pd
import os.path
import asyncio

from settings import *
from getNation import getNation
from getDiscord import getDiscord
from getIDsheet import getSpreadsheet
from datetime import datetime

async def get_alliance_json():
    alliance = pnw + "alliance/id=877/" + key
    response = requests.get(alliance)
    return response.text

async def fetchMembers():
    while True:
        now = datetime.now()
        currentTime = now.strftime("%d-%m-%Y %H:%M:%S")

        memberList = {'DiscordID':[], 'Date Founded':[]}

        data = await get_alliance_json()

        try:
            alliance = json.loads(data, strict=False)
            if (alliance["success"]):
                members = alliance["member_id_list"]
                ids = getSpreadsheet()

                for i in members:
                    memberLog = {'P&W Active':[], 'Discord Messages':[]}

                    nation = getNation(i)

                    if (nation["success"]):
                        #append to the all members list
                        memberList['DiscordID'].append(0)
                        memberList['Date Founded'].append(nation["founded"])

                        #append pnw activity to individual member dataframe
                        memberLog['P&W Active'].append(nation["minutessinceactive"])
                        
                        try:
                            #get discord id from nation id, then count messages
                            messageCount = await getDiscord(ids.loc[i].DiscordID)
                            #append discord activity to individual member dataframe
                            memberLog['Discord Messages'].append(messageCount)
                        except KeyError:
                            memberLog['Discord Messages'].append(0)

                        #create individual member dataframe
                        memberDF = pd.DataFrame(memberLog, index = [currentTime])

                        #if individual member activity csv exists, then append, if not, create
                        memberFile = os.path.abspath('./memberactivity/' + str(i) + '.csv')
                        if (os.path.isfile(memberFile)):
                            memberDF.to_csv(memberFile, header=False, mode='a')
                        else:
                            memberDF.to_csv(memberFile, header=['P&W Active', 'Discord Messages'])
                    else:
                        print(nation["error"])

                #create dataframe for list of all members
                membersDF = pd.DataFrame(memberList, members)
                membersDF.to_csv(os.path.abspath('./members.csv'), header=['DiscordID', 'Date Founded'])

            else:
                print(alliance["error"])
        except ValueError:
            print ("Decoding JSON Failed")
        except AttributeError:
            print ("Parsing Failed")

        await asyncio.sleep(7200)

#event loop
loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(fetchMembers())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()