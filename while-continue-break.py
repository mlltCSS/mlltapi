while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == "done":
        print("Done!")
        break
    print(line)

