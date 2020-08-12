## August 13

### Settin up Clean installation of dsr
1. First step is to install the Robocomp.
2. Installing the  following dependencies
  - cppItertools
  - gcc-9
  - Fast-CDR
  - foonathan_memory_vendor
  - Fast-DDS
  - pyRep


  ```
 sudo git clone https://github.com/ryanhaining/cppitertools /usr/local/include/cppitertools
 ```
 ```
 sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
 sudo apt update
 sudo apt install -y gcc-9
 ```
 ```
 mkdir ~/software
 cd ~/software
 git clone https://github.com/eProsima/Fast-CDR.git
 mkdir Fast-CDR/build
 cd Fast-CDR/build
 export MAKEFLAGS=-j$(($(grep -c ^processor /proc/cpuinfo) - 0))
 cmake ..
 cmake --build .
 sudo make install
 cd ~/software
 git clone https://github.com/eProsima/foonathan_memory_vendor.git
 cd foonathan_memory_vendor
 mkdir build
 cd build
 cmake ..
 cmake --build .
 sudo make install
 cd ~/software
 git clone https://github.com/eProsima/Fast-DDS.git
 mkdir Fast-DDS/build
 cd Fast-DDS/build
 cmake ..
 cmake --build .
 sudo make install
 ```
 ```
 sudo apt install -y libasio-dev libtinyxml2-dev libqglviewer-dev-qt5
 sudo ldconfig
 ```
 ```
 git clone https://github.com/stepjam/PyRep.git
 cd PyRep
 echo "export COPPELIASIM_ROOT=<CoppeliaSim path>" >> ~/.bashrc
 echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$COPPELIASIM_ROOT" >> ~/.bashrc
 echo "export QT_QPA_PLATFORM_PLUGIN_PATH=$COPPELIASIM_ROOT" >> ~/.bashrc
 source ~/.bashrc
 pip3 install -r requirements.txt
 python3 setup.py install --user
 ```
 >  **Note:**  Make sure to replace **<CoppeliaSim path\>** with the Coppelia Sim path in your machine

 While installing PyRep if you get an error:  
 -	```
   build/pyrep/backend/pyrep/backend/_sim_cffi.c:22:12: fatal error: pyconfig.h: No such file or directory
   #  include <pyconfig.h>
                      ^~~~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    ```
  then install these packages:
  `sudo apt-get install python3-dev python3.6-dev`
 ---
 -		> ImportError: libcoppeliaSim.so.1: cannot open shared object file: No such file or directory

  Add the CoppeliaSim path to `/etc/ld.so.config/` and then `sudo ldconfig`
 ---
 -   > /usr/bin/ld: cannot find -lcoppeliaSim
 collect2: error: ld returned 1 exit status
 error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

  make sure correct path of coppeliaSim is set in the `LD_LIBRARY_PATH`
 ---
 -  > ImportError: /usr/lib/x86_64-linux-gnu/libQt5Gui.so.5: symbol  NumberOptionEE version Qt_5 not defined in file
 libQt5Core.so.5 with link time reference

  make sure you have `ls /usr/lib/x86_64-linux-gnu/libQt5Gui.so.5` file in your machine. After that start the `./run.sh `
 without *sudo*
 ---
 3. clonning the https://github.com/robocomp/dsr-graph.git
 4. go to the viriatoPyrep directory and run the `./run.sh`
 -  > from pyrep.robots.mobiles.viriato import Viriato
 ModuleNotFoundError: No module named 'pyrep.robots.mobiles.viriato'

  Then make sure you copied the viriato.py from dsr-grpah/pyrep to
  `/home/xxxyour-userxxx/.local/lib/python3.6/site-packages/pyrep/robots/mobiles/viriato.py`
 -  ```
     import numpy_indexed as npi \
       ModuleNotFoundError: No module named 'numpy_indexed'
       ```
  install the following package `pip3 install numpy-indexed`

  Make sure you have all these dependencies required for Viriato_Pyrep:\
 - OpenCV version 3 is also required by the PyRep
   - install it from the openCV git repo
 ---

 ---
 Task for tomorrow:

 - [x] Setting up a clean installation of the new DSR
 - [ ] Start documenting the work
 - [ ] Combine everything, so that everything work seamlessly with each other.
 - [ ] Error occured while running different dsr components.
