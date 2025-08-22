import shlex

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