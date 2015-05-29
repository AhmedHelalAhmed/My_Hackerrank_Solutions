class Node:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def dist(self,target):
        return abs(target.x - self.x) + abs(target.y - self.y)
def nxmv(posx, posy, board):

    bot_node = Node(posy, posx)
    dirty_nodes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                dirty_nodes.append(Node(j,i))
    near = None
    for node in dirty_nodes:
        if near is None or node.dist(bot_node) < near.dist(bot_node):
            near = node
    if near is not None:
        print_move(near.x - bot_node.x, near.y - bot_node.y)
def print_move(delta_x,delta_y):
    if delta_x < 0:
        print('LEFT')
    elif delta_x > 0:
        print('RIGHT')
    elif delta_y < 0:
        print('UP')
    elif delta_y > 0:
        print('DOWN')
    else:
        print('CLEAN')
if __name__ == '__main__':
    x,y = map(int,input().split())
    board = [[j for j in input().strip()] for i in range(5)]
    nxmv(x,y,board)
