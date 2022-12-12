
class CPU():
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.current_command = None
        self.command_queue = []
        self.CRT = ""
        for i in range(0, 6):
            for i in range(0, 40):
                self.CRT += '.'
        self.caret_position = 0

    def add_command(self, command):
        self.command_queue.append(command)

    def tick(self):
        if self.current_command is None:
            if len(self.command_queue) > 0:
                self.current_command = self.command_queue.pop(0)
            else:
                return

        if (self.caret_position % 40) in [self.X-1, self.X, self.X+1]:
            self.CRT = self.CRT[:self.caret_position] + "#" + self.CRT[self.caret_position + 1:]
        
        self.caret_position += 1

        if self.current_command.name == 'addx' and self.current_command.left == 0:
            self.X += self.current_command.value

        if self.current_command.left == 0:
            self.current_command = None
            return
        else :
            self.current_command.left -= 1
        
        self.cycle += 1

    def signal_strength(self):
        return self.X * self.cycle

    def print_screen(self):
        n = 40 # chunk length
        chunks = [self.CRT[i:i+n] for i in range(0, len(self.CRT), n)]
        for chunk in chunks:
            print(chunk)


class Command():
    def __init__(self, name, value, left):
        self.name = name
        self.value = value
        self.left = left

    def __repr__(self):
        return f'{self.name} {self.value} {self.left}'

def parse_command(line):
    l = line.split(' ')
    name = l[0]
    value = 0
    if name == 'addx':
        left = 1
        value = l[1]
    else:
        left = 0
    return Command(name, int(value), int(left))

def main():
    cpu = CPU()
    with(open('input.txt')) as f:
        for line in f:
            line = line.strip()
            cpu.add_command(parse_command(line))

    signals = []
    n = 0
    while len(cpu.command_queue) > 0:
        cpu.tick()
        if cpu.cycle % (20 + n * 40) == 0:
            signals.append(cpu.signal_strength())
            n += 1

    print("Puzzle 1: ", sum(signals))

    print("=================================")
    #print(cpu.CRT)
    cpu.print_screen()

if __name__ == '__main__':
    main()
    
    