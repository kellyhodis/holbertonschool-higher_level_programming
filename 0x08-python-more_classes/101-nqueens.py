#!/usr/bin/python3
"""
module for solving the n queens puzzle
"""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    int(sys.argv[1])
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N >= 4:
    count = 0
    tile_row = 0
    tile_col = 1
    solutions = [[0, 0] for i in range(0, N)]
    for coord in solutions:
        coord[0] = tile_row
        coord[1] = tile_col
        if tile_row == tile_col:
            tile_col += 1
        if tile_col >= N:
            tile_col = 0
        if tile_row >= N:
            break
        tile_row += 1
        tile_col += 1
        count += 1
    print(solutions)
else:
    print("N must be at least 4")
    sys.exit(1)
