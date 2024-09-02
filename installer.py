import os
import subprocess
import sys

##################à
# Define the function to run the command
def run_command(command):
    try:
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True)
        #output
        return output.decode('utf-8')
    #finish
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None
print(run_command)