from array import array

def mars_roverars(robot, limmits) -> int:
    """Марсоход."""
    pos_max: int = 0 #Позиция самого большого числа в массиве.
    pos_min: int = len(robot) - 1 #Позиция самого минимального числа в массиве.
    robot.sort(reverse=True) 
    count: int = 0
    while pos_max <= pos_min and pos_min > pos_max:
        if (robot[pos_max] + robot[pos_min]) <= limmits:
            pos_min -= 1
        pos_max += 1
        count += 1
    if pos_min == pos_max:       
        count += 1         
    return count

robots: array = [int(x) for x in input().split(' ')]
limit = int(input())
print(mars_roverars(robots, limit))
if __name__ == '__main__':
    mars_roverars(robots, limit)
