# python program to interface with google calendar api

from googleapiclient.discovery import build
from google.oauth2 import service_account

class Calender_api(object):
    """docstring for Calender_api."""
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.credential_file = 'client_secret.json'
        self.service_account_name = 'testacc@robocompgui-1591069682447.iam.gserviceaccount.com'
        self.credentials = service_account.Credentials.from_service_account_file(self.credential_file,scopes=self.SCOPES)
        self.delegated_credentials = self.credentials.with_subject(self.service_account_name)
        self.service = build('calendar', 'v3', credentials=self.delegated_credentials)

    def getEvent(self):
        try:
            page_token = None
            while True:
              events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
              for event in events['items']:
                print(event['summary'])
              page_token = events.get('nextPageToken')
              if not page_token:
                break

        except:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize.')
