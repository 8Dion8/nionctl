import typer
import os
import subprocess
from time import sleep
from rich import print as rich_print
from rich.console import Console
from rich.table import Table

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

main_app = typer.Typer()

wifi_app = typer.Typer()
bluetooth_app = typer.Typer()

main_app.add_typer(wifi_app, name="wifi")
main_app.add_typer(bluetooth_app, name="bt")

console = Console()

HOMEDIR = os.getenv("HOME")




@main_app.command()
def gitclone(link: str, dest: str = HOMEDIR + "/gitclones"):
    os.system(f"cd {dest}")
    out = run_shell_command(f"git clone {link}")
    rich_print(out)
    
@main_app.command()
def neofetch():
    out = run_shell_command("neofetch")
    print(out)



@wifi_app.command("list")
def wifi_list():
    out = run_shell_command("nmcli dev wifi")
    
    table = Table("BSSID", "Name", "Channel", "Rate", "Signal", "Security", show_lines=True)

    first_line = True

    for line in out.splitlines():
        wifi_inuse = False
        if first_line:
            first_line = False
            continue
        elements = list(filter(None, line.split("  ")))
        first_element = elements[0]
        if first_element.count(":") != 5:
            wifi_inuse = True
            elements.pop(0)

        bssid = elements[0].strip()
        name = elements[1].strip()
        channel = elements[3].strip()
        rate = elements[4].strip()
        bars = elements[6].strip()
        security = elements[7].strip()

        if not wifi_inuse:
            table.add_row(bssid, name, channel, rate, bars, security)
        else:
            table.add_row(bssid, name, channel, rate, bars, security, style="bold green")

    console.print(table)

@wifi_app.command("connect")
def wifi_connect(ssid: str):
    out = run_shell_command(f"nmcli c up {ssid}")
    rich_print(out)

@wifi_app.command("disconnect")
def wifi_disconnect():
    connected_ssid = run_shell_command("iwgetid -r")
    out = run_shell_command(f"nmcli c down {connected_ssid}")
    rich_print(out)



@bluetooth_app.command("on")
def bluetooth_on():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl power on")
        if "Changing power on succeeded" in out:
            rich_print("[bold green]Bluetooth power on succeeded!")
            return
    rich_print("[bold red]Bluetooth power on failed.")
    
@bluetooth_app.command("off")
def bluetooth_off():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl power off")
        if "Changing power off succeeded" in out:
            rich_print("[bold green]Bluetooth power off succeeded!")
            return
    rich_print("[bold red]Bluetooth power off failed.")

@bluetooth_app.command("list")
def bluetooth_list():
    out = run_shell_command("bluetoothctl devices")
    rich_print(out)

@bluetooth_app.command("connect")
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

@bluetooth_app.command("disconnect")
def bluetooth_disconnect(ssid: str):
    run_shell_command(f"bluetoothctl disconnect {ssid}")
    
@bluetooth_app.command("pair-on")
def bluetooth_pair_on():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl pairable on")
        if "Changing pairable on succeeded" in out:
            rich_print("[bold green]Bluetooth pairable on succeeded!")
            return
    rich_print("[bold red]Bluetooth pairable on failed.")

@bluetooth_app.command("pair-off")
def bluetooth_pair_off():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl pairable off")
        if "Changing pairable off succeeded" in out:
            rich_print("[bold green]Bluetooth pairable off succeeded!")
            return
    rich_print("[bold red]Bluetooth pairable off failed.")

@bluetooth_app.command("remove")
def bluetooth_remove(ssid: str):
    out = run_shell_command(f"bluetoothctl remove {ssid}")
    rich_print(out)



if __name__ == "__main__":
    main_app()