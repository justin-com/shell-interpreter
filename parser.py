import shlex
import sys

def parse_command(line):
    """
    Parses a raw line of input into a tuple of a command and arguments.

    Parameters:
        line (str): The raw line of input.

    Returns:
        tuple[str, list[str]]: A command and a list of arguments.
    """
    if not line.strip():
        return ("", [])
    
    try:
        tokens = shlex.split(line)
    except ValueError as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return ("", [])
    
    if not tokens:
        return ("", [])
    cmd = tokens[0]
    args = tokens[1:]
    return cmd, args