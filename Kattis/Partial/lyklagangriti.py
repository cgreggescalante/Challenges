# Keystrokes

strokes = input()

output = []
cursor = 0

for stroke in strokes:
    if stroke not in "LRB":
        output.insert(cursor, stroke)
        cursor += 1
    elif stroke == "L":
        cursor -= 1
    elif stroke == "R":
        cursor += 1
    elif stroke == "B" and cursor > 0:
        output = output[:cursor-1] + output[cursor:]
        cursor -= 1
    if cursor < 0:
        cursor = 0
    if cursor > len(output):
        cursor = len(output)

print(''.join(output))
