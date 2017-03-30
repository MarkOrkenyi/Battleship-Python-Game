import subprocess


def play_sound(soundname):
    '''Plays a given sound. "soundname" is the name of the .wav file in the /sounds directory.'''

    file = "sounds/" + soundname + ".wav"
    subprocess.Popen(['aplay', '-q', file])
