key = [
    [3, 6, 9, '#'],
    [2, 5, 8, 0],
    [1, 4, 7, '*']
]

def find_idx(number, i):
    for j in range(len(key[i])):
        if key[i][j] == number:
            return j

def solution(numbers, hand):
    answer = ''
    left = key[0][-1]
    right = key[-1][-1]
    lx, ly = 2, 3
    rx, ry = 0, 3
    
    for num in numbers:
        if num in key[2]:
            left = num
            lx, ly = 2, find_idx(left, 2)
            answer += 'L'
        elif num in key[0]:
            right = num
            rx, ry = 0, find_idx(right, 0)
            answer += 'R'
        else:
            tx, ty = 1, find_idx(num, 1)
            dr = abs(tx-rx)+abs(ty-ry)
            dl = abs(tx-lx)+abs(ty-ly)
            if dr > dl:
                left = num
                lx, ly = tx, ty
                answer += 'L'
            elif dr < dl:
                right = num
                rx, ry = tx, ty
                answer += 'R'
            else:
                if hand == 'left':
                    left = num
                    lx, ly = tx, ty
                    answer += 'L'
                else:
                    right = num
                    rx, ry = tx, ty
                    answer += 'R'
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"	
solution(numbers, hand)
#"LRLLLRLLRRL"