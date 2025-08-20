import subprocess, shlex

def run_shell():
    while True:
        cmd = input("$ ")
        if cmd.lower() == "exit":
            break
        subprocess.run(cmd, shell=True)



# Default HOFs
def custom_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def custom_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

def custom_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for item in it:
        value = func(value, item)
    return value


# Custom HOFs
def apply_until_false(func, cond, iterable):
    result = []
    i = 0
    while i < len(iterable):
        if not cond((iterable[i])):
            while i < len(iterable):
                result.append(iterable[i])
                i += 1
            return result
        result.append(func(iterable[i]))
        i += 1
    return result

def map_with_index(func, iterable):
    result = []
    for i, item in enumerate(iterable):
        result.append(func(i, item))
    return result

def conditional_pipeline(funcs, cond):
    def pipeline(data):
        result = []
        for item in data:
            if cond(item):
                for func in funcs:
                    item = func(item)
            result.append(item)
        return result
    return pipeline

'''
# Testing the HOFs
if __name__ == "__main__":
    run_shell()
    
    nums = [1, 2, 3, 4, 5]
    
    print(custom_map(lambda x: x**2, nums))
    print(custom_filter(lambda x: x % 2 == 0, nums))
    print(custom_reduce(lambda a, b: a + b, nums))
    

    func1 = lambda x: x + 1
    cond1 = lambda x: x < 5
    print(apply_until_false(func1, cond1, [1,2,3,7,8]))

    func2 = lambda x, i: x * i
    print(map_with_index(func2, [10,20,30,40]))

    funcs = [
        lambda x: x + 1,
        lambda x: x * 2,
        lambda x: x - 3
    ]
    cond2 = lambda val: val % 2 == 0
    print(conditional_pipeline(funcs, cond2)([1,2,3,4]))
'''

def parse_command(line):
    if not line.strip():
        return ("", [])
    
    try:
        tokens = shlex.split(line)
    except ValueError as e:
        print(f"Parse error: {e}")
        return ("", [])
    
    if not tokens:
        return ("", [])
    cmd = tokens[0]
    args = tokens[1:]
    return cmd, args

def run_interpreter():
    print("Interpreter mode: ':exit' to finish, ':show' to display buffer")
    program_lines = []

    while True:
        line = input("> ")
        if line is None:
            continue

        cmd, args = parse_command(line)

        if cmd == ":exit":
            break
        if cmd == ":show":
            print(program_lines)
            continue

        program_lines.append((cmd, args))

    return program_lines

if __name__ == "__main__":
    program_lines = run_interpreter()
    print("Stored program(s):", program_lines)