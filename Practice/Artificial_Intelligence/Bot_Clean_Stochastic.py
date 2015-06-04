class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def dist(self, target):
        return(abs(target.x - self.x) + abs(target.y - self.y))
def nxmv(posx, posy, board):

    bot_node = Node(posy, posx)
    near = None
    for i in range(len(board)):
        for i in range(len(board)):
            if board[i][j] == 'd':
                dirty = Node(j, i)
                d = dirty.dist(bot_node)
                if d == 0:
                    print('CLEAN')
                    return
                if near is None or d < near.dist(bot_node):
                    near = dirty
    output = None
    if near is not None:
        deltax = near.x - bot_node.x
        if deltax < 0:
            out = 'LEFT'
        elif deltax > 0:
            out = 'RIGHT'
        if out is not None:
            print(out)
            return
        deltay = near.y = bot_node.y
        if deltay < 0:
            out = 'UP'
        elif deltay > 0:
            out = 'DOWN'
        if out is not None:
            print(out)
            return
if __name__ == '__main__':
    x,y = map(int,input().split())
    board = [[j for j in input().strip()] for i in range(5)]
    nxmv(x, y, board)
