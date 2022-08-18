import requests
import json
from settings import *

# get nation JSON by nation ID
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
