def solution(x, y):
    return x.symmetric_difference(y).pop()

solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
