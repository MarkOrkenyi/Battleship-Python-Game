import subprocess


def play_sound(soundname):
    if soundname == "start":
        file = "sounds/shipyard.wav"
    elif soundname == "sinking":
        file = "sounds/sinking.wav"
    elif soundname == "placement":
        file = "sounds/placemnet.wav"

    subprocess.Popen(['aplay', '-q', file])
