#!/usr/bin/python -O

from subprocess import call, check_output
import os
import utils
from scanner import *
from pdfmaker import *


working_dir     = "/tmp/autopdf"
git_dir     = os.path.abspath("git") #Must exist, and be a git rep.

if not os.path.exists(working_dir):
    os.makedirs(working_dir)

def fail(msg):
    with open("log.txt", "a") as log:
        log.write(msg)
    raise



#Update GIT
try:
    os.chdir(git_dir)
#   call("git pull", shell=True) and fail("oops")
except:
    fail("git update failed")


#Get all courses
print git_dir
scanner = FileScanner(["java"])
pdfmaker = PDFMaker()

courses = scanner.scan(git_dir)
changes = set(scanner.getChanged(git_dir))


for project in course.projects:
    #Skip if no changes
    if changes & set(project.file_paths): #If the file list has changes
        pdfmaker.make(project.name, project.file_paths, project.getTempDir(working_dir))


