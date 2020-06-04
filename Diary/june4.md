## June 4


A service account's credentials, which you obtain from the Google API Console, include a generated email address that is unique, a client ID, and at least one public/private key pair. You use the client ID and one private key to create a signed JWT and construct an access-token request in the appropriate format. Your application then sends the token request to the Google OAuth 2.0 Authorization Server, which returns an access token. The application uses the token to access a Google API. When the token expires, the application repeats the process.
Your server application uses a JWT to request a token from the Google Authorization Server, then uses the token to call a Google API endpoint. No end-user is involved. 

while using the calendar of service account, I found that the calendar that it uses is different than 
the owner calendar, and also it is no where seen in browser (calendar.google.com).

To view the calendar we must add the calendar and give access to the user to view and modify events.
the trickest part is to figure out how to give access from the service account as the service account 
is a dummy account and no where can be seen.

So the only solution i came up with is to programmatically give access to user using **_(acl.insert)_** of the google calendar api.

Now, as soon as you clicked the new activity and click OK, it saves the information 
in a event for the time mentioned on the form and date on the activity agenda gui. 


Task for tommorow:
- [x]  implementing google api with qt
- [ ]  implement the activity agenda which show all event of that particular day
