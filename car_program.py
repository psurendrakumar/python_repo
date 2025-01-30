car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already started!")
        else:
            car_started = True
            print("car started")
    elif command == "stop":
        if not car_started:
            print("Car is already stopped!")
        else:
            car_started = False
            print("car stoped")
    elif command == "help":
        print("""
    start - To start the car
    stop - To stop the car
    quit - To exit
        """)
    elif command == "quit":
        break
    else:
        print("sorry i don't understand that")