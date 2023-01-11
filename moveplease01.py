#!/usr/bin/env python3

import shutil
import os #provides access to low level os operations


os.chdir('/home/student/mycode/') #move into this directory
shutil.move('raynor.obj', 'ceph_storage/') #try moving the raynor files .obj into ceph_stroage/dir


xname = input('What is the new name for kerrigan.obj? ') #collect string input from the user
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moving kerrigan.obj into ceph_storage/ with chosen name

