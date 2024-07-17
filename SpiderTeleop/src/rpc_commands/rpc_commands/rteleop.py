from pynput import keyboard
import subprocess
import os

# Define the base path for the movement scripts
base_path = '/home/wshengggg/HWSpider/src/rpc_commands/rpc_commands'

# Define the mapping of keys to commands
key_command_map = {
    'w': 'moveforward.py',
    'a': 'moveleft.py',
    's': 'movebackward.py',
    'd': 'moveright.py',
    'q': 'rotateanticlockwise.py',
    'e': 'rotateclockwise.py',
    '1': 'standlow.py',
    '2': 'standmiddle.py',
    '3': 'standhigh.py',
    '4': 'standsuperhigh.py',
    '5': 'quadrupledstand.py',
    '6': 'transport.py',
    '7': 'posturedetect.py',
    '8': 'runaction.py',
    '9': 'stop.py',
    'i': 'quadrupledmoveforward.py',
    'j': 'quadrupledmoveleft.py',
    'l': 'quadrupledmoveright.py',
    'k': 'quadrupledmovebackward.py' ,
    'u': 'quadrupledrotateanticlockwise.py',
    'o': 'quadrupledrotateclockwise.py',
    }

def execute_command(script_name):
    try:
        # Construct the full path to the script
        script_path = os.path.join(base_path, script_name)
        subprocess.run(['python3', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing {script_name}: {e}")

def on_press(key):
    try:
        if key.char in key_command_map:
            execute_command(key_command_map[key.char])
    except AttributeError:
        pass

def main():
    print("Press the corresponding key to control the spider robot:")
    print("\nHexapod Mode:")
    print("  q w e ")
    print("  a s d ")
    print("\nNote: Switch to Quadrupled Mode (input '5') before using Quadrupled Mode commands (u, i, o, j, k, l).")
    print("\nQuadrupled Mode:")
    print("  u i o ")
    print("  j k l ")
    print("\nPosture Controls:")
    print("1: Stand Low")
    print("2: Stand Middle")
    print("3: Stand High")
    print("4: Stand Super High")
    print("5: Quadrupled Stand")
    print("6: Transport")
    print("7: Posture Detect")
    print("8: Run Action")
    print("9: Stop")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
