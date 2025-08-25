from executor import execute_command
from parser import parse_command

def run_interpreter():
    """
    Runs the interpreter loop.
    Continuously reads input, parses commands, and executes them.
    Special commands:
        ":exit" - ends the loop
        ":show" - displays the current buffer of commands

    Returns:
        str | None: Output of ":show" if input. Else, None.
    """
    print("Interpreter mode: ':exit' to finish, ':show' to display buffer")
    program_lines = []

    while True:
        cmd, args = input_func()

        if not cmd:
            program_lines.append((cmd, args))
            continue
        if cmd == ":exit":
            break
        if cmd == ":show":
            output_func(str(program_lines))

        program_lines.append((cmd, args))
        result = execute_command(cmd, args)
        if result:
            output_func(result)

def input_func():
    """
    Reads and parses a line of input.
    Prompts the user for input then parses it into a command and arguments.

    Returns:
        tuple[str, list[str]]: A pair of (commands, args).
    """
    line = input("> ")
    if line is None:
        return None

    cmd, args = parse_command(line)
    return (cmd, args)

def output_func(msg):
    """
    Handles output messages from the interpreter.
    
    Parameters:
        msg (str): Message given.
    
    Returns:
        str: Same message.
    """
    return msg