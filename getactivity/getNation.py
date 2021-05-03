import requests
import json
from settings import *

def getNation (nationID):

    nationLink = pnw + "nation/id=" + str(nationID) + "/" + key
    nationResponse = requests.get(nationLink)

    nationData = nationResponse.text
    
    try:
        nation = json.loads(nationData, strict=False)
        return nation;
    except ValueError:
        print ("Decoding JSON Failed")
    except AttributeError:
        print ("Parsing Failed")

    