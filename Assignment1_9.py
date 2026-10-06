#write a program to print table of 2

def main():
    for i in range(2, 21, 1):
        if i % 2 == 0:
            print(i, end="  ")

if __name__ == "__main__":
    main()

