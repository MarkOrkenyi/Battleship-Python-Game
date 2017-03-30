import subprocess


def play(audio_file_path):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path])


play("/home/markorkenyi/Codecool/PYTHON/Battleship/Battleship-Python-Game/sounds/shipyard.wav")
