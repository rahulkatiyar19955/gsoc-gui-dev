# python program to interface with google calendar api

from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, time


class CalenderApi(object):
    """docstring for CalenderApi."""

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.credential_file = 'client_secret.json'
        self.service_account_name = 'testacc@robocompgui-1591069682447.iam.gserviceaccount.com'
        self.credentials = service_account.Credentials.from_service_account_file(self.credential_file,
                                                                                 scopes=self.SCOPES)
        self.delegated_credentials = self.credentials.with_subject(self.service_account_name)
        self.service = build('calendar', 'v3', credentials=self.delegated_credentials)

    # this method is used to fetch event for a particular date
    def getEvents(self, date_argument):
        eventList = []
        try:
            page_token = None
            startTime = time(hour=0, minute=0, second=0)
            endTime = time(hour=23, minute=59, second=59)
            today_beginning = datetime.combine(date_argument, startTime).isoformat() + 'Z'
            today_ending = datetime.combine(date_argument, endTime).isoformat() + 'Z'
            while True:
                events = self.service.events().list(calendarId=self.service_account_name,
                                                    pageToken=page_token,
                                                    timeMin=today_beginning,
                                                    timeMax=today_ending).execute()
                for event in events['items']:
                    eventList.append(event)
                page_token = events.get('nextPageToken')
                if not page_token:
                    break
        except:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize.')
        finally:
            return eventList

    # get all events on a calendar
    def getAllEvent(self):
        eventList = []
        try:
            page_token = None
            while True:
                events = self.service.events().list(calendarId=self.service_account_name,
                                                    pageToken=page_token).execute()
                for event in events['items']:
                    eventList.append(event)
                page_token = events.get('nextPageToken')
                if not page_token:
                    break
            return eventList
        except:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize.')

    # create a event with the information provided in the bodycontent
    def createEvent(self, bodyContent):
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

    # get a list of calendars
    def getCalenderList(self):
        try:
            calendar = self.service.calendars().get(calendarId='primary').execute()
            print(calendar)

        except:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize.')

    # this method is used to give access to a email address,
    # so that using this id we can manipulate event using
    # browser
    def giveAccess(self,emailAddress):
        rule = {
            'scope': {
                'type': "user",
                'value': emailAddress,
            },
            'role': 'owner'
        }
        created_rule = self.service.acl().insert(calendarId='primary', body=rule).execute()
        return created_rule['id']