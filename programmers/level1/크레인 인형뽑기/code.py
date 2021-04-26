def solution(board, moves):
    answer = 0
    matrix_size = len(board[0])
    v_s = []
    v_s_p = -1

    for i in moves:
        for k in range(matrix_size):
            if board[k][i-1] != 0:
                value = board[k][i-1]
                board[k][i-1] = 0
                if v_s_p != -1 and v_s[v_s_p] == value:
                    v_s.pop()
                    v_s_p = v_s_p -1
                    answer = answer + 2
                    break
                else:
                    v_s.append(value)
                    v_s_p = v_s_p + 1
                    break

    return answer
