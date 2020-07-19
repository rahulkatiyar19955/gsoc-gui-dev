## July 13

* So for the successfull navigation we need a component which will act as a observer and prompt the user when the robot obstructed by the obstacle or the human, at this time a timeout should occur with the message that *the robot is blocked*.
* also a message should appear when the robot successfully reach the target coordinate as instructed by the user in the GUI.
* timeout should also occur when robot keeps moving for a particular time and didn't reach to its goal.

---

* All the data that are generated in this process must be saved somewhere for further analysis.
* these data must include
  - minimum obstacle distance and angle
  - pose of the robot
  - target achieved or not

---
- for timeout implementation part we can create a QTimer with user selectable timeperiod. and check for the robot movement, if it stops and is on or near to the target location we can know that the robot has achieved the goal, and if it is not near the target or blocked by human we can know that it is blocked.

- blockage with human can be obtained from the DSR by checking the if there is any link between the robot and human with *is_softblock* or *is_blocking* link type.

---
- for saving data we can make a class with the variables as its private variables, and create a array of class objects, and then write these class objects into a file.



Task for tomorrow:
- [X] design a pipeline for the component
- [ ] implementing the component to capture navigation data
