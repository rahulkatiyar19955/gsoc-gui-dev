## August 5

**My approach to this problem will be:**

step1 .Define a correct path between two known points

step2 Save this data as a regerence data set

step3 For a particular selected variable with a constant delta(increment)\
  minValue -> maxValue

step4 Save the data for every intermediate value in the range

step5 Compute the error buy comparing it with the metrics of reference data

step6 Fix the value of that variable which has the minimum error

step7 Perform the step3 to step6 for every other variable.

---

......methods to perform the steps........

step1 —> this step can be performed by first selecting the start and end points, and then navigate the robot by joystick or keyboard

step2 —> this step can be achieved using the dataCapture component.

step3 —> (new) write another component which will change the value of the variable at every iteration.

step4 —> this step is also achieved using the dataCapture component.

step5 —> NavDataReader with slight modification can give the value of the variable which has the minimum error value.

step6 —> this step can be done manually by entering the value that is get form the previous step. into the code.

step7 —> iterating over all the variables by manually executing the code for every variable.





---
Task for tomorrow:

- [x] devise an optimizing strategy

- [ ] write down the steps in automating the workflow
