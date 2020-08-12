## August 14

### Errors while running viriatoPyrep:

---

```
File "/home/rahul/.local/lib/python3.6/site-packages/pyrep/objects/object.py", line 25, in init
  assert_type = self._get_requested_type()
File "/home/rahul/.local/lib/python3.6/site-packages/pyrep/objects/object.py", line 88, in _get_requested_type
  raise NotImplementedError('Must be overridden.')
NotImplementedError: Must be overridden.
```
 - The solution to this problem is comment few lines of codes in **pyrep/objects/object.py**
  -
 ```
 #assert_type = self._get_requested_type()
 #actual = ObjectType(sim.simGetObjectType(self._handle))
 #if actual != assert_type:
 #    raise WrongObjectTypeError(
 #        'You requested object of type %s, but the actual type was '
 #        '%s' % (assert_type.name, actual.name))
```

- After doing these change the Virtual machine stop unexpectedly with the error:
`the instruction at 0xec408b71 referenced memory at 0x00000400. The memory could not be written`

- after so many trial and error, finally got a the solution.
  - change the display driver setting of the VM by switching off the 3d acceleration and selecting VMSVGA driver.
  - this will work but is significantly slower than the previous.
  - for better performance install the DSR in a standalone OS (not in the Virtual Machine), as Running an instance of CORTEX requires a powerfil machine, also we are runnning the "brain" of the robot in a simulated realistc world.

---




 Task for tomorrow:

 - [x] Setting up a clean installation of the new DSR
 - [ ] Start documenting the work
 - [ ] Combine everything, so that everything work seamlessly with each other.
 - [x] Error occured while running different dsr components.
