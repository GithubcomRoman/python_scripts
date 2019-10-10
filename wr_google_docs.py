from pprint import pprint

import re
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'file.json'
spreadsheet_id = 'enter yours'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


with open('file.data', 'r') as f:
    nums = f.read().splitlines()
number_of_ct=len(nums)
number_of_ct -= 1
#number_of_ct=4

print("Containers on server:", number_of_ct)

i = 1

while number_of_ct > 0:
        ct_info = re.split(r'[|]', nums[number_of_ct])
        ia = str(i)
        iA = "A"
        gg = str(20)
        gG = ":G"
        range = (iA + ia + gG + gg)

        values = service.spreadsheets().values().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body={
                        "valueInputOption": "USER_ENTERED",
                        "data": [
                                {"range": range,
                                "majorDimension": "ROWS",
                                "values": [[ct_info[1], ct_info[2], ct_info[3], ct_info[4], ct_info[5], ct_info[6], ct_info[7]]]}
                        ]
                }
        ).execute()
        i += 1
        number_of_ct -= 1
