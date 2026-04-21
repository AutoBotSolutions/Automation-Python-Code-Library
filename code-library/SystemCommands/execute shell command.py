To execute a shell command in Python, you can use the `subprocess` module, which provides a powerful and flexible way to run shell commands.

Here's an example of how you can execute a shell command:

### Example Code
```python
import subprocess

# Example shell command
command = "ls -l"

# Execute the command
try:
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print("Command Output:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error while executing command:")
    print(e.stderr)
```

### Explanation:
1. **`command`**: This is the shell command you want to execute (e.g., `"ls -l"`).
2. **`subprocess.run`**: Runs the command you specify.
   - `shell=True`: Executes the command through the shell.
   - `check=True`: Ensures Python raises an exception for non-zero exit codes.
   - `text=True`: Ensures the output is returned as strings, not bytes.
   - `capture_output=True`: Captures both `stdout` (standard output) and `stderr` (standard error) of the command.
3. **Error Handling**: If the command fails, it raises a `subprocess.CalledProcessError`, which can be caught and processed.

### Output
- The command output is printed on success.
- Any errors (like "command not found") are printed in the `stderr` section.

Let me know if you have a specific command you'd like to execute programmatically!
