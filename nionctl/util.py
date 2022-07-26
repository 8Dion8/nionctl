import typer
from rich import print as rich_print
from rich.console import Console
from rich.table import Table
import subprocess
import os

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

util_app = typer.Typer()
console = Console()
HOMEDIR = os.getenv("HOME")



@util_app.command()
def gitclone(link: str, dest: str = HOMEDIR + "/gitclones"):
    os.system(f"cd {dest}")
    out = run_shell_command(f"git clone {link}")
    rich_print(out)