# -*- coding: utf-8 -*-
"""
5.7
"""
N, K, M = map(int, input("Введите количество станций, станцию K и станцию M через пробел: ").split())

if K == M:
    print(0)
else:
    distance_clockwise = (M - K + N) % N
    distance_counterclockwise = (K - M + N) % N
    print(min(distance_clockwise, distance_counterclockwise))

