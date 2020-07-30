## July 29

### Problems that i encounter while writing AGM agent in python.

- one of things that i observed is that the ids that we passed as an argument to the AGMGraph or RobocompAGMWorld is of type string, it will works with int also, but as soon as you remove any node or link it will give you error as int cannot be compared with string direclty.

- while create a RT link, make sure there is no cycle formed in the graph, if found will make the program exist with the error `RT loop detected`.

- You must specify your component name in the *executive.config* file, and make sure the ports are all consistent with the other components also.



---
Task for tomorrow:
- [x] Addition in the previous component(dataCapture and NavDataReader)
