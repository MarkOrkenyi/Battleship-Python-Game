import subprocess


def play_sound(soundname):
    if soundname == "start":
        file = "sounds/shipyard.wav"
    elif soundname == "sinking":
        file = "sounds/sinking.wav"
    elif soundname == "placement":
        file = "sounds/placement.wav"
    elif soundname == "splash":
        file = "sounds/splash.wav"
    elif soundname == "hit":
        file = "sounds/hit.wav"

    subprocess.Popen(['aplay', '-q', file])
