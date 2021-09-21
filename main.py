import turtle
import random

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.title("Elevator Model")

#create the user positions and floor positions
positions = [(-100, -210), (-100, -140), (-100, -70), (-100, 0), (-100, 70),(-100, 140), (-100, 210)]
floor_positions = [(50, -210), (50, -140), (50, -70), (50, 0), (50, 70) ,(50, 140), (50, 210)]

#customizing the object characteristics
elevator = turtle.Turtle()
floor = turtle.Turtle()
remover = turtle.Turtle()
move = turtle.Turtle()
user = turtle.Turtle()
user.color("white")
user.shape('circle')
remover.shape("circle")
remover.color("black")
move.shape("circle")
move.color("blue")
user_positions = [(50, -200), (50, -130), (50, -60), (50, 10), (50, 80) ,(50, 150), (50, 220)]


#visualizes the elevator object
def draw_elevator(elevator):
    elevator.color('white')
    for pos in positions:
        elevator.penup()
        elevator.setpos(pos)
        elevator.pendown()
        for i in range(2):
            elevator.forward(25)
            elevator.left(90)
            elevator.forward(60)
            elevator.left(90)
        elevator.penup()
    return elevator


#visualizes the floor objects
def draw_floors(floor):
    floor.color('white')
    for floor_pos in floor_positions:
        floor.penup()
        floor.setpos(floor_pos)
        floor.pendown()
        for i in range(2):
            floor.forward(95)

        floor.penup()
    return floor


#creates the randomized users and assigns them to a position on the floor objects
#returns a list of the users'positions
def random_users():
    level_of_busy = ["not busy", "not busy", "fairly busy", "very busy"]
    level = random.choice(level_of_busy)
    if level == "not busy":
        no_of_users = random.randint(0, 5)
    elif level == "fairly busy":
        no_of_users = random.randint(6, 15)
    elif level == "very busy":
        no_of_users = random.randint(16, 21)

    new_pos = []
    user_pos = []
    for start in range(no_of_users):
        user.penup()
        position = random.choice(user_positions)
        if position not in new_pos:
            new_pos.append(position)
            user_pos.append(position)
        else:
            no_of_times = new_pos.count(position)
            new_pos.append(position)
            position_x = position[0] + 25 * no_of_times
            position_y = position[1]
            position = (position_x, position_y)
            new_pos.append(position)
            user_pos.append(position)

        user.setpos(position)
        user.pendown()
        user.stamp()
    return user_pos
#assigns the users'position to a variable
position_list = random_users()

#returns the number of users on a particular floor in a list
def users_per_floor(position_list):
    floor1 = 0
    floor2 = 0
    floor3 = 0
    floor4 = 0
    floor5 = 0
    floor6 = 0
    floor7 = 0
    #[(50, -200), (50, -130), (50, -60), (50, 10), (50, 80) ,(50, 150), (50, 220)]
    for i in position_list:
        position_y = i[1]
        if position_y >= -200 and position_y < -130:
            floor1 += 1
        elif position_y >= -130 and position_y < -60:
            floor2 += 1
        elif position_y >= -60 and position_y < 10:
            floor3 += 1
        elif position_y >= 10 and position_y < 80:
            floor4 += 1
        elif position_y >= 80 and position_y < 150:
            floor5 += 1
        elif position_y >= 150 and position_y < 220:
            floor6 += 1
        elif position_y >= 220:
            floor7 +=1
    return [floor1, floor2, floor3, floor4, floor5, floor6, floor7]

floor_sum_list= users_per_floor(position_list)


#moves the users to their destinations
destination_list = []
def move_to_destination():
    destination = random.randint(1, 7)
    # [(50, -200), (50, -130), (50, -60), (50, 10), (50, 80) ,(50, 150), (50, 220)]
    if destination == 1:
        if 1 not in destination_list:
            destination_list.append(1)
            position_x = -120
            position_y = -200
        else:
            position_x = -120 - 25* (destination_list.count(1))
            position_y = -200
            destination_list.append(1)
        position = (position_x, position_y)

    if destination == 2:
        if 2 not in destination_list:
            destination_list.append(2)
            position_x = -120
            position_y = -130
        else:
            position_x = -120 - 25* (destination_list.count(1))
            position_y = -130
            destination_list.append(2)
        position = (position_x, position_y)

    if destination == 3:
        if 3 not in destination_list:
            destination_list.append(3)
            position_x = -120
            position_y = -60
        else:
            position_x = -120 - 25* (destination_list.count(3))
            position_y = -60
            destination_list.append(3)
        position = (position_x, position_y)

    if destination == 4:
        if 4 not in destination_list:
            destination_list.append(4)
            position_x = -120
            position_y = 10
        else:
            position_x = -120 - 25* (destination_list.count(4))
            position_y = 10
            destination_list.append(4)
        position = (position_x, position_y)

    if destination == 5:
        if 1 not in destination_list:
            destination_list.append(5)
            position_x = -120
            position_y = 80
        else:
            position_x = -120 - 25* (destination_list.count(5))
            position_y = 80
            destination_list.append(5)
        position = (position_x, position_y)

    if destination == 6:
        if 6 not in destination_list:
            destination_list.append(6)
            position_x = -120
            position_y = 150
        else:
            position_x = -120 - 25* (destination_list.count(6))
            position_y = 150
            destination_list.append(6)
        position = (position_x, position_y)

    if destination == 7:
        if 7 not in destination_list:
            destination_list.append(7)
            position_x = -120
            position_y = 220
        else:
            position_x = -120 - 25* (destination_list.count(7))
            position_y = 220
            destination_list.append(7)
        position = (position_x, position_y)

    move.penup()
    move.setpos(position)
    move.pendown()
    move.stamp()
    print(destination_list)




#removes the users from their initial floors
def remove_user(position_list):
    iteration = 0
    counter = 0
    for i in position_list:
        position_x = i[0]
        position_y = i[1]
        position = (position_x, position_y)
        remover.penup()
        remover.setpos(position)
        remover.pendown()
        remover.stamp()
        move_to_destination()
        iteration +=1

draw_elevator(elevator)

draw_floors(floor)
remove_user( position_list)
wn.exitonclick()

