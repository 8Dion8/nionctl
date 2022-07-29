import typer
from rich import print as rich_print
from rich.console import Console
from rich.table import Table
import subprocess
import os

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

wifi_app = typer.Typer()
console = Console()
HOMEDIR = os.getenv("HOME")

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


def print_speed_results(data):
    rich_print(f"[bold green]Ping: {round(data['ping'] * 10)/10}  ms")
    rich_print(f"[bold green]Down: {round(data['download']/1e+4)/1e+2} mbit/s")
    rich_print(f"[bold green]Up:   {round(data['upload']/1e+4)/1e+2} mbit/s")

@wifi_app.command("speedtest")
def wifi_speedtest():
    from shutil import which
    if which("speedtest-cli") is None:
        rich_print("[bold red]speedtest-cli is not installed! Please install speedtest-cli using[/bold red][yellow]pip3 install speedtest-cli")
        return
    import speedtest
    s = speedtest.Speedtest()
    rich_print("[yellow]Getting server")
    s.get_best_server()
    rich_print("[yellow]Testing download")
    s.download()
    rich_print("[yellow]Testing upload")
    s.upload()
    results = s.results.dict()
    print_speed_results(results)