from a_star import AStar
import time

astar = AStar()
i = 0
while i < 10:
    astar.motors(i * 20, i * 20)
    print(astar.read_encoders())
    i += 1
    time.sleep(0.5)

astar.motors(100, 0)
time.sleep(2)
print(f"Left: {astar.read_encoders()}")

astar.motors(0, 100)
time.sleep(2)
print(f"Right: {astar.read_encoders()}")

astar.motors(0, 0)