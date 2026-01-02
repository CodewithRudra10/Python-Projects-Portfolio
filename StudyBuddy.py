import datetime
import random
import os
import time

def clear_screen():
    os.system('cls' if os.name== 'nt' else 'clear')

quotes=[
"even a smaller step forward is still a progress.",
"success is not final failure is not fatal ; it's the courage to  continue that counts.",
"if things are not failing, it means you are not innovating enough.",
"You don't have to be great to start but you have to start it to be great.",
"Take risks now do something bold that you won't regret it.",
"The Harder you work for something ; the greater you will feel when you achieve it."
]


tasks=[]
notes={}
user_name=""

def get_greeting():
    current_hour= datetime.datetime.now().hour
    if current_hour < 12:
        print("Good Morning Rudra!")
    elif current_hour < 17:
        print("Good Afternoon Rudra!")
    elif current_hour < 21:
        print("Good Evening Rudra!")
    else:
        print("Good Night Rudra!")

def show_welcome():
    clear_screen()
    global user_name

    if not user_name:
        print("welcome To StudyBuddy!")
        user_name=input("what is your name").strip() .capitalize()
    if not user_name:
        user_name="Student"

greeting=get_greeting()
quote=random.choice(quotes)

print(f"Hello  {user_name} {greeting}")
print(f"Today's Thought: {quote}")
print("let's crush this day!")

input("press enter to continue")

def show_menu():
    print("/n . what would you like to do today")
    print("1.View task")
    print("2.Add New Task")
    print("3. Mark Task as Done")
    print("4. View Notes")
    print("5. Add Notes")
    print("6. Get some motivational quotes")
    print("7.Exit")

def main():
    show_welcome()
    time.sleep(1)

    while True:
        show_menu()
        choice=(input("enter your choice (1-7)")) .strip()

        if choice=="1":
            print("/n Your Tasks:")
            if tasks:
                for i, task in enumerate (tasks,1):
                    status="done" if task.get("done" ) else ""
                    print(f"{i} . {status} {task['text']}")
            else:
                print("No Tasks Yet! Add one to get started.")

        if choice=="2":
            task_text=input("enter new task:") .strip()
            if task_text:
                tasks.append({"text": task_text, "done":False})
                print("Task Added")
            else:
                print("Task cannot be Empty")

        elif choice=="3":
            if not tasks:
                print("no task to be done")
            else:
                print("your tasks")
                for i  in task in enumerate(tasks,1):
                    status="done" if task["done"] else ""
                    print(f"{i}.{status} {task['text']}")
                try:
                    idx=int(input("/n Enter task number to mark as done:"))-1
                    if 0<=idx<len(tasks):
                        tasks[idx]["done"]=True
                        print("task marked as done")
                    else:
                        print("invalid number")
                except:
                    print("Please enter a valid number")


        elif choice=="4":
            if not notes:
                print("/n no notes saved yet")
            else:
                print("/n your notes")
                for subject, note_list in notes.items():
                    print(f"/n {subject.upper()}:")
                    for note in note_list:
                        print(f":{note}")
        

        elif choice=="5":
            subject=input("enter the subject)").strip() .captalize()
            note=input(f"enter note for {subject}:").strip()
            if subject and note:
                if subject not in notes:
                    notes[subject]=[]
                    notes[subject].append(note)
                    print("note saved")
                else:
                    print("subject and note cannot be empty").capitalize()
        

        elif choice=="6":
            print(f"{random.choice(quotes)}")


        elif choice=="7":
            print("GoodBye{user_name} Keep grinding hard!")


        else:
            print("Invalid choice ; Please Try Again")

            input("/n Press Enter to continue")

if __name__=="__main__":
    main()


