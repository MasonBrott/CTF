import itertools

time_limit = 401
player_dict = {}
num = 1
order = []

players = """Person 1 will take 29 minutes to cross the bridge.
Person 2 will take 3 minutes to cross the bridge.
Person 3 will take 38 minutes to cross the bridge.
Person 4 will take 9 minutes to cross the bridge.
Person 5 will take 72 minutes to cross the bridge.
Person 6 will take 11 minutes to cross the bridge.
Person 7 will take 97 minutes to cross the bridge.
"""
players = players.split(".")

for player in players:
    player = player.split(" ")
    if num < len(players):
        player_dict[int(player[1])] = int(player[4])
        num += 1

fast_dict = dict(sorted(player_dict.items(), key=lambda item: item[1]))
start_dict = fast_dict
end_dict = {}
two_fastest = dict(itertools.islice(fast_dict.items(), 2))


def start_side():
    global start_dict
    global end_dict
    global order
    start_dict = dict(sorted(start_dict.items(), key=lambda item: item[1]))
    
    if len(start_dict) >= 2:
        # If two fastest people are present in starting side send them to far side
        if set(two_fastest.items()).issubset(set(start_dict.items())):
            # Remove two fastest people from start_dict
            start_dict.pop(list(two_fastest.keys())[0])
            start_dict.pop(list(two_fastest.keys())[1])
            # Add the two moved to end_dict
            end_dict.update(two_fastest)
            # Add the two people sent over to the order
            order.append(list(two_fastest.keys()))
            far_side()
        else:
            #Send the two slowest people
            slowest = dict(itertools.islice(start_dict.items(), len(start_dict) - 2, len(start_dict)))
            start_dict.pop(list(slowest.keys())[-1])
            start_dict.pop(list(slowest.keys())[-2])
            end_dict.update(slowest)
            order.append(list(slowest.keys()))

            far_side()

    
def far_side():
    global start_dict
    global end_dict
    global order
    if len(start_dict) > 0:
        end_dict = dict(sorted(end_dict.items(), key=lambda item: item[1]))
        fastest = dict(itertools.islice(end_dict.items(), 1))
        end_dict.pop(list(fastest.keys())[0])
        start_dict.update(fastest)
        order.append(list(fastest.keys()))

    start_side()

start_side()

# print(start_dict)
# print(end_dict)
# print(order)
print(order)