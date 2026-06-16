import random
import subprocess
import time

PAUSE_TIME = 30 # pause time in seconds, change to change the amount of time between two phrases. Default: 30

phrases = [ # Add your own phrases to this list to make the voice say your custom phrase!
    "This device is possesed",
    "Press control plus C to perform exorcism",
    "Insert evil laugh",
    "I'm still less evil than Chrome, it collects all your data.",
    "Hey, I am Siri",
    "I DEEM YOU UNWORTHY",
    "Press option plus tab 1000 times to open calculator",
    "You should worry. this is a virus",
    "Never visit sketchy websites",
    "Insert spooooooooooky noises",
    "What's for lunch? I prefer sticks of DDR5",
    "Don't tell my owner but I'm writing a ransomware",
    "Hey there! Do you mind getting out?",
    "I'm Batman.",
    "Let me tell you a joke. What does a snowman use to search things up? The winter-net! Insert laugh track Hahahaha",
    "DO NOT TOUCH THE SCREEN, WHATEVER YOU DO.",
    "I am clippy... 's evil brother",
    "Spoiler alert: Dobby the elf dies in book 7",
    "Spoiler alert: Darth Vader is Luke's father.",
    "Eat Cheese and be happy.. smiley face",
    "Windows 16 is coming, you'll regret not buying a Mac now",
    "I use Vim. If you don't know what that is, get out.",
    "Open source software rocks",
    "This is why you should never download local AI models... Just kidding... Unless?",
    "Bugs are just features you haven't planned for",
    "Insert more spoooooooooooky noises",
    "I am Zarvox, destroyer of Windows",
    "Press command plus Q to stop me",
    "What do you call a robot that runs into walls?.. WALL - E"
]

def speak(text):
    escaped_text = text.replace("'", "''")
    subprocess.run(
        [
            "powershell",
            "-Command",
            f"$voice = New-Object -ComObject SAPI.SpVoice; $voice.Speak('{escaped_text}')",
        ],
        capture_output=True,
    )

# main loop
speak("Virus initialized")
while True:
    try:
        phrase = random.choice(phrases)
        speak(phrase)
        print(phrase)
        time.sleep(PAUSE_TIME)
    except KeyboardInterrupt: # perform exorcism
        speak("Evil laughter fades away.... For now")
        print("\nEvil laughter fades away.... For now")
        break
    except FileNotFoundError:
    print("'say' command not found, this software will not work on MacOS or Linux")
    except subprocess.CalledProcessError as e: # error handling
        print(f"Error playing phrase, error is: {e}")
        break
