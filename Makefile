# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


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

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target install/strip
install/strip: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Installing the project stripped..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -DCMAKE_INSTALL_DO_STRIP=1 -P cmake_install.cmake
.PHONY : install/strip

# Special rule for the target install/strip
install/strip/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Installing the project stripped..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -DCMAKE_INSTALL_DO_STRIP=1 -P cmake_install.cmake
.PHONY : install/strip/fast

# Special rule for the target install/local
install/local: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Installing only the local directory..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -DCMAKE_INSTALL_LOCAL_ONLY=1 -P cmake_install.cmake
.PHONY : install/local

# Special rule for the target install/local
install/local/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Installing only the local directory..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -DCMAKE_INSTALL_LOCAL_ONLY=1 -P cmake_install.cmake
.PHONY : install/local/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake cache editor..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/ccmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target list_install_components
list_install_components:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Available install components are: \"Unspecified\""
.PHONY : list_install_components

# Special rule for the target list_install_components
list_install_components/fast: list_install_components

.PHONY : list_install_components/fast

# Special rule for the target install
install: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Install the project..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -P cmake_install.cmake
.PHONY : install

# Special rule for the target install
install/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Install the project..."
	/home/kati/Desktop/IIT/clion-2020.1.2/bin/cmake/linux/bin/cmake -P cmake_install.cmake
.PHONY : install/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/CMakeFiles /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /home/kati/robocomp/components/robocomp-viriato/components/navDataReader/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src

# Build rule for target.
ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src
.PHONY : ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src

# fast build rule for target.
ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src/fast:
	$(MAKE) -f src/CMakeFiles/ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src.dir/build.make src/CMakeFiles/ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src.dir/build
.PHONY : ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src/fast

#=============================================================================
# Target rules for targets named navDataReader

# Build rule for target.
navDataReader: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 navDataReader
.PHONY : navDataReader

# fast build rule for target.
navDataReader/fast:
	$(MAKE) -f src/CMakeFiles/navDataReader.dir/build.make src/CMakeFiles/navDataReader.dir/build
.PHONY : navDataReader/fast

#=============================================================================
# Target rules for targets named navDataReader_autogen

# Build rule for target.
navDataReader_autogen: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 navDataReader_autogen
.PHONY : navDataReader_autogen

# fast build rule for target.
navDataReader_autogen/fast:
	$(MAKE) -f src/CMakeFiles/navDataReader_autogen.dir/build.make src/CMakeFiles/navDataReader_autogen.dir/build
.PHONY : navDataReader_autogen/fast

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... install/strip"
	@echo "... install/local"
	@echo "... edit_cache"
	@echo "... rebuild_cache"
	@echo "... list_install_components"
	@echo "... install"
	@echo "... ICES__home_kati_robocomp_components_robocomp-viriato_components_navDataReader_src"
	@echo "... navDataReader"
	@echo "... navDataReader_autogen"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

