# Eight Queens

board = [input() for _ in range(8)]

works = True
for i in range(8):
    # Columns
    if board[i].count("*") > 1:
        works = False
        break
    # Rows
    if [board[j][i] for j in range(8)].count("*") > 1:
        works = False
        break
    # Negative Diagonals from left side
    if [board[i + k][k] for k in range(8 - i)].count("*") > 1:
        works = False
        break
    # Positive Diagonals from right side
    if [board[i + k][7 - k] for k in range(8 - i)].count("*") > 1:
        works = False
        break

for j in range(8):
    # Negative Diagonals from top
    if [board[i][j + i] for i in range(8 - j)].count("*") > 1:
        works = False
        break
    # Positive Diagonals from top
    if [board[i][j - i] for i in range(j+1)].count("*") > 1:
        works = False
        break

print("valid" if works else "invalid")
