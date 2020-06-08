from google_calender import CalenderApi
from datetime import datetime, timedelta, date, time
import json

# initializing the Calendar API object
apiObj = CalenderApi()

# today date
d = datetime.utcnow().date()

# tommorow date
tomorrow = datetime(d.year, d.month, d.day, 10) + timedelta(days=1)

start = tomorrow.isoformat()
end = (tomorrow + timedelta(hours=1)).isoformat()

# sample object example
#     { "Type": "Individual",
#       "IndividualName": "",
#       "TherapistName": "",
#       "Location": "Physical therapy room",
#       "Element": "TV",
#       "Notification": "False",
#       }
# body = {"summary": 'Hello there, Automating calendar',
#         "description": ,
#         "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
#         "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
#         }

desciptionJson = {'Type': 'Individual', 'IndividualName': '', 'TherapistName': '', 'Location': 'Physical therapy room',
                  'Element': 'Stretcher', 'Notification': False}
body = {'summary': 'Activity test', 'description': json.dumps(desciptionJson),
        'start': {'dateTime': '2020-06-06T00:00:00Z'}, 'end': {'dateTime': '2020-06-06T05:00:00Z'}}


def Call_CreateEvent():
    apiObj.createEvent(bodyContent=body)


# get all events for a particular day
def Call_getEvents():
    date_obj = date.today()
    date_obj = datetime(date_obj.year, date_obj.month, date_obj.day, 10) + timedelta(days=1)
    # getting events for tommorow
    eventList = apiObj.getEvents(date_obj)
    for event in eventList:
        try:
            print(event["summary"])
            jsonObj = json.loads(event["description"])
        except:
            pass


# get all event in the calendar
def Call_getAllEvent():
    eventList = apiObj.getAllEvent()
    for event in eventList:
        try:
            print(event["summary"])
            jsonObj = json.loads(event["description"])
        except:
            pass


# insert a email address to authorize to view the calendar
# emailAddress should be a string
def Call_giveAccess(emailAddress):
    print(apiObj.giveAccess(emailAddress=emailAddress))


def main():
    Call_CreateEvent()
    Call_getAllEvent()


if __name__ == "__main__":
    main()
