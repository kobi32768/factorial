import sys
import tqdm

factorial = 1
args = sys.argv
for i in tqdm.tqdm(range(1, int(args[1]) + 1)):
    factorial *= i

    if (len(args) >= 3):
        if (args[2] == "-w"):
            print(str(i) + ": " + str(factorial))

if (len(args) >= 3):
    if (args[2] == "-f"):
        f = open("factorial.txt", "w")
        f.write(str(factorial))
    else:
        print(str(i) + ": " + str(factorial))
