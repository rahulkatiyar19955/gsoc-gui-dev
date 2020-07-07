## July 7

* on starting the code i get a Error\
Unable to open display ":1.0".\
Error: Unable to open display ":1.0".\
Can't open graphics window\
Aborted (core dumped)

    * the solution for this as explained by araceli is to change a line in 
        **innerviewer.cpp** \
        ```wsi->getScreenResolution(osg::GraphicsContext::ScreenIdentifier("",0, 0), width, height);```

         and remove this line \
        ```traits->displayNum = 1;```



Task for tomorrow:
- [x] creating a copy of the component newSocialNavigationAgent
- [ ] understand the component
