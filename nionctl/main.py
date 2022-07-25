import typer
import os
import subprocess

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

main_app = typer.Typer()
wifi_app = typer.Typer()
main_app.add_typer(wifi_app, name="wifi")

HOMEDIR = os.getenv("HOME")


@main_app.command()
def gitclone(link: str, dest: str = HOMEDIR + "/gitclones"):
    os.system(f"cd {dest}")
    out = run_shell_command(f"git clone {link}")
    print(out)
    


@main_app.command()
def neofetch():
    out = run_shell_command("neofetch")
    print(out)


@wifi_app.command("list")
def wifi_list():
    out = run_shell_command("nmcli dev wifi")
    print(out)

@wifi_app.command("connect")
def wifi_connect(ssid: str):
    out = run_shell_command(f"nmcli c up {ssid}")
    print(out)

@wifi_app.command("disconnect")
def wifi_disconnect():
    connected_ssid = run_shell_command("iwgetid -r")
    out = run_shell_command(f"nmcli c down {connected_ssid}")
    print(out)

if __name__ == "__main__":
    main_app()