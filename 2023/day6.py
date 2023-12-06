day6_example = {7: 9,
                15: 40,
                30: 200}

day6_input = {55: 401,
              99: 1485,
              97: 2274,
              93:1405}

import math

def win_range(time, distance):
    min_speed = math.ceil(distance / time)

    if min_speed >= time:
        return 0
    else:
        min_hold = min_speed
        max_hold = time

        while (min_hold * (time - min_hold)) <= distance:
            min_hold += 1

        while (max_hold * (time - max_hold)) <= distance:
            max_hold -= 1

        return max_hold - min_hold + 1 


# Part 1
print(math.prod([win_range(k,v) for k,v in day6_input.items()]))
# 2374848

# Part 2
print(win_range(55999793,401148522741405))
# 39132886

