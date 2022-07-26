import typer

import wifi
import bt
import util


main_app = typer.Typer()

main_app.add_typer(wifi.wifi_app, name="wifi")
main_app.add_typer(bt.bt_app,     name="bt"  )
main_app.add_typer(util.util_app, name="util")


if __name__ == "__main__":
    main_app()