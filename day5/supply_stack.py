from queue import LifoQueue
import re

def get_state_and_commands(lines):
    state = []
    commands = []
    readin_state = True
    for line in lines:
        if readin_state and not line.strip():
            readin_state = False
        if line.strip():
            state.append(line) if readin_state else commands.append(line)
    return state, commands

def inizialize_staks(state):
    last_line = [ch for ch in state[-1].split(" ") if ch.isdigit()]
    n_of_stacks = len(last_line)
    
    stacks = []
    for i in range(n_of_stacks):
        stacks.append(LifoQueue())
    
    # state = state[:-1]
    del state[-1]

    for line in reversed(state):
        stack_index = 0
        spaces_seen = 0 
        for cell in line.split(" "):
            if cell.strip():
                crate = ''.join(e for e in cell if e.isalnum())
                crate = crate.strip()
                stacks[stack_index].put(crate)
                stack_index += 1
                spaces_seen = 0
            else:
                # QUA STA L'ERRORE. VA BENE SE CI SONO SPAZI MULTIPLO DI 2
                spaces_seen += 1
                if spaces_seen % 4 == 0:
                    stack_index += 1
    return stacks

def parse_command(command):
    command = command.strip()
    m = re.match("move (?P<q>\d+) from (?P<f>\d+) to (?P<t>\d+)", command)
    return {"quantity": int(m.group('q')), "from": int(m.group('f'))-1, "to": int(m.group('t'))-1}

def parse_commands(commands):
    parsed_commands = []
    for command in commands:
        parsed_commands.append(parse_command(command))
    return parsed_commands

def move_one_at_time(commands, stacks):
    for command in commands:
        for i in range(command["quantity"]):
                # print(f"Moving from {command['from']+1} to {command['to']+1}")
                # print(stacks[command["from"]].queue)
            stacks[command["to"]].put(stacks[command["from"]].get_nowait())                


    result = ''.join([s.queue[-1] for s in stacks])
    return result

def move_multiple_at_time(commands, stacks):
    buf = LifoQueue()
    for command in commands:
        for i in range(command["quantity"]):
            buf.put(stacks[command["from"]].get_nowait())
        
        while not buf.empty():
            stacks[command["to"]].put(buf.get_nowait())
    
    result = ''.join([s.queue[-1] for s in stacks])
    return result

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        state, commands = get_state_and_commands(lines)

        stacks = inizialize_staks(state)
        commands = parse_commands(commands)

        # print(*commands, sep="\n")

        # for i,stack in enumerate(stacks):
        #     print(f"Stack {i+1}: {stack.queue}")

        print(f"Puzzle 2: {move_multiple_at_time(commands, stacks)}")

if __name__ == "__main__":
    main()