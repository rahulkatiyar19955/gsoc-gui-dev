# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kati/robocomp/components/robocomp-viriato/components/navDataReader

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kati/robocomp/components/robocomp-viriato/components/navDataReader

# Utility rule file for navDataReader_autogen.

# Include the progress variables for this target.
include src/CMakeFiles/navDataReader_autogen.dir/progress.make

src/CMakeFiles/navDataReader_autogen:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/kati/robocomp/components/robocomp-viriato/components/navDataReader/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC and UIC for target navDataReader"
	cd /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/src && /home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -E cmake_autogen /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/src/CMakeFiles/navDataReader_autogen.dir/AutogenInfo.json ""

navDataReader_autogen: src/CMakeFiles/navDataReader_autogen
navDataReader_autogen: src/CMakeFiles/navDataReader_autogen.dir/build.make

.PHONY : navDataReader_autogen

# Rule to build all files generated by this target.
src/CMakeFiles/navDataReader_autogen.dir/build: navDataReader_autogen

.PHONY : src/CMakeFiles/navDataReader_autogen.dir/build

src/CMakeFiles/navDataReader_autogen.dir/clean:
	cd /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/src && $(CMAKE_COMMAND) -P CMakeFiles/navDataReader_autogen.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/navDataReader_autogen.dir/clean

src/CMakeFiles/navDataReader_autogen.dir/depend:
	cd /home/kati/robocomp/components/robocomp-viriato/components/navDataReader && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kati/robocomp/components/robocomp-viriato/components/navDataReader /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/src /home/kati/robocomp/components/robocomp-viriato/components/navDataReader /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/src /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/src/CMakeFiles/navDataReader_autogen.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/navDataReader_autogen.dir/depend

