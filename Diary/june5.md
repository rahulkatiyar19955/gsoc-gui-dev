## June 5

So after working with googl api that activity agenda now shows a list of all events for the particular day that was selected.
Along with the start time and end time we also need to incorporate many fields like individual name, activity type and many more, and also get these visible to user on google calendar browser ui so that if any user want to modify it using browser(editing remotely) can perform those changes.

So i came up with the idea to store all these fields as JSON in the description part of the event. Using this approach it is easy to
retrieve these fields.

one of the problem that i face is when the one or more fields are missing from the description. so error handling plays a significant role here, proper error handling is used to ensure no such error distrupt the execution.

I have also added 'Z' at the end of the time to make sure all the events are configured with the UTC time. So that there is no confusion regarding the timezone.

Task for tommorow:
- [x] implementing google api with qt
- [x] implement the activity agenda which show all event of that particular day
