from executor import execute_command
from parser import parse_command

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
        execute_command(cmd, args)

    return program_lines