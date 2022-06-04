import sys
import tqdm

factorial = 1
args = sys.argv
if (len(args) >= 3 and args[2] == "-w"):
    for i in range(1, int(args[1]) + 1):
        factorial *= i
        print(str(i) + ": " + str(factorial))
else:
    for i in tqdm.tqdm(range(1, int(args[1]) + 1)):
        factorial *= i

if (len(args) >= 3):
    if (args[2] == "-f"):
        f = open("factorial.txt", "w")
        f.write(str(factorial))
else:
    print(str(i) + ": " + str(factorial))
