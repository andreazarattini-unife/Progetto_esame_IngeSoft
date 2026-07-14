"""Tkinter user interface for ZMTransform."""

from __future__ import annotations  #permette di riferirsi a classi presenti anche più avanti

import platform
import queue
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, scrolledtext, ttk

from zmtransform.analysis import (
    analyze_measurements,
    create_result_workbook,
    find_input_files,
)

WINDLL = None

#Robusto rispetto al tipo di OS
if platform.system() == "Windows": # pylint: disable=comparison-with-callable
    from ctypes import windll as WINDLL



class ZincApp:
    """Desktop application used to run zinc measurement analysis."""
    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def __init__(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue()
        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, pady=10)

        frame_bottoni = tk.Frame(root)
        frame_bottoni.pack(pady=10)

        self.progress_bar = ttk.Progressbar(
            frame_bottoni,
            orient="horizontal",
            length=200,
            mode="determinate",
        )
        self.progress_bar.grid(row=0, column=2, padx=5)

        self.select_button = tk.Button(
            frame_bottoni,
            text="Seleziona la cartella",
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    def write_log(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def select_directory(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if not output_file:
            self.write_log("Salvataggio annullato.")
            return

        bs_files, ts_files = find_input_files(input_dir)
        self.write_log(f"Cartella selezionata: {input_dir}")
        self.write_log(f"Numero di file Excel trovati in cartella BS: {len(bs_files)}")
        self.write_log(f"Numero di file Excel trovati in cartella TS: {len(ts_files)}")

        if not bs_files:
            self.write_log("File Excel non trovato in cartella BS.")
            return

        self.select_button["state"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def run_analysis(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "Elaborazione avviata."))
            #Esegue i calcoli
            rows, errors = analyze_measurements(bs_files, ts_files)
            #Crea il file Excel
            workbook = create_result_workbook(rows)
            #Salva
            workbook.save(output_file)

            for error in errors:
                self.messages.put(("log", error))

            self.messages.put(("progress", "100"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def process_messages(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)


def configure_windows_dpi() -> None:
    """Improve Tkinter rendering on Windows when the API is available."""
    try:
        if WINDLL is None:
            return
        WINDLL.shcore.SetProcessDpiAwareness(1)
    except (AttributeError, OSError):
        pass


def main() -> None:
    """Start dell'applicazione"""
    configure_windows_dpi()
    root = tk.Tk()
    ZincApp(root)
    root.mainloop()
