## June 3

Today i have implement a client code to interface with google calender api.
for this purpose a separate google account is created with id _testrobocomp@gmail.com_
 
google Calender api use Oauth2.0 for interfacing with the client which opens up a consent
 screen when the client make a request for authorization 
 token, which is not suitable for our case as we have dedicated google
 account for saving calender event
 <br>
 so i figure out there is a service account method using which
 we can use same account for all user and there will be no consent screen pop up 
 when a request is sent.
     
     +--------+                               +---------------+
     |        |--(A)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+
Oauth protocol flow

Regarding the first part of the Gui where new activity is added by the user is 
done now.
So, when the user click on the new activity button, a new dialog box will pop up 
requesting all the necessary information, after submiting it will add up into the activities items.

Task for tommorow:
- [x] Create a humanObserverAgent_gui with the first_mockup_gui
- [x]  Implementing simple code for google_calender api integration with python
- [x]  create a activity_form.ui which take inputs from user.
- [ ]  implementing google api with qt