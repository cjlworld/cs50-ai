"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None

INF = 1024

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt = sum([1 for i in range(3) for j in range(3) if board[i][j] is not None])
    # print(f"cnt = {cnt}")
    if cnt % 2 == 0:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    res = copy.deepcopy(board)
    res[action[0]][action[1]] = player(board)
    return res

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 有 winner 返回 winner，否则返回 None
    if not terminal(board):
        return None
    state = utility(board)
    if state == 0:
        return None
    elif state == 1:
        return X
    else:
        return O
    raise NotImplementedError


# 结束判断
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # 横向, 竖向
    for i in range(3):
        # 横向
        if board[i][0] is not None and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return True
        # 竖向
        if board[0][i] is not None and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True

    # 斜向
    if board[0][0] is not None and board[1][1] == board[0][0] and board[2][2] == board[0][0]:
        return True
    if board[0][2] is not None and board[1][1] == board[0][2] and board[2][0] == board[0][2]:
        return True

    # 还有的下
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return False
    
    # 下满了
    return True
    raise NotImplementedError

# 分数判断
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return 1
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return -1
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return 1
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return -1
    
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return 1
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return -1
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return 1
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return -1
    
    # 平局
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if len(actions(board)) == 9:
        return (random.randint(0, 2), random.randint(0, 2))
    action = MiniMAX(board, INF if player(board) == X else -INF)[1]
    return action

    raise NotImplementedError

# 返回具有必胜策略的分数
def MiniMAX(board, father_value): 
    """
    father 表示该层的父层已有的分数

    return (value, action) 
        action 表示该层取得 value 的对应下一步策略
    """

    if terminal(board):
        return (utility(board), None)

    # X 行动
    if player(board) == X: 
        value = -INF
        optimalAction = (0, 0)
        for action in actions(board):
            child = MiniMAX(result(board, action), value)
            if child[0] > value or (child[0] == value and random.randint(1, 3) == 1):
                value = child[0]
                optimalAction = action
            if value > father_value: # alpha-beta 剪枝
                return (value, optimalAction)
    # O 行动
    else: 
        value = INF
        optimalAction = (0, 0)
        for action in actions(board):
            child = MiniMAX(result(board, action), value)

            if child[0] < value or (child[0] == value and random.randint(1, 3) == 1):
                value = child[0]
                optimalAction = action
            # alpha-beta 剪枝
            if value < father_value: 
                return (value, optimalAction)
    
    return (value, optimalAction)

