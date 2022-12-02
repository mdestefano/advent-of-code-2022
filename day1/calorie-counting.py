import numpy as np

def main():
    with open('input1.txt') as f:
        lines = f.readlines()
        
        elves = []
        elf = 0
        elves.append(0)
        for line in lines:
            if line.strip():
                elves[elf] += int(line)
            else:
                elf+=1
                elves.append(0)
        
        elves = np.sort(elves)
        print(sum(elves[-3:]))

    return 

if __name__ == "__main__":
    main()