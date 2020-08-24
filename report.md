|                        |                                 |
|------------------------|---------------------------------|
|__Orgainization__       | [Robocomp](https://robocomp.github.io/web/) |
|__Project name__        | Robocomp GUI Development |
|__Primary repository__  | [robocomp-viriato](https://github.com/robocomp/robocomp-viriato)              |
|__Project Mentors__     | [Araceli Vega Magro](https://github.com/aracelivegamagro), [Pedro Núñez Trujillo](https://github.com/pedromnunez), [Ramon Cintas](https://github.com/rcintas) |
|__Project Page__        | [Summer of Code Project Page](https://summerofcode.withgoogle.com/projects/#4921229867220992)   |
|__Status__              | Completed                       |



# Project Abstract
Graphical user Interfaces (GUIs) plays a significant role in
improving the usability of software and enable smooth interaction between the user and the system.

In this project, I have worked on the GUI part, interfacing it with other components and agent as well. Some of these components work with the DSR (Deep State Representation) and AGM (Active Grammar-based Modeling).




## Major Task of the Project:
  - Creating a Graphical User Interface which will work with inner Model and DSR (Deep State Representation) and facilitate the user to perform operation like moving and positioning the robot and visualising laser Data.

  - Also, this GUI should allow for activity scheduling with Google calender support.

  - This GUI should support ASR and TTS functionality and allow adding, modifying and repositioning persons in inner model and DSR.

  - I have assigned one task which should allow a user to simulate the person position based on a dataset.

  - Another task that is assigned to me is to create a new tool which will automate the process of optimising navigation variables.


## Component that I worked on:
During my GSoC duration i worked on these components:
- [Human Observer Agent GUI](https://github.com/rahulkatiyar19955/gsoc-gui-dev/tree/master/humanObserverAgent_GUI)

- [Human Scene Simulation](https://github.com/rahulkatiyar19955/gsoc-gui-dev/tree/master/HumanSceneSim)

- [Python AGM Agent](https://github.com/robocomp/robocomp-examples/tree/master/getting-started/python/AGM_Agent)

- [Data Capture Component](https://github.com/rahulkatiyar19955/gsoc-gui-dev/tree/master/dataCapture)

- [Navigation Data Reader](https://github.com/rahulkatiyar19955/gsoc-gui-dev/tree/master/navDataReader)

- [Social Navigation GUI](https://github.com/rahulkatiyar19955/gsoc-gui-dev/tree/master/SocialNavigationGUI)


## Challenging part of Project:
There are times when I stuck with problems and didn't able to figure out how to solve them, but with the help of mentors and a lot of googling brings me out.

I will list a few such problems that I faced:
- The first problem that I faced is while setting up the robocomp environment, even a small mistake in the documentation or not correctly specifying the library version number leads to failing the setup.

- While linking the Graphical interface with Robocomp core functionality, I have to read the whole codebase first, which is in itself is a big task.

- Robocomp uses both python2 as well python3, which will make it more challenging to make the code compatible with both.

- Interfacing graphical interface with AGM is a lot more complicated than I thought, as there was no python tutorial available on AGM.


## Future Work:
- Currently, the new DSR is in the Development phase, so in future, all these components can be upgraded to work with the new DSR.


## Links for the Blogs:
1. [Introduction](https://robocomp.github.io/web/gsoc/2020/posts/rahul_katiyar/post01)
2. [Human Observer Agent GUI](https://robocomp.github.io/web/gsoc/2020/posts/rahul_katiyar/post02)
3. [Integrating Google Calendar with GUI](https://robocomp.github.io/web/gsoc/2020/posts/rahul_katiyar/post03)
4. [Human Scene Simulation](https://robocomp.github.io/web/gsoc/2020/posts/rahul_katiyar/post04)
5. [Automated tool to perform optimisation](https://robocomp.github.io/web/gsoc/2020/posts/rahul_katiyar/post05)

## Youtube links:
  [GSoc Robocomp playlist](https://www.youtube.com/playlist?list=PL15a54aGvXvnKV4LLaJrCyd4P8-Jpts6t)
- This playlist contains a tutorial and demonstration of the components that I implemented.


## Commits & Pull Requests

- **Pull Request:** [Added AGM Agent Example #9](https://github.com/robocomp/robocomp-examples/pull/9)

- **Pull Request:** [Components created during GSoC #2](https://github.com/robocomp/robocomp-viriato/pull/2)

 ---
  Pull Request before GSoC
  - https://github.com/robocomp/robocomp/pull/260
  - https://github.com/robocomp/robocomp/pull/243


## Diary
Throughout my GSoC duration, I tried to document the progress and the problems that I faced.
You can find all the daily logs [here..](https://github.com/rahulkatiyar19955/gsoc-gui-dev/tree/master/Diary)


## Conclusion
A remarkable journey comes to an end. I'm very thankful to all my mentors, friends and parents who helped and motivated me during the entire journey. Though GSoC 2020 comes to an end, I'm looking forward to contributing to Open Source and Robocomp Project.

---

**Contact**:\
For any query or suggestions related to the work, feel free to contact me at:\
Email - [rahulkatiyar1995@gmail.com](mailto:rahulkatiyar1995@gmail.com) \
Github Profile - https://github.com/rahulkatiyar19955 \
Twitter - @wowrahul \
Profile - https://rahulkatiyar19955.github.io/
