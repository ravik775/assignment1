from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.

SAMPLE_RANGE_NAME = 'Sheet1!A1:E'#'Class Data!A2:E'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    #https://docs.google.com/spreadsheets/d/1YfQEcgK2L-wPP5mgQOSdoPNUBqYIvF0ieDC7KQ7ORos/edit?usp=sharing
    SAMPLE_SPREADSHEET_ID = '1YfQEcgK2L-wPP5mgQOSdoPNUBqYIvF0ieDC7KQ7ORos'
    creds = None
    # https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
    #
    # Authorize using one of the following scopes:
    #     'https://www.googleapis.com/auth/drive'
    #     'https://www.googleapis.com/auth/drive.file'
    #     'https://www.googleapis.com/auth/drive.readonly'
    #     'https://www.googleapis.com/auth/spreadsheets'
    #     'https://www.googleapis.com/auth/spreadsheets.readonly'
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    if not SAMPLE_SPREADSHEET_ID:
        res = sheet.create(body={'properties': {'title': 'Example Sheet %s' % time.strftime("%y-%m-%d")}}).execute()
        SAMPLE_SPREADSHEET_ID = res['spreadsheetId']
        print ("Created sheet %s"% res["properties"]["title"])

        data = {'values': [('Name', 'Country', 'Mobile Number'),
                       ('John','US', '7896541230'), ('Steve','UK', '7198657416')]}

        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME, valueInputOption='RAW', body=data).execute()
    include_grid_data = True
    result = sheet.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, ranges=SAMPLE_RANGE_NAME, includeGridData=include_grid_data).execute()
    print ("Result or return")
    print (result.get('values', []) )
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s, %s' % (row[0], row[1], row[2]))

if __name__ == '__main__':
    main()