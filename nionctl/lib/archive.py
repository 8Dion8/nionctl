import typer
from rich import print as rich_print
from rich.console import Console
from rich.table import Table
import subprocess
import os

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

archive_app = typer.Typer()
console = Console()
HOMEDIR = os.getenv("HOME")


@archive_app.command("zip")
def archive_zip(input_directory: str, output_file: str):
    out = run_shell_command(f"zip -r {output_file} {input_directory}")
    rich_print(out)

@archive_app.command("unzip")
def archive_unzip(input_file: str, output_directory: str):
    out = run_shell_command(f"unzip {input_file} -d {output_directory}")
    rich_print(out)

@archive_app.command("tar")
def archive_tar(input_directory: str, output_file: str):
    out = run_shell_command(f"tar -cvf {output_file} {input_directory}")
    rich_print(out)

@archive_app.command("untar")
def archive_untar(input_file: str, output_directory: str):
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    out = run_shell_command(f"tar -xvf {input_file} -C {output_directory}")
    rich_print(out)

@archive_app.command("targz")
def archive_targz(input_directory: str, output_file: str):
    out = run_shell_command(f"tar -zcvf {output_file} {input_directory}")
    rich_print(out)

@archive_app.command("untargz")
def archive_untargz(input_file: str, output_directory: str):
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    out = run_shell_command(f"tar -zxvf {input_file} -C {output_directory}")
    rich_print(out)

@archive_app.command("tarbz2")
def archive_tarbz2(input_directory: str, output_file: str):
    out = run_shell_command(f"tar -jcvf {output_file} {input_directory}")
    rich_print(out)

@archive_app.command("untarbz2")
def archive_untarbz2(input_file: str, output_directory: str):
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    out = run_shell_command(f"tar -jxvf {input_file} -C {output_directory}")
    rich_print(out)