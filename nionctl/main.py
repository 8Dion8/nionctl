import typer

import os, sys
pwd = "/".join(__file__.split("/")[:-1])
sys.path.append(pwd)

import lib.wifi as wifi
import lib.bt as bt
import lib.util as util
import lib.archive as archive
import lib.img as img


main_app = typer.Typer()

main_app.add_typer(wifi.wifi_app,       name="wifi"   )
main_app.add_typer(bt.bt_app,           name="bt"     )
main_app.add_typer(util.util_app,       name="util"   )
main_app.add_typer(archive.archive_app, name="archive")
main_app.add_typer(img.img_app,         name="img"    )


if __name__ == "__main__":
    main_app()
