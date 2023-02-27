import time
import pyautogui


# from colorama import Fore


# for user
def user():
    username = pyautogui.prompt(title="Input Box", text="Enter username")
    password = pyautogui.password(title="Input Box", text="Enter password")
    user_login_list = [username, password]
    print("\nWelcome to Sports Complex\n")
    print("Games in the sports complex are\n"
          "Cricket      '9 am to 2 pm'  900 per hour\n"
          "Football     '9 am to 2 pm'  600 per hour\n"
          "Hockey       '9 am to 2 pm'  700 per hour\n")
    count = 1
    book1 = pyautogui.prompt(title="Input Box", text="Enter the game you want to book ground ")
    if book1 == "Cricket":  # Cricket
        while count > 0:
            time_duration = pyautogui.prompt(title="Input Box", text="Enter the time duration")
            time_interval = eval(pyautogui.prompt(title="Input Box", text="Enter the time interval"))
            while time_interval < 1:
                time_interval = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                              "Enter the time_interval"))
            bats = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of bat"))
            while bats < 0:
                bats = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of bat"))
            balls = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of ball"))
            while balls < 0:
                balls = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of ball"))
            cnic = pyautogui.prompt(title="Input Box", text="Enter you cnic without dashes")
            while len(cnic) != 13:
                cnic = pyautogui.prompt(title="Input Box", text="Enter you cnic without dashes")
            date = pyautogui.prompt(title="Input Box", text="Enter the date in dd/mm/yyyy")
            price = 900 * time_interval
            issue_card = '''\n\t\t\t\t\t\t\t-----Thanks for choosing us-----
                              -----------Issue Card for Cricket---
                              Name: <|name|>
                              CNIC: <|cnic|>
                              Time: <|XYZ|>
                              Date: <|dd/mm/yyyy|>1'''
            issue_card = issue_card.replace('<|name|>', username)
            issue_card = issue_card.replace('<|cnic|>', cnic)
            issue_card = issue_card.replace('<|dd/mm/yyyy|>', date)
            issue_card = issue_card.replace('<|XYZ|>', time_duration)
            print(issue_card)
            print("\t\t\t\t\t\t\tBats:", bats)
            print("\t\t\t\t\t\t\tBall:", balls)
            print("\t\t\t\t\t\t\tPrice:", price)
            count = count - 1
        book1 = pyautogui.prompt(title="Input Box", text="Enter the game you want to book ground")
        if count == 0:
            pyautogui.alert("Sorry the ground is book. Please try again")

    count = 1
    book1 = pyautogui.prompt(title="Input Box", text="Enter the game you want to book ground")
    if book1 == "Football":  # Football
        while count > 0:
            time_duration = pyautogui.prompt(title="Input Box", text="Enter the time duration")
            time_interval = eval(pyautogui.prompt(title="Input Box", text="Enter the time interval"))
            while time_interval < 1:
                time_interval = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                              "Enter the time_interval"))
            while time_interval < 1:
                time_interval = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                              "Enter the time_interval"))
            bibs = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of bibs"))
            while bibs < 0:
                bibs = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of bibs"))
            footballs = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of football"))
            while footballs < 0:
                footballs = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of football"))
            cnic = pyautogui.prompt(title="Input Box", text="Enter you cnic without dashes")
            while len(cnic) != 13:
                cnic = pyautogui.prompt(title="Input Box", text="Enter you cnic without dashes")
            date = pyautogui.prompt(title="Input Box", text="Enter the date in dd/mm/yyyy")
            price = 600 * time_interval
            issue_card = '''\n\t\t\t\t\t\t\t-----Thanks for choosing us-----
                                      -----------Issue Card for Football---
                                      Name: <|name|>
                                      CNIC: <|cnic|>
                                      Time: <|XYZ|>
                                      Date: <|dd/mm/yyyy|>'''
            issue_card = issue_card.replace('<|name|>', username)
            issue_card = issue_card.replace('<|cnic|>', cnic)
            issue_card = issue_card.replace('<|dd/mm/yyyy|>', date)
            issue_card = issue_card.replace('<|XYZ|>', time_duration)
            print(issue_card)
            print("\t\t\t\t\t\t\tBats:", bibs)
            print("\t\t\t\t\t\t\tBall:", footballs)
            print("\t\t\t\t\t\t\tPrice:", price)
            count = count - 1
        book1 = pyautogui.prompt(title="Input Box", text="Enter the game you want to book ground")

        if count == 0:
            pyautogui.alert("Sorry the ground is book. Please try again")

    count = 1
    book1 = pyautogui.prompt(title="Input Box", text="Enter the game you want to book ground")
    if book1 == "Hockey":  # Hockey
        while count > 0:
            time_duration = pyautogui.prompt(title="Input Box", text="Enter the time duration")
            time_interval = eval(pyautogui.prompt(title="Input Box", text="Enter the time interval"))
            while time_interval < 1:
                time_interval = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                              "Enter the time_interval"))
            sticks = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of sticks"))
            while sticks < 0:
                sticks = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of sticks"))
            balls = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of balls"))
            while balls < 0:
                balls = eval(pyautogui.prompt(title="Input Box", text="Enter the amount of ball"))
            cnic = pyautogui.prompt(title="Input Box", text="Enter you cnic without dashes")
            while len(cnic) != 13:
                cnic = pyautogui.prompt(title="Input Box", text="Enter you cnic without dashes")
            date = pyautogui.prompt(title="Input Box", text="Enter the date in dd/mm/yyyy")
            price = 700 * time_interval
            issue_card = '''\n\t\t\t\t\t\t\t-----Thanks for choosing us-----
                                              -----------Issue Card for Hockey---
                                              Name: <|name|>
                                              CNIC: <|cnic|>
                                              Time: <|XYZ|>
                                              Date: <|dd/mm/yyyy|>'''
            issue_card = issue_card.replace('<|name|>', username)
            issue_card = issue_card.replace('<|cnic|>', cnic)
            issue_card = issue_card.replace('<|dd/mm/yyyy|>', date)
            issue_card = issue_card.replace('<|XYZ|>', time_duration)
            print(issue_card)
            print("\t\t\t\t\t\t\tBats:", sticks)
            print("\t\t\t\t\t\t\tBall:", balls)
            print("\t\t\t\t\t\t\tPrice:", price)
            count = count - 1
        book1 = pyautogui.prompt(title="Input Box", text="Enter the game you want to book ground")
        if count == 0:
            pyautogui.alert("Sorry the ground is book. Please try again")

    else:
        pyautogui.alert("Wrong command")


