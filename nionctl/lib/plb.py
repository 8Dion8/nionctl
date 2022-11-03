import typer
from rich import print as rich_print
from rich.console import Console
from rich.table import Table
import subprocess
import os
from time import sleep
from shutil import which

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

plb_app = typer.Typer()
console = Console()
HOMEDIR = os.getenv("HOME")



@plb_app.command("toggle")
def playback_toggle():
    run_shell_command("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")
    

@plb_app.command("next")
def playback_next():
    run_shell_command("mpris-ctl next")


@plb_app.command("prev")
def playback_prev():
    run_shell_command("mpris-ctl prev")