=====
Regression on Order Statistics
=====

A basic utility to recover the mean and standard deviation of a left censored normally distributed data set.


Requirements
============

python 2.7
numpy 1.9.0
scipy 0.14


Motivation
==========

A colleague had some sensor data that included a bunch of non-detects at low values and needed a way to estimate the distribution.  I couldn't find a python implementation of ROS algorithm online so I wrote this simple version to handle it.  

TODO
====

Eventually I'll expand this to handle other distributions and more complicated censor scenarios.

Authors
=======

Created by Christopher Bates (@chrsbats).

