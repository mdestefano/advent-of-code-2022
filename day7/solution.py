import pprint
from queue import LifoQueue, Queue

def read_trace(trace_file):
    with open(trace_file, "r") as f:
        return f.readlines()

def add_edge(graph, node1, node2, label):
    if label not in graph[node1]:
        graph[node1][label] = []
    graph[node1][label].append(node2)

def add_node(graph, node, parent=None, is_dir=False, size=0):
    if node not in graph:
        graph[node] = {"contains": [], "navigation": [], "parent": parent, "is_dir": is_dir, "size": size}

def is_command(line):
    return line.startswith("$")  

def update_size(graph, node="/"):
    if not graph[node]["is_dir"]:
        return graph[node]["size"]
    
    size = sum(map(lambda x: update_size(graph, x), graph[node]["contains"]))
    graph[node]["size"] = size
    return size


def get_dir_name(current_dir, arg):
    if current_dir == "/":
        return current_dir + arg    
    return current_dir + "/" + arg                

def contains_directory(graph, node):
    return any(map(lambda x: graph[x]["is_dir"], graph[node]["contains"]))

def find_smallest_to_free_enough_space(graph, node, current_free_space, required_free_space):
    # if not contains_directory(graph, node):
    #     result = node if current_free_space + graph[node]["size"] >= required_free_space else None
    #     return result

    # candidates = list(filter(lambda x: graph[x]["is_dir"] and current_free_space + graph[x]["size"] >= required_free_space, graph[node]["contains"]))
    # if len(candidates) == 0:
    #     return None

    # best_candidate = next(filter(lambda x: graph[x]["size"] == min(map(lambda y: graph[y]["size"], candidates)), candidates))

    # deeper_result = find_smallest_to_free_enough_space(graph, best_candidate, current_free_space, required_free_space)
    # return deeper_result if deeper_result is not None else best_candidate

    stack = LifoQueue()
    queue = Queue()
    queue.put(node)

    while not queue.empty():
        current_node = queue.get()
        if graph[current_node]["is_dir"]:
            stack.put(current_node)
            for child in graph[current_node]["contains"]:
                queue.put(child)

    best = None
    while not stack.empty():
        current_node = stack.get()
        if current_free_space + graph[current_node]["size"] >= required_free_space:
            best = current_node if best is None else best if graph[best]["size"] < graph[current_node]["size"] else current_node

    return best

### start reading from here
graph = {}
add_node(graph, "/", is_dir=True)
traces = read_trace("input.txt")

current_dir = "/"

for trace in traces:
    trace = trace.strip()
    if is_command(trace):
        trace = trace.split(" ")
        command = trace[1]
        arg = trace[2] if len(trace) > 2 else None

        if command == "cd":

            if arg == "..":
                current_dir = graph[current_dir]["parent"]
            elif arg == "/":
                current_dir = "/"
            else:
                current_dir = get_dir_name(current_dir, arg)

    else:
        trace = trace.split(" ")
        element_name = get_dir_name(current_dir, trace[1])
        is_dir = trace[0] == "dir"
        size = int(trace[0]) if not is_dir else 0
        
        if not element_name in graph.keys():
            add_node(graph, element_name, parent=current_dir, is_dir=is_dir, size=size)
            add_edge(graph, current_dir, element_name, "contains")
        #graph[current_dir]["size"] += size


update_size(graph)

#find all directories with size < 100000
candidates = []
for node in graph.values():
    if node["is_dir"] and node["size"] <= 100000:
        candidates.append(node)

result = sum(map(lambda x: x["size"], candidates))
print(f"Puzzle1: {result}")


TOTAL_SIZE = 70000000
REQUIRED_FREE_SPACE = 30000000
current_free_space = TOTAL_SIZE - graph["/"]["size"]
smallest = find_smallest_to_free_enough_space(graph, "/", current_free_space, REQUIRED_FREE_SPACE)
print(f"Puzzle2: dir: {smallest}, size: {graph[smallest]['size']}")
