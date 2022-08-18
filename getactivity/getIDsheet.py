import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('./bk-members.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("All the BK Members").worksheet('discordid')

def getSpreadsheet():
    df = pd.DataFrame(sheet.get_all_records())
    df.set_index('NationID', inplace=True)
    return df