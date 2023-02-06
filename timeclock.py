import datetime
import project_list

def open_project_check():
    global open_project
    global current_project
    global last_project

    if project_list.open_project == True:
        open_project = True
        current_project = project_list.current_project
    else:
        open_project = False
        last_project = project_list.current_project

def stop_project():
    global stop_time

    confirm_stop = input("All set with " + current_project + " for the day? (y/n): \n")
    if confirm_stop == "y":

        print("Nice work on " + current_project + " today! See you next time!")
        stop_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

        with open(f"project_list.py", "w") as f:
            f.write("open_project = False \n")
            f.write("current_project = '" + current_project + "'")
            f.close()
        
        with open(f"{current_project}_time.txt", "a") as f:
            f.write("STOP: " + stop_time + "\n")
            f.close()
    else:
        print("Ok, just let me know when you're ready to take a break.")

def start_project(project):
    print("Excellent, I'll mark down the time. Let me know when you're finished.")

    start_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

    with open(f"{project}_time.txt", "a") as f:
            f.write("STAR: " + start_time + "\n")
            f.close()

    with open(f"project_list.py", "w") as f:
        f.write("open_project = True \n")
        f.write("current_project = '" + project + "'")
        f.close()
 
def main():
    open_project_check()
    if open_project == True:
        stop_project()
    else:
        continue_project_check = input("Do you want to pick up where you last left off with: " + last_project + " ? (y/n) \n")
        if continue_project_check == "y":
            start_project(last_project)
        else:
            project_to_continue = input("Which project will you be working on? \n")
            start_project(project_to_continue)


if __name__ == "__main__":
    main()