from google_calender import CalenderApi
from datetime import datetime,timedelta
import json

apiObj = CalenderApi()
# apiObj.getEvent()
# apiObj.getCalenderList()
d = datetime.utcnow().date()
tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
start = tomorrow.isoformat()
end = (tomorrow + timedelta(hours=1)).isoformat()
desciptionJson = {'Type': 'Individual', 'IndividualName': '', 'TherapistName': '', 'Location': 'Physical therapy room', 'Element': 'Stretcher', 'Notification': False}
body={'summary': 'Activity 2', 'description': json.dumps(desciptionJson), 'start': {'dateTime': '2020-06-06T00:00:00Z'}, 'end': {'dateTime': '2020-06-06T05:00:00Z'}}


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
eventList = apiObj.getAllEvent()
for event in eventList:
    try:
        print(event["description"])
        jsonObj = json.loads(event["description"])
        print(jsonObj["Type"])
    except:
        pass

# apiObj.createEvent(bodyContent=body)
# apiObj.getAllEvent()

# apiObj.getAllEvent()