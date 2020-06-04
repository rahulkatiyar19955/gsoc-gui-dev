# python program to interface with google calendar api

from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

class CalenderApi(object):
    """docstring for CalenderApi."""

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.credential_file = "client_secret.json"
        self.service_account_name = 'testacc@robocompgui-1591069682447.iam.gserviceaccount.com'
        self.credentials = service_account.Credentials.from_service_account_file(self.credential_file,
                                                                                 scopes=self.SCOPES)
        self.delegated_credentials = self.credentials.with_subject(self.service_account_name)
        self.service = build('calendar', 'v3', credentials=self.delegated_credentials)

    def getEvent(self,date):
        eventList = []
        try:
            page_token = None
            timeMin = date.isoformat()
            timeMax = (date + timedelta(days=1)).isoformat()
            while True:
                events = self.service.events().list(calendarId=self.service_account_name,
                                                    pageToken=page_token,
                                                    timeMin = timeMin,
                                                    timeMax= timeMax).execute()
                for event in events['items']:
                    print(event['summary'])
                page_token = events.get('nextPageToken')
                if not page_token:
                    break
        except:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize.')

    def getAllEvent(self):
        eventList = []
        try:
            page_token = None
            while True:
                events = self.service.events().list(calendarId=self.service_account_name,
                                                    pageToken=page_token).execute()
                for event in events['items']:
                    eventList.append(event)
                    print(event)
                page_token = events.get('nextPageToken')
                if not page_token:
                    break
            return eventList
        except:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize.')

    def createEvent(self,bodyContent):
        """Function to create event in the calender"""
        # sample body example
        # body = {"summary": 'Activity Number',
        #         "description": { "Type": "Individual",
        #                           "IndividualName": "",
        #                           "TherapistName": "",
        #                           "Location": "Physical therapy room",
        #                           "Element": "TV",
        #                           "Notification": "False",
        #                           },
        #         "start": {"dateTime": start},
        #         "end": {"dateTime": end},
        #         }
        event = self.service.events().insert(calendarId=self.service_account_name, body=bodyContent).execute()
        return event

    def getCalenderList(self):
        try:
            calendar = self.service.calendars().get(calendarId='primary').execute()
            print(calendar)

        except:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize.')


