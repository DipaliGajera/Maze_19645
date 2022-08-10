import collections

def findPathBfs(maze, start, destination):
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = collections.deque([(start [0], start [1])])
    while queue:
        x, y = queue.popleft()
        
        if x == destination[0] and y == destination[1]:
            return True
        
        for dx, dy in dirs:
            nx = x
            ny = y
            
        while 0 <= nx + dx < len (maze) and 0 <= ny + dy < len(maze [0]) and maze[nx + dx] [ny + dy] != 1:
            nx += dx 
            ny += dy

        if maze [nx] [ny] != 0:
            continue

        maze [nx] [ny] = 2
        queue.append( (nx, ny))
    return False

def main():
    maze = []
    val = int(input("How many array do you want to enter : "))

    for i in range(0,val):
        arr = []
        n = int(input("How many elements do you want to enter : "))
        for j in range(0, n):
            ele = int(input("Enter array values : "))
            arr.append(ele)
        maze.append(arr)

    print()
    val = 2
    destination = []
    starting_position = []
    for k in range(0,val):
        pos = int(input("Enter the start position : "))
        destination.append(pos)

    print()
    for d in range(0,val):
        pos = int(input("Enter the position for Destination : "))
        starting_position.append(pos)

    print()
    result = findPathBfs(maze, destination, starting_position)
    print("------------------------------------")
    print("The Maze output will be :-", '"', result, '"')
    print("------------------------------------")

if __name__ == '__main__':
    main()