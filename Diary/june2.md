## June 2 
I have done a small change in **deployment_GSOC.xml**
`line 17 python --change to ---> python2`

so that it explicitly call python2 rather than python3 to execute AGMExecutive_robocomp.py

I m getting this error while running the fakeHumanAgent
`./bin/fakeHumanAgent: error while loading shared libraries: libagm.so: cannot open shared object file: No such file or directory`

the solution to this problem(suggested by pedro sir)
is to simply add a line `"/usr/local/lib"` without quotes
in `/etc/ld.so.conf` and then run **ldconfig**

I have created a repository to push all my work during gsoc to [Gsoc-GUI-dev](https://github.com/rahulkatiyar19955/gsoc-gui-dev.git)

Task for tommorow:

 - [ ] Create a humanObserverAgent_gui with the first_mockup_gui
       
  - [x] Setting up a repository for code
       
  - [ ]  Implementing simple code for google_calender api integration with python
       
  - [x] Create a separate repository for diary log, so that it looks nice and readable also
  - [ ]  create a activity_form.ui which take inputs from user.
  - [ ]  implementing google api with qt


