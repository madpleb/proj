from a_star import AStar
import time

astar = AStar()

starting_left = 200
start_right = 200 
left_speed = starting_left
right_speed = start_right

left_sum = 0
right_sum = 0

def slow_stop(start_speed): 
    i = start_speed
    while i > 0:
        i = i - 10
        astar.motors(i, i)
        time.sleep(0.2)

def adjust_speed():
    global left_speed
    global right_speed
    global starting_left
    global start_right

    if (left_sum - right_sum > 2):
        print("\t Adjusted left motor")
        left_speed = left_speed - 2
        astar.motors(left_speed, right_speed)
    elif (right_sum - left_sum  > 2):        
        print("\t Adjusted right motor")
        right_speed = right_speed - 2
        astar.motors(left_speed, right_speed)
    else:
        print("\t Motors are fine")
        # astar.motors(left_speed, right_speed)

    if starting_left - left_speed > 8:
        left_speed = left_speed + 10
        right_speed = right_speed + 10
        astar.motors(left_speed, right_speed)
    


astar.motors(left_speed, right_speed)


i = 0
while i <= 150:
    encoders = astar.read_encoders()
    print(f"Encoders: {encoders}")

    left_sum += encoders[0]
    right_sum += encoders[1]
    print(f"Total left: {left_sum}")
    print(f"Total right: {right_sum}")

    # adjust_speed()

    i += 1
    time.sleep(0.1)


print(f"Left speed: {left_speed}")
print(f"Right speed: {right_speed}")

# astar.motors(100, 0)
# time.sleep(2)
# print(f"Left: {astar.read_encoders()}")

# astar.motors(0, 100)
# time.sleep(2)
# print(f"Right: {astar.read_encoders()}")

slow_stop(100)