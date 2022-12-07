def bfs(src, target):
    queue = []
    queue.append(src)

    frontier = []
    while len(queue) > 0:  
        source = queue.pop(0)
        frontier.append(source)
        print(source)
        if source == target:
            print("success")
            return
        pos_moves = []
        pos_moves = possible_moves(source, frontier)
        for moves in pos_moves:
            if moves not in frontier and moves not in queue:
                queue.append(moves)


def gen(source, dir, b):
 
    new_state = source.copy()
    if dir == 'd':
        new_state[b + 3], new_state[b] = new_state[b], new_state[b + 3]
    if dir == 'u':
        new_state[b - 3], new_state[b] = new_state[b], new_state[b - 3]
    if dir == 'r':
        new_state[b + 1], new_state[b] = new_state[b], new_state[b + 1]
    if dir == 'l':
        new_state[b - 1], new_state[b] = new_state[b], new_state[b - 1]
    return new_state


def possible_moves(source, explored):
    direction = []  
    b = source.index(X)
    if b not in [0, 1, 2]:
        direction.append('u')
    if b not in [6, 7, 8]:
        direction.append('d')
    if b not in [0, 3, 6]:
        direction.append('l')
    if b not in [2, 5, 8]:
        direction.append('r')

    possible_states = []
    for dir in direction:
        possible_states.append(gen(source, dir, b))

    return [un_move for un_move in possible_states if un_move not in explored]


src = []
goal = []
print("Enter the source 8 puzzle as single dimension list : \nEnter X for blank")
for i in range(1,10):
     src.append(input())
print("source:")
print(src)
print("Enter the goal 8 puzzle as single dimension list : \nEnter X for blank")
for i in range(1,10):
    goal.append(input())
print("goal:",goal,"\n")
print("Possible moves :")
bfs(src, goal)  