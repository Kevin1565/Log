def menu():
    print('-'*20, 'DB Logging Menu','-'*20)
    print(' [1] Session\n [2] Time\n [3] Excuse\n [4] Exit')

def get_Menu_Selection():
    options = ['1', '2', '3', '4']
    selection = input('Select log type: ')
    while selection not in options:
        selection = input('Select log type: ')
    return selection

def sessions():
    active = True
    while active == True:
        options = ['1', '2', '3']
        print('-'*20,'SESSIONS','-'*20)
        print(' [1] View\n','[2] Add\n', '[3] Exit')
        selection = input('Enter the number of your task: ')
        while selection not in options:
            selection = input('Enter the number of your task: ')
        if selection == '1':
            user = input('Enter the username: ')
            f = open("Sessions.txt", "r")
            lines = f.readlines()
            f.close()
            found = False
            for lines in lines:
                if lines.find(user) != -1:
                    found = True
                    sessions = 0
                    for ch in lines:
                        if ch == '|':
                            sessions += 1
                    print("{0} has {1} sessions.".format(user, sessions))
            if not found:
                print("User not found.")
            
        if selection == '2':
            f = open("Sessions.txt", "r")
            lines = f.readlines()
            f.close()
            user = input('Enter the username: ')
            f = open("Sessions.txt", "a")
            added = False
            for lines in lines:
                if user in lines:
                    added = True
                    f.write(' |')
            if added == False:
                    f.write(('\n{0} |'.format(user)))
            f.close()
        
        elif selection == '3':
            print('Exiting to menu.')
            print()
            
    


def excused():
    active = True
    while active == True:
        options = ['1', '2', '3', '4']
        print('-'*20,'EXCUSED','-'*20)
        print(' [1] View\n','[2] Add\n', '[3] Remove\n [4] Exit')
        selection = input('Enter the number of your task: ')
        while selection not in options:
            selection = input('Enter the number of your task: ')
        if selection == '1':
            f = open("Excused List.txt", "r")
            lines = f.readlines()
            names = []
            for line in lines:
                names.append(line.replace('\n', ''))
            f.close()
            print(names)
        elif selection == '2': 
            f = open("Excused List.txt", "a")
            f.write(input('Enter the username: ') + '\n')
            f.close()
        elif selection == '3':
            f = open("Excused List.txt", "r")
            lines = f.readlines()
            f.close()
            user = input('Enter the username: ')
            f = open("Excused List.txt", "w")
            for line in lines:
                if line != (user + '\n'):
                    f.write(line)
            f.close()
        else:
            active = False

def main():
    menu()
    selection = get_Menu_Selection()
    if selection == '1':
        sessions()
    elif selection == '2':
        pass
    elif selection == '3':
        excused()
    else:
        pass
main()
