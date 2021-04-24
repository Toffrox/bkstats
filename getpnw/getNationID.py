import requests
import json
from settings import *

def getNationActivity (nationID):

    nationLink = pnw + "nation/id=" + str(nationID) + "/" + key
    nationResponse = requests.get(nationLink)

    nationData = nationResponse.text
    
    try:
        nation = json.loads(nationData, strict=False)
        if (nation["success"]):
            minutes = nation["minutessinceactive"]
            return minutes
        else:
            print(nation["error"])
            return -1
    except ValueError:
        print ("Decoding JSON Failed")
    except AttributeError:
        print ("Parsing Failed")

    