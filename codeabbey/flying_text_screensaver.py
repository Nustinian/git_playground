def toggle(direction):
    if direction == 1:
        return -1
    if direction == -1:
        return 1

nums = [int(x) for x in input().split()]
width, height, length = nums[0], nums[1], nums[2]

horizontal_switch = width - length
vertical_switch = height - 1
coordinates = [0, 0]
forward = 1
down = 1
for i in range(101):
    print(" ".join(map(str, coordinates)), " ")
    coordinates[0] += forward
    coordinates[1] += down
    if (i + 1) % vertical_switch == 0:
        down = toggle(down)
    if (i + 1) % horizontal_switch == 0:
        forward = toggle(forward)

