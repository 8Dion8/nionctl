import typer
from rich import print as rich_print
from rich.console import Console
from rich.table import Table
import subprocess
import os
from time import sleep
from shutil import which
import re

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

img_app = typer.Typer()
console = Console()
HOMEDIR = os.getenv("HOME")



@img_app.callback()
def img_callback():
    if which("convert") is None:
        rich_print("[bold red] imagemagick is not installed!\nPlease install imagemagick using your system package manager.")


@img_app.command("info")
def img_info(filename: str):
    out = run_shell_command(f"identify -ping {filename}")
    table = Table(show_header=False, show_lines=True)

    info = out.split()

    filetype = info[1]
    table.add_row("Image type", filetype)

    imgsize = info[2]
    table.add_row("Image geometry", imgsize)

    depth = info[4]
    table.add_row("Color depth", depth)

    colorspace = info[5]
    table.add_row("Colorspace", colorspace)

    filesize_bytes = info[6][:-1]

    if len(filesize_bytes) > 9:
        filesize = str(round((int(filesize_bytes) / 1073741824) * 100) / 100) + " Gb"
    elif len(filesize_bytes) > 6:
        filesize = str(round((int(filesize_bytes) / 1048576) * 100) / 100) + " Mb"
    elif len(filesize_bytes) > 3:
        filesize = str(round((int(filesize_bytes) / 1024) * 100) / 100) + " kB"
    else:
        filesize = filesize_bytes + " B"
    
    table.add_row("File size", filesize)

    console.print(table)    


@img_app.command("resize")
def img_resize(input_image: str, geometry: str, output_image: str):
    if re.match(r"\d+x\d+|\d+\%", geometry):
        out = run_shell_command(f"convert {input_image} -resize {geometry} {output_image}")
        rich_print(out)
    else:
        rich_print("[bold red] Invalid resize options! Please provide geometry either as {width}x{height} or {percentage}%")

@img_app.command("convert")
def img_convert(input_image: str, output_image: str):
    out = run_shell_command(f"convert {input_image} {output_image}")
    rich_print(out)

@img_app.command("negate")
def img_negate(input_image: str, output_image: str):
    out = run_shell_command(f"convert -negate {input_image} {output_image}")
    rich_print(out)

@img_app.command("rotate")
def img_rotate(input_image: str, degrees: int, output_image: str):
    out = run_shell_command(f"convert {input_image} -rotate {degrees} {output_image}")
    rich_print(out)

@img_app.command("bw")
def img_bw(input_image: str, output_image: str):
    out = run_shell_command(f"convert {input_image} -colorspace Gray {output_image}")
    rich_print(out)


