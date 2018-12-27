import gspread
import facebook
import sys
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope) #Included json file only has placeholders due to privacy

client = gspread.authorize(credentials)

# Stand in Google Sheets file name, spreadsheet with three rows: Confession, Number, Posted Status
sheet = client.open('TestData').sheet1

token = sys.argv[1]
graph = facebook.GraphAPI(access_token=token)

baseCon = 8500  # Base post number in case the confession count resets/no access to previous confession number


def post(entryNumber):  # Posts unposted entries onto the Facebook page
    if sheet.cell(entryNumber, 1).value:
        if sheet.cell(entryNumber, 3).value != 'Posted':  # If the entry has not been posted
            posting = '#' + str(sheet.cell(entryNumber, 2).value) + \
                ': ' + '"' + sheet.cell(entryNumber, 1).value + '"'
            sheet.update_cell(entryNumber, 3, 'Posted')  # Update Posted Status
            graph.put_object(parent_object='me', connection_name='feed', message=posting)  # Post


for i in range(2, sheet.row_count):  # Go through all rows
    if sheet.cell(i, 1).value:
        if sheet.cell(i, 2).value == '':  # Continues confession number sequence, assigns value
            baseCon += 1
            sheet.update_cell(i, 2, baseCon)
            post(i)
        else:
            # If a confession number has already been assigned
            val = int(sheet.cell(i, 2).numeric_value)
            baseCon = val
            post(i)
    else:
        break
