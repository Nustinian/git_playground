import math

def time_parser(time):
    hour = int(time.split(':')[0])
    if hour > 12:
        hour -= 12
    minute = int(time.split(':')[1])
    minute_hand_radians = math.pi * minute / 30
    hour_hand_radians = math.pi * hour / 6 + math.pi * minute / 360
    return minute_hand_radians, hour_hand_radians

def coordinate_calculator(radians, length):
    coordinates = [10, 10]
    coordinates[0] += math.sin(radians) * length
    coordinates[1] += math.cos(radians) * length
    print(str(coordinates[0]), " ", str(coordinates[1]), " ")

counter = int(input())
times = input().split()
for time in times:
    minute_hand_radians, hour_hand_radians = time_parser(time)
    coordinate_calculator(hour_hand_radians, 6)
    coordinate_calculator(minute_hand_radians, 9)