# for admin
def admin():
    game_list = []
    thing_list = []
    quantity_list = []
    time_list = []
    price_list = []

    game_list1 = []
    thing_list1 = []
    quantity_list1 = []
    time_list1 = []
    price_list1 = []

    game_list2 = []
    thing_list2 = []
    quantity_list2 = []
    time_list2 = []
    price_list2 = []

    count = 3
    fixed_username = "Ateeq"
    fixed_password = "123"
    login_list = [fixed_username, fixed_password]
    username = pyautogui.prompt(title="Input Box", text="Enter username")
    password = pyautogui.password(title="Input Box", text="Enter the password")
    while count > 0:
        if username in login_list and password in login_list:
            pyautogui.alert("Please wait")
            count = 0
            time.localtime(5)
            pyautogui.alert("Login successful")
            pyautogui.alert("Welcome")
            games = eval(pyautogui.prompt(title="Input Box", text="How many games you want in sports complex"))
            while games < 1:
                games = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0! How many games "
                                                                      "you want in sports complex"))
            for i in range(games):
                game_name = pyautogui.prompt(title="Input Box", text="Enter name of game")
                game_list.append(game_name)
                if game_name == "Cricket":
                    price = eval(pyautogui.prompt(title="Input Box", text="Enter price per hour of game"))
                    price_list.append(price)
                    timing = pyautogui.prompt(title="Input Box", text="Enter the timing of game")
                    time_list.append(timing)
                    stock = eval(
                        pyautogui.prompt(title="Input Box", text="How many stock/thing do you want in game"))
                    while stock < 1:
                        stock = eval(
                            pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                     "How many stock/thing do you want in game"))
                    for j in range(stock):
                        stock_name = pyautogui.prompt(title="Input Box", text="Enter name of stock/thing")
                        thing_list.append(stock_name)
                        stock_quantity = eval(
                            pyautogui.prompt(title="Input Box", text="Enter the quantity of stock/thing"))
                        while stock_quantity < 1:
                            stock_quantity = eval(
                                pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                         "Enter the quantity of stock/thing"))
                        quantity_list.append(stock_quantity)
                    print(game_list)
                    print(thing_list)
                    print(quantity_list)
                    print(price_list)
                    print(time_list)
                # for k in game_listi:
                #     print(game_list[index], thing_list[index], quantity_list[index], thing_list[index + 1],
                #           quantity_list[index + 1])
                #     index = index + 1
                if game_name == "Football":
                    game_list1.append("Football")
                    price = eval(pyautogui.prompt(title="Input Box", text="Enter price per hour of game"))
                    price_list1.append(price)
                    timing = pyautogui.prompt(title="Input Box", text="Enter the timing of game")
                    time_list1.append(timing)
                    stock = eval(
                        pyautogui.prompt(title="Input Box", text="How many stock/thing do you want in game"))
                    while stock < 1:
                        stock = eval(
                            pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                     "How many stock/thing do you want in game"))
                    for j in range(stock):
                        stock_name = pyautogui.prompt(title="Input Box", text="Enter name of stock/thing")
                        thing_list1.append(stock_name)
                        stock_quantity = eval(
                            pyautogui.prompt(title="Input Box", text="Enter the quantity of stock/thing"))
                        while stock_quantity < 1:
                            stock_quantity = eval(
                                pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                         "Enter the quantity of stock/thing"))
                        quantity_list1.append(stock_quantity)
                    print(game_list1)
                    print(thing_list1)
                    print(quantity_list1)
                    print(price_list1)
                    print(time_list1)

                if game_name == "Hockey":
                    game_list2.append("Hockey")
                    price = eval(pyautogui.prompt(title="Input Box", text="Enter price per hour of game"))
                    price_list2.append(price)
                    timing = pyautogui.prompt(title="Input Box", text="Enter the timing of game")
                    time_list2.append(timing)
                    stock = eval(
                        pyautogui.prompt(title="Input Box", text="How many stock/thing do you want in game"))
                    while stock < 1:
                        stock = eval(
                            pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                     "How many stock/thing do you want in game"))
                    for j in range(stock):
                        stock_name = pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                              "Enter name of stock/thing")
                        thing_list2.append(stock_name)
                        stock_quantity = eval(
                            pyautogui.prompt(title="Input Box", text="Enter the quantity of stock/thing"))
                        while stock_quantity < 1:
                            stock_quantity = eval(
                                pyautogui.prompt(title="Input Box", text="Please enter greater than 0! Enter the "
                                                                         "quantity of stock/thing"))
                        quantity_list2.append(stock_quantity)
                    print(game_list2)
                    print(thing_list2)
                    print(quantity_list2)
                    print(price_list2)
                    print(time_list2)

            check_list = pyautogui.prompt(title="Input Box", text="Do you want to update the list enter yes")
            while check_list == "Yes":
                game_name = pyautogui.prompt(title="Input Box", text="Enter the game name to update things")
                if game_name == "Cricket":
                    admin_choice = pyautogui.prompt(title="Input Box",
                                                    text="Do you update list or only check it or "
                                                         "change time or price")
                    if admin_choice == "Update":
                        choice3 = pyautogui.prompt(title="Input Box",
                                                   text="Do you want to update both or only bat or ball")
                        if choice3 == "Both":
                            print("Things")
                            print("Things", thing_list)
                            print("Stock", quantity_list)
                            bat = eval(pyautogui.prompt(title="Input Box", text="Enter the change quantity of bat"))
                            while bat < 1:
                                bat = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                    "Enter the change quantity of bat"))
                            index_bat = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                      "bat is present in list"))
                            quantity_list[index_bat] = bat
                            ball = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of ball"))
                            while ball < 1:
                                ball = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                     "Enter the change quantity of "
                                                                                     "ball"))
                            index_ball = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                       "bat is present in list"))
                            quantity_list[index_ball] = ball
                            print("Update things", quantity_list)
                            pyautogui.alert("Update Successfully")
                        elif choice3 == "Bat":
                            print("Things", thing_list)
                            print("Stock", quantity_list)
                            bat = eval(pyautogui.prompt(title="Input Box", text="Enter the change quantity of bat"))
                            while bat < 1:
                                bat = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                    "Enter the change quantity of bat"))
                            index_bat = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                      "bat is present in list"))
                            quantity_list[index_bat] = bat
                            print("New Bat quantity", quantity_list)
                            pyautogui.alert("Update Successfully")
                        elif choice3 == "Ball":
                            print("Things", thing_list)
                            print("Stock", quantity_list)
                            ball = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of ball"))
                            while ball < 1:
                                ball = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                     "Enter the change quantity of "
                                                                                     "ball"))
                            index_ball = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                       "bat is present in list"))
                            quantity_list[index_ball] = ball
                            print("New Ball quantity", quantity_list)
                            pyautogui.alert("Update Successfully")
                    elif admin_choice == "Check":
                        print("Things", thing_list)
                        print("Stock", quantity_list)
                    elif admin_choice == "Price":
                        print(price_list)
                        price = eval(pyautogui.prompt(title="Input Box", text="Enter new price per hour of game"))
                        while price < 1:
                            price = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                  "Enter the price"))
                        price_list = price
                        print("New price", price_list)
                    elif admin_choice == "Time":
                        print(time_list)
                        timing = pyautogui.prompt(title="Input Box", text="Enter the new timing of game")
                        time_list = timing
                        print("New timing", time_list)

                # Football Start
                elif game_name == "Football":
                    admin_choice = pyautogui.prompt(title="Input Box",
                                                    text="Do you update list or only check it or "
                                                         "change time or price")
                    if admin_choice == "Update":
                        choice3 = pyautogui.prompt(title="Input Box",
                                                   text="Do you want to update both or only bibs or football")
                        if choice3 == "Both":
                            print("Things")
                            print("Things", thing_list1)
                            print("Stock", quantity_list1)
                            bibs = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of bibs"))
                            while bibs < 1:
                                bibs = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                     "Enter the change quantity of "
                                                                                     "bibs"))
                            index_bib = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                      "bat is present in list"))
                            quantity_list1[index_bib] = bibs
                            football = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of ball"))
                            while football < 1:
                                football = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                         "Enter the change quantity of "
                                                                                         "football"))
                            index_ball = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                       "bat is present in list"))
                            quantity_list1[index_ball] = football
                            print("Update things", quantity_list1)
                            pyautogui.alert("Update Successfully")
                        elif choice3 == "Bibs":
                            print("Things", thing_list1)
                            print("Stock", quantity_list1)
                            bibs = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of bat"))
                            while bibs < 1:
                                bibs = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                     "Enter the change quantity of "
                                                                                     "bibs"))
                            index_bib = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                      "bat is present in list"))
                            quantity_list[index_bib] = bibs
                            print("New Bibs quantity", quantity_list1)
                            pyautogui.alert("Update Successfully")
                        elif choice3 == "Football":
                            print("Things", thing_list1)
                            print("Stock", quantity_list1)
                            football = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of ball"))
                            while football < 1:
                                football = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                         "Enter the change quantity of "
                                                                                         "football"))
                            index_ball = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                       "bat is present in list"))
                            quantity_list1[index_ball] = football
                            print("New Ball quantity", quantity_list1)
                            pyautogui.alert("Update Successfully")
                    elif admin_choice == "Check":
                        print("Things", thing_list1)
                        print("Stock", quantity_list1)
                    elif admin_choice == "Price":
                        print("Old", price_list1)
                        price = eval(pyautogui.prompt(title="Input Box", text="Enter new price per hour of game"))
                        while price < 1:
                            price = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                  "Enter the price"))
                        price_list1 = price
                        print("New price", price_list1)
                    elif admin_choice == "Time":
                        print(time_list1)
                        timing = pyautogui.prompt(title="Input Box", text="Enter the new timing of game")
                        time_list1 = timing
                        print("New timing", time_list1)
                # Hockey start
                if game_name == "Hockey":
                    admin_choice = pyautogui.prompt(title="Input Box",
                                                    text="Do you update list or only check it or "
                                                         "change time or price")
                    if admin_choice == "Update":
                        choice3 = pyautogui.prompt(title="Input Box",
                                                   text="Do you want to update both or only sticks or ball")
                        if choice3 == "Both":
                            print("Things")
                            print("Things", thing_list2)
                            print("Stock", quantity_list2)
                            sticks = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of bat"))
                            while sticks < 1:
                                sticks = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                       "Enter the change quantity "
                                                                                       "sticks"))
                            index_stick = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                        "bat is present in list"))
                            quantity_list2[index_stick] = sticks
                            ball = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of ball"))
                            while ball < 1:
                                ball = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                     "Enter the change quantity of "
                                                                                     "ball"))
                            index_ball = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                       "bat is present in list"))
                            quantity_list2[index_ball] = ball
                            print("Update things", quantity_list)
                            pyautogui.alert("Update Successfully")
                        elif choice3 == "Sticks":
                            print("Things", thing_list2)
                            print("Stock", quantity_list2)
                            sticks = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of bat"))
                            while sticks < 1:
                                sticks = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                       "Enter the change quantity of "
                                                                                       "sticks"))
                            index_stick = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                        "bat is present in list"))
                            quantity_list[index_stick] = sticks
                            print("New Bat quantity", quantity_list2)
                            pyautogui.alert("Update Successfully")
                        elif choice3 == "Ball":
                            print("Things", thing_list2)
                            print("Stock", quantity_list2)
                            ball = eval(
                                pyautogui.prompt(title="Input Box", text="Enter the change quantity of ball"))
                            while ball < 1:
                                ball = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                     "Enter the change quantity of "
                                                                                     "ball"))
                            index_ball = eval(pyautogui.prompt(title="Input Box", text="Enter the index in which "
                                                                                       "bat is present in list"))
                            quantity_list[index_ball] = ball
                            print("New Ball quantity", quantity_list2)
                            pyautogui.alert("Update Successfully")
                    elif admin_choice == "Check":
                        print("Things", thing_list2)
                        print("Stock", quantity_list2)
                    elif admin_choice == "Price":
                        print(price_list2)
                        price = eval(pyautogui.prompt(title="Input Box", text="Enter new price per hour of game"))
                        while price < 1:
                            price = eval(pyautogui.prompt(title="Input Box", text="Please enter greater than 0!"
                                                                                  "Enter the price"))
                        price_list2 = price
                        print("New price", price_list2)
                    elif admin_choice == "Time":
                        print(time_list2)
                        timing = pyautogui.prompt(title="Input Box", text="Enter the new timing of game")
                        time_list2 = timing
                        print("New timing", time_list2)

                check_list = pyautogui.prompt(title="Input Box", text="Do you want to update the list enter yes")
                if check_list == "No":
                    pyautogui.alert("Thanks for cooperating with us")
        else:
            pyautogui.alert("Wrong")
            count = count - 1
            print("You have %d chances left" % count)
            if count == 0:
                print("No chance left")
                break
            username = pyautogui.prompt(title="Input Box", text="Enter username")


if __name__ == "__main__":
    choice = pyautogui.prompt(title="Input Box", text="Enter the choice whether user or admin")
    if choice == "user":
        user()
    if choice == "admin":
        admin()
    if choice != "user" or choice != "admin":
        pyautogui.alert("Wrong command")
        exit()
