import functools

class Monkey:
    def __init__(self, starting_items, operation, test, worried=False):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.target_true = None
        self.target_false = None
        self.inspected_items = 0
        self.worried = worried

    def set_targets(self, target_true, target_false):
        self.target_true = target_true
        self.target_false = target_false

    def take(self, item):
        self.items.append(item)

    def round(self):
        for item in self.items:
            self.inspected_items += 1
            new = self.operation(item)
            new = int(new / 3) if not self.worried else new
            if self.test(new):
                self.target_true.take(new)
            else:
                self.target_false.take(new)
        self.items = []
            
def parse_input(filename, worried=False):
    monkeys = []
    targets = []
    tests = []
    with open(filename, "r") as f:
        text = f.read()
    monkeys_lines = text.split("\n\n")
    
    for monkey_line in monkeys_lines:
        lines = monkey_line.split("\n")
        tests.append(get_test_operand(lines[3].strip()))

    modulo = functools.reduce(lambda x, y: x * y, tests)

    for monkey_line in monkeys_lines:
        lines = monkey_line.split("\n")
        starting_items = parse_starting_items(lines[1].strip())
        operation = parse_operation(lines[2].strip(), modulo=modulo, worried=worried)
        test = parse_test(lines[3].strip())
        monkey = Monkey(starting_items, operation, test, worried=worried)
        monkeys.append(monkey)

        target_true = parse_target_true(lines[4].strip())
        target_false = parse_target_false(lines[5].strip())
        targets.append((target_true, target_false))

    for i in range(len(monkeys)):
        target_true, target_false = targets[i]
        if target_true is not None:
            monkeys[i].set_targets(monkeys[target_true], monkeys[target_false])
        else:
            monkeys[i].set_targets(None, None)

    return monkeys


def parse_target_false(target_false_string):
    # remove prefix of "Target false: "
    target_false_string = target_false_string.removeprefix("If false: throw to monkey ")
    if target_false_string == "None":
        return None
    return int(target_false_string)

def parse_target_true(target_true_string):
    # remove prefix of "Target true: "
    target_true_string = target_true_string.removeprefix("If true: throw to monkey ")
    if target_true_string == "None":
        return None
    return int(target_true_string)

def get_test_operand(test_string):
    # remove prefix of "Test: "
    test_string = test_string.removeprefix("Test: divisible by ")
    return int(test_string)

def parse_test(test_string):
    # remove prefix of "Test: "
    operand = get_test_operand(test_string)
    return lambda x: x % operand == 0
        
def parse_operation(operation_string, modulo, worried=False):
    # remove prefix of "Operation: "
    operation_string = operation_string.removeprefix("Operation: new = ")
    not_worried_op = lambda old: eval(operation_string)
    worried_op = lambda old: eval(operation_string) % modulo
    return not_worried_op if not worried else worried_op

def parse_starting_items(starting_items_string):
    # remove prefix of "Starting items: "
    starting_items_string = starting_items_string[15:]
    items_string = starting_items_string.split(",")
    
    if len(items_string) == 1 and items_string[0] == "":
        return []
    
    return [int(x) for x in items_string]

def main():
    monkeys = parse_input("input.txt")

    for i in range(20):
        for i, monkey in enumerate(monkeys):
            monkey.round()

        # for i, monkey in enumerate(monkeys):
        #     print(f"Monkey {i}: {monkey.items}")

        # print("=====================================")


    activity = sorted(list(map(lambda x: x.inspected_items, monkeys)))
    monkey_business = activity[-1] * activity[-2]
    print(f"Monkey business: {monkey_business}")

    worried_monkeys = parse_input("input.txt", worried=True)
    for i in range(10000):
        for i, monkey in enumerate(worried_monkeys):
            monkey.round()

        # for i, monkey in enumerate(worried_monkeys):
        #     print(f"Monkey {i}: {monkey.items}")

        # print("=====================================")
    activity = sorted(list(map(lambda x: x.inspected_items, worried_monkeys)))
    monkey_business = activity[-1] * activity[-2]
    print(f"Monkey business: {monkey_business}")

if __name__ == "__main__":
    main()