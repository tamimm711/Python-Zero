tasks = []
while True:
    cmd = input("(a)dd, (l)ist, (q)uit: ").lower()
    if cmd == "a":
        task = input("New task: ")
        tasks.append(task)
    elif cmd == "l":
        for i, t in enumerate(tasks, 1):
            print(i, t)
    elif cmd == "q":
        break
    