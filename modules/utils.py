# Import the necessary modules
import sys

# Define the ANSI escape codes for different colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Print a message in different colors
print(RED + "This text is red" + RESET)
print(GREEN + "This text is green" + RESET)
print(YELLOW + "This text is yellow" + RESET)
print(BLUE + "This text is blue" + RESET)
print(MAGENTA + "This text is magenta" + RESET)
print(CYAN + "This text is cyan" + RESET)