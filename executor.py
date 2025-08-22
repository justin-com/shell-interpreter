import subprocess

def execute_command(cmd, args):
    if cmd == "echo":
        if not args:
            print("echo: missing arg")
            return
        print (" ".join(args))
        return
    
    if cmd == "cd":
        import os
        try:
            os.chdir(args[0])
            print("cd: success")
        except IndexError:
            print("cd: missing arg")
        except FileNotFoundError:
            print(f"cd: no such directory: {args[0]}")
        return
    
    try:
        result = subprocess.run([cmd] + args, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")
    except FileNotFoundError:
        print(f"Unknown command: {cmd}")