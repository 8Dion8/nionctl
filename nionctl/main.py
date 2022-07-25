import typer
import os
import subprocess
from time import sleep

def run_shell_command(command):
    out = subprocess.run([i for i in command.split()], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return out

main_app = typer.Typer()

wifi_app = typer.Typer()
bluetooth_app = typer.Typer()

main_app.add_typer(wifi_app, name="wifi")
main_app.add_typer(bluetooth_app, name="bt")

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



@bluetooth_app.command("on")
def bluetooth_on():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl power on")
        if "Changing power on succeeded" in out:
            print("Bluetooth power on succeeded!")
            return
    print("Bluetooth power on failed.")
    
@bluetooth_app.command("off")
def bluetooth_off():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl power off")
        if "Changing power off succeeded" in out:
            print("Bluetooth power off succeeded!")
            return
    print("Bluetooth power off failed.")

@bluetooth_app.command("list")
def bluetooth_list():
    out = run_shell_command("bluetoothctl devices")
    print(out)

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
                        print(f"Connected to {ssid}!")
                        return
        except:
            print(f"Connection timeout {i}, trying again...")
            continue
        print(f"Connection timeout {i}, trying again...")
    print(f"Connection to {ssid} failed.")

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
            print("Bluetooth pairable on succeeded!")
            return
    print("Bluetooth pairable on failed.")

@bluetooth_app.command("pair-off")
def bluetooth_pair_off():
    timeout = 5
    for i in range(5):
        sleep(0.1)
        out = run_shell_command("bluetoothctl pairable off")
        if "Changing pairable off succeeded" in out:
            print("Bluetooth pairable off succeeded!")
            return
    print("Bluetooth pairable off failed.")

@bluetooth_app.command("remove")
def bluetooth_remove(ssid: str):
    out = run_shell_command(f"bluetoothctl remove {ssid}")
    print(out)



if __name__ == "__main__":
    main_app()