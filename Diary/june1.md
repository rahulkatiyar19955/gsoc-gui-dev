## June 1
I have cloned the robocomp-viriato repository. But when I run the cmd inside the folder where simulation.xml file exists, the command executed successfully, but it does not display anything.

After observing the path inside the simulation.xml, I get to know that the robocomp-viriato should be inside the robocomp/component folder. The cmd successfully execute after I did the required modification.  

In the second step, I clone the AGM repository and install all the prerequisite. Running compile.sh, it gives me an error I tried to run "make" in the build directory, and it gives me another error.

`make[2]: pyside-uic: Command not found`
which I think is because of I have pyside2 installed in my system instead of pyside.

I changed **CMakeLists.txt** in build folder with following changes
`line 140 & 151: pyside-uic --changed to --> pyside2-uic`



in **AGM/tools/agmagentsim/ CMakeLists.txt**
`line 19: pyside-uic --changed to --> pyside2-uic`
now it builds successfully

while executing AGMExecutive_robocomp.py i got a error

`"eModuleNotFoundError: No module named 'xmllib'"`

after searching through web i found that it is Deprecated since release 2.0.
since python2 is also deprecated i tried to find a workaround and still finding...  

I have install python2(which is also deprecated) and it is working fine now.




Task for tommorow:

 - [ ] Create a humanObserverAgent_gui with the first_mockup_gui

  - [ ] Setting up a repository for code

  - [ ]  Implementing simple code for google_calender api integration with python

  - [ ] Create a separate repository for diary log, so that it looks nice and readable also
