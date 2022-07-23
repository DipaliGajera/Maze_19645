from typing import List

class Solution:
    def DFS(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        direction = [(1,0), (-1,0), (0,-1), (0,1)]
        m = len(maze)
        n = len(maze[0])

        stack = []
        seen = set()

        stack.append((start[0], start[1]))
        seen.add((start[0], start[1]))

        while stack:
            cur_i, cur_j = stack.pop()

            for d in direction:
                i = cur_i
                j = cur_j

                while 0 <= i < m and 0 <= j < n and maze[i][j] == 0:
                    i += d[0]
                    j += d[1]

                i -= d[0]
                j -= d[1]

                if i ==destination[0] and j == destination[1]:
                    return True

                if (i, j) not in seen:
                    stack.append((i,j))
                    seen.add((i, j))
                   
        return False

def main():
    obj = Solution()
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
    result = obj.DFS(maze, destination, starting_position)
    print("------------------------------------")
    print("The Maze output will be :-", '"', result, '"')
    print("------------------------------------")

if __name__ == '__main__':
    main()
