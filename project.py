from controller import Controller
from database import Database

#app and router in the same level

def main():
    running = True
    csv_path = './database.csv'
    database = Database(csv_path)
    controller = Controller(database)
    run(controller)


def run(controller):
    running = True
    while running:
        action = actions()
        if action == 8:
            running = False
        else:
            router(action, controller)



def actions():
    print("Choose a valid option:")
    print("\n")
    print("1 - See All Movies")
    print("2 - Add a Movie")
    print("3 - Delete a Movie")
    print("4 - Mark a Movie As Seen")
    print("5 - Rate a Movie")
    print("6 - Find A Movie Online")
    print("7 - Export Your List As a PDF File")
    print("8 - Quit The Program")
    print("Please type 1, 2, 3, 4, 5, 6, 7, or 8 \n")
    choice = int(input("Action: "))
    print("\n")
    return choice

def router(action, controller):
    match action:
        case 1:
            controller.list()
        case 2:
            controller.add_movie()
        case 3:
            controller.delete_movie()
        case 4:
            controller.mark_as_seen()
        case 5:
            controller.rate_movie()
        case 6:
            controller.find_movie_online()
        case 7:
            controller.export_list()
        case _:
            print("Invalid option, please type a valid option")


if __name__ == "__main__":
    main()
