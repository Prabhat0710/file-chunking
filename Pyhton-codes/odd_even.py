def ask(string):
    num = 0
    for i in range(0, len(string)):
        num += 1
    
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


ask("Prabhat")


