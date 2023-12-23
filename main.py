from array import array

def Mars() -> None:
    """Марсоход."""
    robots: array[int] = [int(x) for x in input().split(' ')] 
    limit = int(input())
    pos_max: int = 0 #Позиция самого большого числа в массиве.
    pos_min: int = len(robots) - 1 #Позиция самого минимального числа в массиве.
    robots.sort(reverse=True) 
    while robots[pos_max] > limit or pos_max == pos_min + 1:
        #Перенос позиции самого большого в рамки предела
        pos_max += 1
    count: int = 0
    while pos_max != pos_min and pos_min > pos_max:
        if (robots[pos_max] + robots[pos_min]) <= limit:
            pos_min -= 1
        pos_max += 1
        count += 1
    if pos_min == pos_max:       
        count += 1         
    print(count)

if __name__ == '__main__':
    Mars()
