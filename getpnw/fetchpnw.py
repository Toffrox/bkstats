import requests
import json
from settings import *
from getNationID import getNationActivity

alliance = pnw + "alliance/id=877/" + key

response = requests.get(alliance)
data = response.text
try:
    alliance = json.loads(data, strict=False)
    if (alliance["success"]):
        members = alliance["member_id_list"]
        for i in members:
            print(str(i) + ": " + str(getNationActivity(i)))
    else:
        print(alliance["error"])
except ValueError:
    print ("Decoding JSON Failed")
except AttributeError:
    print ("Parsing Failed")