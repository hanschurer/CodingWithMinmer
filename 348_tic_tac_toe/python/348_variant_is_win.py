from typing import List

def is_win_348_variant(board: List[List[int]], player: int, row: int, col: int) -> bool:
    """
    井字棋变种：判断在指定位置下棋后是否获胜
    
    Args:
        board: 井字棋棋盘，0表示空位，1表示玩家1，2表示玩家2
        player: 当前玩家（1或2）
        row: 要下棋的行
        col: 要下棋的列
        
    Returns:
        如果下棋后获胜返回True，否则返回False
    """
    # 在指定位置下棋
    board[row][col] = player
    
    n = len(board)
    rows = 0      # 行计数
    cols = 0      # 列计数
    diagonal = 0      # 主对角线计数
    anti_diagonal = 0 # 反对角线计数
    
    # 检查所有可能的获胜线
    for i in range(n):
        # 检查行
        if board[row][i] == player:
            rows += 1
        
        # 检查列
        if board[i][col] == player:
            cols += 1
        
        # 检查主对角线
        if board[i][i] == player:
            diagonal += 1
        
        # 检查反对角线
        if board[i][n - 1 - i] == player:
            anti_diagonal += 1
    
    # 如果任何一条线被完全占据，则获胜
    return rows == n or cols == n or diagonal == n or anti_diagonal == n

# 测试函数
def test_tic_tac_toe_win():
    """测试井字棋获胜判断"""
    
    # 测试用例1：行获胜
    board1 = [
        [1, 1, 0],
        [2, 2, 0],
        [0, 0, 0]
    ]
    print("测试用例1 - 行获胜:")
    print("棋盘:")
    for row in board1:
        print(f"  {row}")
    result = is_win_348_variant(board1, 1, 0, 2)  # 在(0,2)位置下棋
    print(f"玩家1在(0,2)下棋后获胜: {result}")
    assert result == True
    print("✓ 测试通过\n")
    
    # 测试用例2：列获胜
    board2 = [
        [1, 2, 0],
        [1, 2, 0],
        [0, 0, 0]
    ]
    print("测试用例2 - 列获胜:")
    print("棋盘:")
    for row in board2:
        print(f"  {row}")
    result = is_win_348_variant(board2, 1, 2, 0)  # 在(2,0)位置下棋
    print(f"玩家1在(2,0)下棋后获胜: {result}")
    assert result == True
    print("✓ 测试通过\n")
    
    # 测试用例3：主对角线获胜
    board3 = [
        [1, 2, 0],
        [2, 1, 0],
        [0, 0, 0]
    ]
    print("测试用例3 - 主对角线获胜:")
    print("棋盘:")
    for row in board3:
        print(f"  {row}")
    result = is_win_348_variant(board3, 1, 2, 2)  # 在(2,2)位置下棋
    print(f"玩家1在(2,2)下棋后获胜: {result}")
    assert result == True
    print("✓ 测试通过\n")
    
    # 测试用例4：反对角线获胜
    board4 = [
        [0, 2, 1],
        [2, 1, 0],
        [0, 0, 0]
    ]
    print("测试用例4 - 反对角线获胜:")
    print("棋盘:")
    for row in board4:
        print(f"  {row}")
    result = is_win_348_variant(board4, 1, 2, 0)  # 在(2,0)位置下棋
    print(f"玩家1在(2,0)下棋后获胜: {result}")
    assert result == True
    print("✓ 测试通过\n")
    
    # 测试用例5：不获胜
    board5 = [
        [1, 2, 0],
        [2, 0, 1],
        [0, 1, 2]
    ]
    print("测试用例5 - 不获胜:")
    print("棋盘:")
    for row in board5:
        print(f"  {row}")
    result = is_win_348_variant(board5, 1, 1, 1)  # 在(1,1)位置下棋
    print(f"玩家1在(1,1)下棋后获胜: {result}")
    assert result == False
    print("✓ 测试通过\n")
    
    # 测试用例6：4x4棋盘
    board6 = [
        [1, 2, 0, 0],
        [2, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print("测试用例6 - 4x4棋盘:")
    print("棋盘:")
    for row in board6:
        print(f"  {row}")
    result = is_win_348_variant(board6, 1, 2, 2)  # 在(2,2)位置下棋
    print(f"玩家1在(2,2)下棋后获胜: {result}")
    assert result == False  # 4x4需要4个连续才能获胜
    print("✓ 测试通过\n")
    
    print("所有测试通过!")

# 可视化函数
def print_board_with_move(board: List[List[int]], player: int, row: int, col: int):
    """可视化棋盘和下棋位置"""
    print(f"玩家{player}在位置({row}, {col})下棋:")
    for i, row_board in enumerate(board):
        row_str = "  "
        for j, cell in enumerate(row_board):
            if i == row and j == col:
                row_str += f"[{cell}]"  # 标记下棋位置
            else:
                row_str += f" {cell} "
        print(row_str)
    
    result = is_win_348_variant(board, player, row, col)
    print(f"结果: {'获胜!' if result else '未获胜'}")

if __name__ == "__main__":
    # 运行测试
    test_tic_tac_toe_win()
    
    # 演示可视化
    print("\n=== 可视化演示 ===")
    demo_board = [
        [1, 2, 0],
        [2, 1, 0],
        [0, 0, 0]
    ]
    print_board_with_move(demo_board, 1, 2, 2) 