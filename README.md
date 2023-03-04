# timeclock
A python CLI tool to easily track time spent on various projects
By running this script from the CLI (I built this specifically for use in linux terminal), the program will prompt the user to either select a new project or an existing project to begin working on. New project will always be option 0, each subsequent project will be given an incremented number so that it is easy to choose a project from the list. 
The program will then write in a file for the named project the START time of the project. The script will identify if there is already a project "opened", and instead of prompting the user to select from the list of projects, will simply ask the user to confirm that they are finished working on the current project. Once confirmed, the program will then write in the file the STOP time of the project. 
Currently this only records the data. Future plans to expand on this to be able to analyze the data. 
