import subprocess

def execute_command(cmd, args):
    """
    Executes a command given certain arguments.

    Parameters:
        cmd (str): The command to run.
        args (list[str]): Arguments for the command.

    Returns:
        str: Output of the command or an error message.
    """
    if cmd == "echo":
        return handle_echo(args)
    
    if cmd == "cd":
        return handle_cd(args)
    
    try:
        result = subprocess.run([cmd] + args, capture_output=True, text=True)
        output = ""
        if result.stdout:
            output += result.stdout
        if result.stderr:
            output += result.stderr
        return output if output else None
    except FileNotFoundError:
        return f"Unknown command: {cmd}"

def handle_echo(args):
    """
    Creates a string from provided arguments.
    
    Parameters:
        args (list[str]): List of arguments for echo to output.

    Returns:
        str: The joined string of arguments provided or an error message if no arguments are provided.
    """
    if not args:
        return "echo: missing arg"
    return " ".join(args)

def handle_cd(args):
    """
    Changes file directory given a destination.

    Parameters:
        args (list[str]): List of arguments where only the first element is considered.

    Returns:
        str: A message depending on the result of the operation.
    """
    import os
    try:
        os.chdir(args[0])
        return "cd: success"
    except IndexError:
        return "cd: missing arg"
    except FileNotFoundError:
        return f"cd: no such directory: {args[0]}"