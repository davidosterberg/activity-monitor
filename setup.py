#!/usr/bin/env python
# coding: utf-8
from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.

setup(name = "activity-monitor",
    version = "1.0",
    description = "A utility to monitor how much time you spend on your projects",
    author = "David Österberg",
    author_email = "david.osterberg@husqvarnagroup.com",
    url = "http://www.husqvarna.se",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['src'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    long_description = """A utility to monitor how much time you spend on your projects""",
    scripts=['bin/activity_report','bin/activity_query'],
    entry_points = {'console_scripts': ['activity_report = activity_report:main',
                                        'activity_query = activity_query:main']}
) 
