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

bt_app = typer.Typer()
console = Console()
HOMEDIR = os.getenv("HOME")



@bt_app.callback()
def bt_callback():
    if which("bluetoothctl") is None:
        rich_print("[bold red] bluetoothctl is not installed!\nPlease install bluetoothctl using your system package manager.")


@bt_app.command("on")
def bluetooth_on():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl power on")
        if "Changing power on succeeded" in out:
            rich_print("[bold green]Bluetooth power on succeeded!")
            return
    rich_print("[bold red]Bluetooth power on failed.")
    
@bt_app.command("off")
def bluetooth_off():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl power off")
        if "Changing power off succeeded" in out:
            rich_print("[bold green]Bluetooth power off succeeded!")
            return
    rich_print("[bold red]Bluetooth power off failed.")

@bt_app.command("list")
def bluetooth_list():
    out = run_shell_command("bluetoothctl devices")
    rich_print(out)

@bt_app.command("connect")
def bluetooth_connect(ssid: str):
    timeout = 10
    run_shell_command(f"bluetoothctl connect {ssid}")
    for i in range(timeout):
        sleep(1)
        info = run_shell_command("bluetoothctl info")
        try: 
            for line in info.splitlines():
                if line.startswith("\tConnected"):
                    connection_status = line.split(":")[1][1:]
                    if connection_status == "yes":
                        rich_print(f"[bold green]Connected to {ssid}!")
                        return
        except:
            rich_print(f"Connection timeout {i}, trying again...")
            continue
        rich_print(f"Connection timeout {i}, trying again...")
    rich_print(f"[bold red]Connection to {ssid} failed.")

@bt_app.command("disconnect")
def bluetooth_disconnect(ssid: str):
    run_shell_command(f"bluetoothctl disconnect {ssid}")
    
@bt_app.command("pair-on")
def bluetooth_pair_on():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl pairable on")
        if "Changing pairable on succeeded" in out:
            rich_print("[bold green]Bluetooth pairable on succeeded!")
            return
    rich_print("[bold red]Bluetooth pairable on failed.")

@bt_app.command("pair-off")
def bluetooth_pair_off():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl pairable off")
        if "Changing pairable off succeeded" in out:
            rich_print("[bold green]Bluetooth pairable off succeeded!")
            return
    rich_print("[bold red]Bluetooth pairable off failed.")

@bt_app.command("pair")
def bluetooth_pair(ssid: str):
    run_shell_command(f"bluetoothctl pair {ssid}")

@bt_app.command("remove")
def bluetooth_remove(ssid: str):
    out = run_shell_command(f"bluetoothctl remove {ssid}")
    rich_print(out)