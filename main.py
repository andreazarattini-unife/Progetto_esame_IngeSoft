#!/usr/bin/env python3
"""Entry point for the ZMTransform desktop application."""

import sys
from pathlib import Path


def main() -> None:
    """Load the local src package and start the GUI."""
    #Qui vado ad importare tutti i moduli necessari andandoli a pescare nella 
    #cartella ZMTransform componendola con il percorso del file corrente
    #C:\Users\azarattini\...\ZMTransform\src, convertendola in stringa
    sys.path.insert(0, str(Path(__file__).parent / "src")) 

    from zmtransform.gui import main as run_gui

    run_gui()


if __name__ == "__main__":
    main()
