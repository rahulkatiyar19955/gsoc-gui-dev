cmake_minimum_required(VERSION 2.6)
PROJECT(  humanObserverAgent_GUI )

INCLUDE( $ENV{ROBOCOMP}/cmake/robocomp.cmake )

ROBOCOMP_IDSL_TO_ICE( CommonBehavior AGMCommonBehavior AGMExecutive AGMExecutiveTopic AGMWorldModel Planning )
