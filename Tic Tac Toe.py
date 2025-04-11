#틱텍토 게임
import random   #컴퓨터가 랜덤한 위치에 놓기해에 사용

#현재 보드 상태 출력
def print_board(board):
    print("\n현재 보드 상태:")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print()
# 가로, 세로, 대각선 승리 조건 체크
def check_winner(board, player):
    winning_combinations = [#이기는 조건 체크
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로 
        [0, 4, 8], [2, 4, 6]  # 대각선
    ]
    #이기는 조건 체크
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

#보드가 꽉찼는지 체크
def is_board_full(board):
    return ' ' not in board

#컴퓨터가 랜덤한 위치에 놓기
def get_computer_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(empty_spots)

#게임 시작
def play_game():
    board = [' '] * 9
    print("\n=== 틱텍토 게임 시작 ===")
    print("위치는 1-9까지의 숫자로 선택하세요:")    #x와y값의 위치를 받지않고 보드판에 번호를 부여하여 좀 더 입력받기 편하게함함
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\n당신은 'X', 컴퓨터는 'O'입니다.")
    
    while True:
        # 사용자 턴
        print_board(board)
        while True:
            try:
                move = int(input("당신의 차례입니다. 위치를 선택하세요 (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("잘못된 위치입니다. 다시 선택하세요.")
            except ValueError:
                print("1부터 9까지의 숫자를 입력하세요.")
        
        # 사용자 승리 체크
        if check_winner(board, 'X'):
            print_board(board)
            print("축하합니다! 당신이 이겼습니다!")
            break
            
        # 무승부 체크
        if is_board_full(board):
            print_board(board)
            print("무승부입니다!")
            break
            
        # 컴퓨터 턴
        print("\n컴퓨터 차례...")
        computer_move = get_computer_move(board)
        board[computer_move] = 'O'
        print(f"컴퓨터가 {computer_move + 1} 위치를 선택했습니다.")
        
        # 컴퓨터 승리 체크
        if check_winner(board, 'O'):
            print_board(board)
            print("컴퓨터가 이겼습니다!")
            break
            
        # 무승부 체크
        if is_board_full(board):
            print_board(board)
            print("무승부입니다!")
            break

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\n다시 플레이하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            print("게임을 종료합니다. 감사합니다!")
            break

#claude 3.5 sonnet를 참고하여 코드를 작성하였습니다.