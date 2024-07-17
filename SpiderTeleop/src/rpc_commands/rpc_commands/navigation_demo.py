import subprocess
import os
import time

# Define the base path for the movement scripts
base_path = '/home/wshengggg/HWSpider/src/rpc_commands/rpc_commands'

def execute_command(script_name):
    try:
        # Construct the full path to the script
        script_path = os.path.join(base_path, script_name)
        subprocess.run(['python3', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing {script_name}: {e}")

def main():
    # Define the sequence of commands to execute
    command_sequence = [
        #(action, wait time)
        ('standmiddle.py', 1),    # Stand middle and wait for 1 seconds
        ('moveforward.py', 2),    # Move forward and wait for 2 seconds
        ('stop.py', 1),            # Stop and wait for 1 second
        ('rotateclockwise.py', 4),  # Rotate clockwise and wait for 4 seconds
        ('stop.py', 1),           
        ('moveleft.py', 2),       
        ('stop.py', 1),           
        ('movebackward.py', 5),  
        ('stop.py', 1),           
        ('rotateanticlockwise.py', 3), 
        ('stop.py', 1),          
        ('standhigh.py', 1),      
        ('moveforward.py', 3),   
        ('stop.py', 1),           
        ('standlow.py', 2),   
        ('moveright.py', 3),
        ('stop.py', 1),
        ('quadrupledstand.py', 2),
        ('quadrupledrotateanticlockwise.py', 3),
        ('stop.py', 1),
        ('quadrupledmoveleft.py', 4),
        ('stop.py', 1),
        ('transport.py', 5),
        ('standmiddle.py', 2),
        ('standhigh.py', 2),
        ]

    print("Starting navigation sequence...")

    # Execute each command in the sequence
    for script_name, duration in command_sequence:
        print(f"Executing {script_name} for {duration} seconds...")
        execute_command(script_name)
        time.sleep(duration)

    print("Navigation sequence completed.")

if __name__ == "__main__":
    main()
