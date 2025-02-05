from pynput import keyboard
import time
done = True
timing = 0.505
emulate_key = 'l'
start_key = keyboard.Key.home
quit_key = keyboard.Key.end

def init_instr():
    print("Stardew Valley Fishing Timer")
    print("By Simon")
    time.sleep(0.2)
    print(" ")
    print("Controls:")
    print("[HOME]: Cast Rod")
    print("[END]: Quit Program")
    print(" ")
    print("Note: Only quick/normal length presses will result in perfect timing")
    print("If timing is not perfect, press the [HOME] button for a shorter/longer amount of time.")

def main_prog():
    with keyboard.Events() as events:
        for event in events:
            if event.key == quit_key:
                break
            if event.key == start_key:
                keyboard.Controller().press(emulate_key)
                time.sleep(timing)
                keyboard.Controller().release(emulate_key)

def terminal_func():
    print("For more information on command-line options type HELP")
    while True:
        comm = input(">")
        if comm == "HELP":
            print("For more specific information type HELP command-name")
            print("TIMING         Adjust the timing for the cast.")
            print("CASTCHANGE     Change the button pressed to time you cast.")
            print("QUITCHANGE     Change the button pressed to quit the program.")
            print("KEY            Change the key used to cast a fishing rod.")
        if comm == "HELP TIMING":
            print("Adjust the timing for the cast")
            print("Original hold time(recomended): 0.505(s)")
                
            if comm == "HELP CASTCHANGE":
                pass
            if comm == "HELP QUITCHANGE":
                pass
            if comm == "HELP KEY":
                pass
            
            




terminal_func()
