import requests
import json
import pandas as pd
import os.path

from settings import *
from getNation import getNation
from datetime import datetime

now = datetime.now()
currentTime = now.strftime("%d-%m-%Y %H:%M:%S")

memberList = {'DiscordID':[], 'Date Founded':[]}

alliance = pnw + "alliance/id=877/" + key
response = requests.get(alliance)
data = response.text

try:
    alliance = json.loads(data, strict=False)
    if (alliance["success"]):
        members = alliance["member_id_list"]
        for i in members:
            memberLog = {'P&W Active':[], 'Discord Messages':[]}

            nation = getNation(i)

            if (nation["success"]):
                print(str(i) + "| inactive: " + str(nation["minutessinceactive"]) + " | founded: " + nation["founded"])

                memberList['DiscordID'].append(0)
                memberList['Date Founded'].append(nation["founded"])

                memberLog['P&W Active'].append(nation["minutessinceactive"])
                memberLog['Discord Messages'].append(0)
                memberDF = pd.DataFrame(memberLog, index = [currentTime])

                memberFile = os.path.abspath('./memberactivity/' + str(i) + '.csv')
                if (os.path.isfile(memberFile)):
                    memberDF.to_csv(memberFile, header=False, mode='a')
                else:
                    memberDF.to_csv(memberFile, header=['P&W Active', 'Discord Messages'])
            else:
                print(nation["error"])

        membersDF = pd.DataFrame(memberList, members)
        membersDF.to_csv(os.path.abspath('./members.csv'), header=['DiscordID', 'Date Founded'])

    else:
        print(alliance["error"])
#except ValueError:
    #print ("Decoding JSON Failed")
except AttributeError:
    print ("Parsing Failed")