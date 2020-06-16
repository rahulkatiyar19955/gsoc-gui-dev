## June 15

* Added functionality to check for internet connectivity,
if not then disable the Activity Calendar

* Also added the functionality to add human into AGM as well as RCIS.
 
After adding the person using the interface that i build, it successfully added it both in RCIS and AGM.
but when i try to move the person using fakeHumanAgent GUI it shows the following error:

` PERSON NAME IN MOVE "person<built-in function id>"
Exception retrieving transform from RCIS: ::RoboCompInnerModelManager::InnerModelManagerError
`

This can be because of the person id which is not consistent with the id in RCIS.


Task for tomorrow:
- [x] write a code to insert a node in DSR
- [ ] added human information to the Human class




