"""Tkinter user interface for ZMTransform."""

from __future__ import annotations #permette di riferirsi a classi presenti anche più avanti

import queue
import threading
import platform
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, scrolledtext, ttk

#Robusto rispetto al tipo di OS
if platform.system == "Windows":
    from ctypes import windll
else:
    windll = None

from zmtransform.analysis import analyze_measurements, create_result_workbook, find_input_files


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁZincAppǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁZincAppǁwrite_log__mutmut: MutantDict = {}  # type: ignore
mutants_xǁZincAppǁselect_directory__mutmut: MutantDict = {}  # type: ignore
mutants_xǁZincAppǁrun_analysis__mutmut: MutantDict = {}  # type: ignore
mutants_xǁZincAppǁprocess_messages__mutmut: MutantDict = {}  # type: ignore


class ZincApp:
    """Desktop application used to run zinc measurement analysis."""

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    @_mutmut_mutated(mutants_xǁZincAppǁ__init____mutmut)
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_orig(self, root: tk.Tk) -> None: #Costruttore
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_1(self, root: tk.Tk) -> None: #Costruttore
        self.root = None
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_2(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = None 

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_3(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title(None)
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_4(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("XXZMTransformXX")
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_5(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("zmtransform")
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_6(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTRANSFORM")
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_7(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry(None)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_8(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("XX1000x800XX")

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_9(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000X800")

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_10(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = None
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_11(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(None, wrap="word")
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_12(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap=None)
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_13(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(wrap="word")
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_14(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, )
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_15(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="XXwordXX")
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_16(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="WORD")
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_17(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=None, fill="both", padx=10, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_18(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill=None, padx=10, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_19(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=None, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_20(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, pady=None)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_21(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(fill="both", padx=10, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_22(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, padx=10, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_23(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_24(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, )

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_25(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=False, fill="both", padx=10, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_26(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="XXbothXX", padx=10, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_27(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="BOTH", padx=10, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_28(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=11, pady=10)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_29(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, pady=11)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_30(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, pady=10)

        frame_bottoni = None
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_31(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, pady=10)

        frame_bottoni = tk.Frame(None)
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_32(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, pady=10)

        frame_bottoni = tk.Frame(root)
        frame_bottoni.pack(pady=None)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_33(self, root: tk.Tk) -> None: #Costruttore
        self.root = root
        #Il thread di analisi non può modificare direttamente la finestra
        #principale Tkinter, quindi manda dei messaggi
        self.messages: queue.Queue[tuple[str, str]] = queue.Queue() 

        self.root.title("ZMTransform")
        self.root.geometry("1000x800")

        self.log_area = scrolledtext.ScrolledText(root, wrap="word")
        self.log_area.pack(expand=True, fill="both", padx=10, pady=10)

        frame_bottoni = tk.Frame(root)
        frame_bottoni.pack(pady=11)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_34(self, root: tk.Tk) -> None: #Costruttore
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

        self.progress_bar = None
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_35(self, root: tk.Tk) -> None: #Costruttore
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
            None,
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_36(self, root: tk.Tk) -> None: #Costruttore
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
            orient=None,
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_37(self, root: tk.Tk) -> None: #Costruttore
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
            length=None,
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_38(self, root: tk.Tk) -> None: #Costruttore
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
            mode=None,
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_39(self, root: tk.Tk) -> None: #Costruttore
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_40(self, root: tk.Tk) -> None: #Costruttore
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_41(self, root: tk.Tk) -> None: #Costruttore
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_42(self, root: tk.Tk) -> None: #Costruttore
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_43(self, root: tk.Tk) -> None: #Costruttore
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
            orient="XXhorizontalXX",
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_44(self, root: tk.Tk) -> None: #Costruttore
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
            orient="HORIZONTAL",
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_45(self, root: tk.Tk) -> None: #Costruttore
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
            length=201,
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_46(self, root: tk.Tk) -> None: #Costruttore
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
            mode="XXdeterminateXX",
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_47(self, root: tk.Tk) -> None: #Costruttore
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
            mode="DETERMINATE",
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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_48(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=None, column=2, padx=5)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_49(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=0, column=None, padx=5)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_50(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=0, column=2, padx=None)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_51(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(column=2, padx=5)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_52(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=0, padx=5)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_53(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=0, column=2, )

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_54(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=1, column=2, padx=5)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_55(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=0, column=3, padx=5)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_56(self, root: tk.Tk) -> None: #Costruttore
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
        self.progress_bar.grid(row=0, column=2, padx=6)

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

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_57(self, root: tk.Tk) -> None: #Costruttore
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

        self.select_button = None
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_58(self, root: tk.Tk) -> None: #Costruttore
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
            None,
            text="Seleziona la cartella",
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_59(self, root: tk.Tk) -> None: #Costruttore
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
            text=None,
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_60(self, root: tk.Tk) -> None: #Costruttore
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
            command=None, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_61(self, root: tk.Tk) -> None: #Costruttore
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
            text="Seleziona la cartella",
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_62(self, root: tk.Tk) -> None: #Costruttore
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
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_63(self, root: tk.Tk) -> None: #Costruttore
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
            )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_64(self, root: tk.Tk) -> None: #Costruttore
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
            text="XXSeleziona la cartellaXX",
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_65(self, root: tk.Tk) -> None: #Costruttore
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
            text="seleziona la cartella",
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_66(self, root: tk.Tk) -> None: #Costruttore
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
            text="SELEZIONA LA CARTELLA",
            command=self.select_directory, #Qui, nel thread principae
            #chiamo la selezione della directory
        )
        self.select_button.grid(row=0, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_67(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=None, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_68(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=None, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_69(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=0, sticky=None, padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_70(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=0, sticky="w", padx=None)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_71(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_72(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_73(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=0, padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_74(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=0, sticky="w", )

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_75(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=1, column=0, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_76(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=1, sticky="w", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_77(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=0, sticky="XXwXX", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_78(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=0, sticky="W", padx=5)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_79(self, root: tk.Tk) -> None: #Costruttore
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
        self.select_button.grid(row=0, column=0, sticky="w", padx=6)

        exit_button = tk.Button(frame_bottoni, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_80(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = None
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_81(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(None, text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_82(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(frame_bottoni, text=None, command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_83(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(frame_bottoni, text="Esci", command=None)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_84(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(text="Esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_85(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(frame_bottoni, command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_86(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(frame_bottoni, text="Esci", )
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_87(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(frame_bottoni, text="XXEsciXX", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_88(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(frame_bottoni, text="esci", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_89(self, root: tk.Tk) -> None: #Costruttore
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

        exit_button = tk.Button(frame_bottoni, text="ESCI", command=root.quit)
        exit_button.grid(row=0, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_90(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=None, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_91(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=None, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_92(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=1, sticky=None, padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_93(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=1, sticky="e", padx=None)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_94(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_95(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_96(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=1, padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_97(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=1, sticky="e", )

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_98(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=1, column=1, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_99(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=2, sticky="e", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_100(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=1, sticky="XXeXX", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_101(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=1, sticky="E", padx=5)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_102(self, root: tk.Tk) -> None: #Costruttore
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
        exit_button.grid(row=0, column=1, sticky="e", padx=6)

        self.root.after(100, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_103(self, root: tk.Tk) -> None: #Costruttore
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

        self.root.after(None, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_104(self, root: tk.Tk) -> None: #Costruttore
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

        self.root.after(100, None) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_105(self, root: tk.Tk) -> None: #Costruttore
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

        self.root.after(self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_106(self, root: tk.Tk) -> None: #Costruttore
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

        self.root.after(100, ) #ogni 100 millisecondi
        #eseguo process_messages

    #Si è impostata come applicazione "principale" la classe ZincApp, la quale fa partire la parte 
    #grafica. Creato il botttone "selectdirectory", esso fa partire a catena tutto il giro di elaborazione
    #dei dati.
    
    #Creo una classe che contiene i dati della GUI, pulsanti, stato dell'applicazione e funzioni associate
    def xǁZincAppǁ__init____mutmut_107(self, root: tk.Tk) -> None: #Costruttore
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

        self.root.after(101, self.process_messages) #ogni 100 millisecondi
        #eseguo process_messages

    @_mutmut_mutated(mutants_xǁZincAppǁwrite_log__mutmut)
    def write_log(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_orig(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_1(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(None, message + "\n")
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_2(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, None)
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_3(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(message + "\n")
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_4(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, )
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_5(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, message - "\n")
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_6(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, message + "XX\nXX")
        self.log_area.see(tk.END)

    def xǁZincAppǁwrite_log__mutmut_7(self, message: str) -> None:
        """Write a message to the GUI log area."""
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(None)

    @_mutmut_mutated(mutants_xǁZincAppǁselect_directory__mutmut)
    def select_directory(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_orig(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_1(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = None
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_2(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["XXvalueXX"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_3(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["VALUE"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_4(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 1
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_5(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = None

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_6(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["XXmaximumXX"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_7(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["MAXIMUM"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_8(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 101

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_9(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = None
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_10(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title=None)
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_11(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="XXSeleziona la cartella datiXX")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_12(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_13(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="SELEZIONA LA CARTELLA DATI")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_14(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_15(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log(None)
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_16(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("XXNessuna cartella selezionata.XX")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_17(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_18(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("NESSUNA CARTELLA SELEZIONATA.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

    def xǁZincAppǁselect_directory__mutmut_19(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = None
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

    def xǁZincAppǁselect_directory__mutmut_20(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title=None,
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

    def xǁZincAppǁselect_directory__mutmut_21(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile=None,
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

    def xǁZincAppǁselect_directory__mutmut_22(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=None,
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

    def xǁZincAppǁselect_directory__mutmut_23(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=None,
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

    def xǁZincAppǁselect_directory__mutmut_24(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
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

    def xǁZincAppǁselect_directory__mutmut_25(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
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

    def xǁZincAppǁselect_directory__mutmut_26(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
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

    def xǁZincAppǁselect_directory__mutmut_27(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
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

    def xǁZincAppǁselect_directory__mutmut_28(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="XXSalva il file con nomeXX",
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

    def xǁZincAppǁselect_directory__mutmut_29(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="salva il file con nome",
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

    def xǁZincAppǁselect_directory__mutmut_30(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="SALVA IL FILE CON NOME",
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

    def xǁZincAppǁselect_directory__mutmut_31(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="XXMisurazioni_Zinco.xlsxXX",
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

    def xǁZincAppǁselect_directory__mutmut_32(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="misurazioni_zinco.xlsx",
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

    def xǁZincAppǁselect_directory__mutmut_33(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="MISURAZIONI_ZINCO.XLSX",
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

    def xǁZincAppǁselect_directory__mutmut_34(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension="XX.xlsxXX",
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

    def xǁZincAppǁselect_directory__mutmut_35(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".XLSX",
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

    def xǁZincAppǁselect_directory__mutmut_36(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("XXFile ExcelXX", "*.xlsx")],
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

    def xǁZincAppǁselect_directory__mutmut_37(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("file excel", "*.xlsx")],
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

    def xǁZincAppǁselect_directory__mutmut_38(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("FILE EXCEL", "*.xlsx")],
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

    def xǁZincAppǁselect_directory__mutmut_39(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "XX*.xlsxXX")],
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

    def xǁZincAppǁselect_directory__mutmut_40(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.XLSX")],
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

    def xǁZincAppǁselect_directory__mutmut_41(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if output_file:
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

    def xǁZincAppǁselect_directory__mutmut_42(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if not output_file:
            self.write_log(None)
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

    def xǁZincAppǁselect_directory__mutmut_43(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if not output_file:
            self.write_log("XXSalvataggio annullato.XX")
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

    def xǁZincAppǁselect_directory__mutmut_44(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if not output_file:
            self.write_log("salvataggio annullato.")
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

    def xǁZincAppǁselect_directory__mutmut_45(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if not output_file:
            self.write_log("SALVATAGGIO ANNULLATO.")
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

    def xǁZincAppǁselect_directory__mutmut_46(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if not output_file:
            self.write_log("Salvataggio annullato.")
            return

        bs_files, ts_files = None
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

    def xǁZincAppǁselect_directory__mutmut_47(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
        output_file = filedialog.asksaveasfilename(
            title="Salva il file con nome",
            initialfile="Misurazioni_Zinco.xlsx",
            defaultextension=".xlsx",
            filetypes=[("File Excel", "*.xlsx")],
        )
        if not output_file:
            self.write_log("Salvataggio annullato.")
            return

        bs_files, ts_files = find_input_files(None)
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

    def xǁZincAppǁselect_directory__mutmut_48(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
        self.write_log(None)
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

    def xǁZincAppǁselect_directory__mutmut_49(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
        self.write_log(None)
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

    def xǁZincAppǁselect_directory__mutmut_50(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
        self.write_log(None)

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

    def xǁZincAppǁselect_directory__mutmut_51(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

        if bs_files:
            self.write_log("File Excel non trovato in cartella BS.")
            return

        self.select_button["state"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_52(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            self.write_log(None)
            return

        self.select_button["state"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_53(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            self.write_log("XXFile Excel non trovato in cartella BS.XX")
            return

        self.select_button["state"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_54(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            self.write_log("file excel non trovato in cartella bs.")
            return

        self.select_button["state"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_55(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            self.write_log("FILE EXCEL NON TROVATO IN CARTELLA BS.")
            return

        self.select_button["state"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_56(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

        self.select_button["state"] = None #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_57(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

        self.select_button["XXstateXX"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_58(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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

        self.select_button["STATE"] = tk.DISABLED #disabilito il pulsante di selezione della cartella
        worker = threading.Thread(
            target=self.run_analysis, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_59(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
        worker = None
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_60(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            target=None, #Una volta selezionata la cartella, passo i due file all'analisi
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_61(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            args=None,
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_62(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            daemon=None,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_63(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            args=(bs_files, ts_files, Path(output_file)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_64(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_65(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_66(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            args=(bs_files, ts_files, Path(None)),
            daemon=True,
        )
        worker.start()

    def xǁZincAppǁselect_directory__mutmut_67(self) -> None:
        """Select input/output paths and start analysis in a background thread."""
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        input_dir = filedialog.askdirectory(title="Seleziona la cartella dati")
        if not input_dir:
            self.write_log("Nessuna cartella selezionata.")
            return

        #Chiedo già all'inizio dell'applicazione dove salvare il file dei 
        #risultati all'utente
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
            daemon=False,
        )
        worker.start()

    @_mutmut_mutated(mutants_xǁZincAppǁrun_analysis__mutmut)
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

    def xǁZincAppǁrun_analysis__mutmut_orig(
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

    def xǁZincAppǁrun_analysis__mutmut_1(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(None)
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

    def xǁZincAppǁrun_analysis__mutmut_2(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("XXlogXX", "Elaborazione avviata."))
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

    def xǁZincAppǁrun_analysis__mutmut_3(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("LOG", "Elaborazione avviata."))
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

    def xǁZincAppǁrun_analysis__mutmut_4(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "XXElaborazione avviata.XX"))
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

    def xǁZincAppǁrun_analysis__mutmut_5(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "elaborazione avviata."))
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

    def xǁZincAppǁrun_analysis__mutmut_6(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "ELABORAZIONE AVVIATA."))
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

    def xǁZincAppǁrun_analysis__mutmut_7(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "Elaborazione avviata."))
            #Esegue i calcoli
            rows, errors = None
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

    def xǁZincAppǁrun_analysis__mutmut_8(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "Elaborazione avviata."))
            #Esegue i calcoli
            rows, errors = analyze_measurements(None, ts_files)
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

    def xǁZincAppǁrun_analysis__mutmut_9(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "Elaborazione avviata."))
            #Esegue i calcoli
            rows, errors = analyze_measurements(bs_files, None)
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

    def xǁZincAppǁrun_analysis__mutmut_10(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "Elaborazione avviata."))
            #Esegue i calcoli
            rows, errors = analyze_measurements(ts_files)
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

    def xǁZincAppǁrun_analysis__mutmut_11(
        self,
        bs_files: list[Path],
        ts_files: list[Path],
        output_file: Path,
    ) -> None:
        """Run the analysis outside the Tkinter main thread."""
        try:
            self.messages.put(("log", "Elaborazione avviata."))
            #Esegue i calcoli
            rows, errors = analyze_measurements(bs_files, )
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

    def xǁZincAppǁrun_analysis__mutmut_12(
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
            workbook = None
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

    def xǁZincAppǁrun_analysis__mutmut_13(
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
            workbook = create_result_workbook(None)
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

    def xǁZincAppǁrun_analysis__mutmut_14(
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
            workbook.save(None)

            for error in errors:
                self.messages.put(("log", error))

            self.messages.put(("progress", "100"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_15(
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
                self.messages.put(None)

            self.messages.put(("progress", "100"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_16(
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
                self.messages.put(("XXlogXX", error))

            self.messages.put(("progress", "100"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_17(
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
                self.messages.put(("LOG", error))

            self.messages.put(("progress", "100"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_18(
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

            self.messages.put(None)
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_19(
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

            self.messages.put(("XXprogressXX", "100"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_20(
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

            self.messages.put(("PROGRESS", "100"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_21(
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

            self.messages.put(("progress", "XX100XX"))
            self.messages.put(("log", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_22(
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
            self.messages.put(None)
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_23(
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
            self.messages.put(("XXlogXX", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_24(
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
            self.messages.put(("LOG", f"Elaborazione terminata: {output_file}"))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self.messages.put(("log", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_25(
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
            self.messages.put(None)
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_26(
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
            self.messages.put(("XXlogXX", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_27(
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
            self.messages.put(("LOG", f"Errore imprevisto durante l'elaborazione: {exc}"))
        finally:
            self.messages.put(("done", ""))

    def xǁZincAppǁrun_analysis__mutmut_28(
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
            self.messages.put(None)

    def xǁZincAppǁrun_analysis__mutmut_29(
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
            self.messages.put(("XXdoneXX", ""))

    def xǁZincAppǁrun_analysis__mutmut_30(
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
            self.messages.put(("DONE", ""))

    def xǁZincAppǁrun_analysis__mutmut_31(
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
            self.messages.put(("done", "XXXX"))

    @_mutmut_mutated(mutants_xǁZincAppǁprocess_messages__mutmut)
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

    def xǁZincAppǁprocess_messages__mutmut_orig(self) -> None:
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

    def xǁZincAppǁprocess_messages__mutmut_1(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while False:
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

    def xǁZincAppǁprocess_messages__mutmut_2(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = None
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_3(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                return

            if kind == "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_4(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind != "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_5(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "XXlogXX":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_6(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "LOG":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_7(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(None)
            elif kind == "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_8(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind != "progress":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_9(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "XXprogressXX":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_10(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "PROGRESS":
                self.progress_bar["value"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_11(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = None
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_12(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["XXvalueXX"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_13(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["VALUE"] = int(payload)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_14(self) -> None:
        """Apply worker messages on the Tkinter main thread."""
        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "log":
                self.write_log(payload)
            elif kind == "progress":
                self.progress_bar["value"] = int(None)
            elif kind == "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_15(self) -> None:
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
            elif kind != "done":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_16(self) -> None:
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
            elif kind == "XXdoneXX":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_17(self) -> None:
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
            elif kind == "DONE":
                self.select_button["state"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_18(self) -> None:
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
                self.select_button["state"] = None

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_19(self) -> None:
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
                self.select_button["XXstateXX"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_20(self) -> None:
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
                self.select_button["STATE"] = tk.NORMAL

        self.root.after(100, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_21(self) -> None:
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

        self.root.after(None, self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_22(self) -> None:
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

        self.root.after(100, None)

    def xǁZincAppǁprocess_messages__mutmut_23(self) -> None:
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

        self.root.after(self.process_messages)

    def xǁZincAppǁprocess_messages__mutmut_24(self) -> None:
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

        self.root.after(100, )

    def xǁZincAppǁprocess_messages__mutmut_25(self) -> None:
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

        self.root.after(101, self.process_messages)

mutants_xǁZincAppǁ__init____mutmut['_mutmut_orig'] = ZincApp.xǁZincAppǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_1'] = ZincApp.xǁZincAppǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_2'] = ZincApp.xǁZincAppǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_3'] = ZincApp.xǁZincAppǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_4'] = ZincApp.xǁZincAppǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_5'] = ZincApp.xǁZincAppǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_6'] = ZincApp.xǁZincAppǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_7'] = ZincApp.xǁZincAppǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_8'] = ZincApp.xǁZincAppǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_9'] = ZincApp.xǁZincAppǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_10'] = ZincApp.xǁZincAppǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_11'] = ZincApp.xǁZincAppǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_12'] = ZincApp.xǁZincAppǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_13'] = ZincApp.xǁZincAppǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_14'] = ZincApp.xǁZincAppǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_15'] = ZincApp.xǁZincAppǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_16'] = ZincApp.xǁZincAppǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_17'] = ZincApp.xǁZincAppǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_18'] = ZincApp.xǁZincAppǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_19'] = ZincApp.xǁZincAppǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_20'] = ZincApp.xǁZincAppǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_21'] = ZincApp.xǁZincAppǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_22'] = ZincApp.xǁZincAppǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_23'] = ZincApp.xǁZincAppǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_24'] = ZincApp.xǁZincAppǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_25'] = ZincApp.xǁZincAppǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_26'] = ZincApp.xǁZincAppǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_27'] = ZincApp.xǁZincAppǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_28'] = ZincApp.xǁZincAppǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_29'] = ZincApp.xǁZincAppǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_30'] = ZincApp.xǁZincAppǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_31'] = ZincApp.xǁZincAppǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_32'] = ZincApp.xǁZincAppǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_33'] = ZincApp.xǁZincAppǁ__init____mutmut_33 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_34'] = ZincApp.xǁZincAppǁ__init____mutmut_34 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_35'] = ZincApp.xǁZincAppǁ__init____mutmut_35 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_36'] = ZincApp.xǁZincAppǁ__init____mutmut_36 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_37'] = ZincApp.xǁZincAppǁ__init____mutmut_37 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_38'] = ZincApp.xǁZincAppǁ__init____mutmut_38 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_39'] = ZincApp.xǁZincAppǁ__init____mutmut_39 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_40'] = ZincApp.xǁZincAppǁ__init____mutmut_40 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_41'] = ZincApp.xǁZincAppǁ__init____mutmut_41 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_42'] = ZincApp.xǁZincAppǁ__init____mutmut_42 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_43'] = ZincApp.xǁZincAppǁ__init____mutmut_43 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_44'] = ZincApp.xǁZincAppǁ__init____mutmut_44 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_45'] = ZincApp.xǁZincAppǁ__init____mutmut_45 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_46'] = ZincApp.xǁZincAppǁ__init____mutmut_46 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_47'] = ZincApp.xǁZincAppǁ__init____mutmut_47 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_48'] = ZincApp.xǁZincAppǁ__init____mutmut_48 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_49'] = ZincApp.xǁZincAppǁ__init____mutmut_49 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_50'] = ZincApp.xǁZincAppǁ__init____mutmut_50 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_51'] = ZincApp.xǁZincAppǁ__init____mutmut_51 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_52'] = ZincApp.xǁZincAppǁ__init____mutmut_52 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_53'] = ZincApp.xǁZincAppǁ__init____mutmut_53 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_54'] = ZincApp.xǁZincAppǁ__init____mutmut_54 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_55'] = ZincApp.xǁZincAppǁ__init____mutmut_55 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_56'] = ZincApp.xǁZincAppǁ__init____mutmut_56 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_57'] = ZincApp.xǁZincAppǁ__init____mutmut_57 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_58'] = ZincApp.xǁZincAppǁ__init____mutmut_58 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_59'] = ZincApp.xǁZincAppǁ__init____mutmut_59 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_60'] = ZincApp.xǁZincAppǁ__init____mutmut_60 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_61'] = ZincApp.xǁZincAppǁ__init____mutmut_61 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_62'] = ZincApp.xǁZincAppǁ__init____mutmut_62 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_63'] = ZincApp.xǁZincAppǁ__init____mutmut_63 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_64'] = ZincApp.xǁZincAppǁ__init____mutmut_64 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_65'] = ZincApp.xǁZincAppǁ__init____mutmut_65 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_66'] = ZincApp.xǁZincAppǁ__init____mutmut_66 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_67'] = ZincApp.xǁZincAppǁ__init____mutmut_67 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_68'] = ZincApp.xǁZincAppǁ__init____mutmut_68 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_69'] = ZincApp.xǁZincAppǁ__init____mutmut_69 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_70'] = ZincApp.xǁZincAppǁ__init____mutmut_70 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_71'] = ZincApp.xǁZincAppǁ__init____mutmut_71 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_72'] = ZincApp.xǁZincAppǁ__init____mutmut_72 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_73'] = ZincApp.xǁZincAppǁ__init____mutmut_73 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_74'] = ZincApp.xǁZincAppǁ__init____mutmut_74 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_75'] = ZincApp.xǁZincAppǁ__init____mutmut_75 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_76'] = ZincApp.xǁZincAppǁ__init____mutmut_76 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_77'] = ZincApp.xǁZincAppǁ__init____mutmut_77 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_78'] = ZincApp.xǁZincAppǁ__init____mutmut_78 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_79'] = ZincApp.xǁZincAppǁ__init____mutmut_79 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_80'] = ZincApp.xǁZincAppǁ__init____mutmut_80 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_81'] = ZincApp.xǁZincAppǁ__init____mutmut_81 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_82'] = ZincApp.xǁZincAppǁ__init____mutmut_82 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_83'] = ZincApp.xǁZincAppǁ__init____mutmut_83 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_84'] = ZincApp.xǁZincAppǁ__init____mutmut_84 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_85'] = ZincApp.xǁZincAppǁ__init____mutmut_85 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_86'] = ZincApp.xǁZincAppǁ__init____mutmut_86 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_87'] = ZincApp.xǁZincAppǁ__init____mutmut_87 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_88'] = ZincApp.xǁZincAppǁ__init____mutmut_88 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_89'] = ZincApp.xǁZincAppǁ__init____mutmut_89 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_90'] = ZincApp.xǁZincAppǁ__init____mutmut_90 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_91'] = ZincApp.xǁZincAppǁ__init____mutmut_91 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_92'] = ZincApp.xǁZincAppǁ__init____mutmut_92 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_93'] = ZincApp.xǁZincAppǁ__init____mutmut_93 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_94'] = ZincApp.xǁZincAppǁ__init____mutmut_94 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_95'] = ZincApp.xǁZincAppǁ__init____mutmut_95 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_96'] = ZincApp.xǁZincAppǁ__init____mutmut_96 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_97'] = ZincApp.xǁZincAppǁ__init____mutmut_97 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_98'] = ZincApp.xǁZincAppǁ__init____mutmut_98 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_99'] = ZincApp.xǁZincAppǁ__init____mutmut_99 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_100'] = ZincApp.xǁZincAppǁ__init____mutmut_100 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_101'] = ZincApp.xǁZincAppǁ__init____mutmut_101 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_102'] = ZincApp.xǁZincAppǁ__init____mutmut_102 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_103'] = ZincApp.xǁZincAppǁ__init____mutmut_103 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_104'] = ZincApp.xǁZincAppǁ__init____mutmut_104 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_105'] = ZincApp.xǁZincAppǁ__init____mutmut_105 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_106'] = ZincApp.xǁZincAppǁ__init____mutmut_106 # type: ignore # mutmut generated
mutants_xǁZincAppǁ__init____mutmut['xǁZincAppǁ__init____mutmut_107'] = ZincApp.xǁZincAppǁ__init____mutmut_107 # type: ignore # mutmut generated

mutants_xǁZincAppǁwrite_log__mutmut['_mutmut_orig'] = ZincApp.xǁZincAppǁwrite_log__mutmut_orig # type: ignore # mutmut generated
mutants_xǁZincAppǁwrite_log__mutmut['xǁZincAppǁwrite_log__mutmut_1'] = ZincApp.xǁZincAppǁwrite_log__mutmut_1 # type: ignore # mutmut generated
mutants_xǁZincAppǁwrite_log__mutmut['xǁZincAppǁwrite_log__mutmut_2'] = ZincApp.xǁZincAppǁwrite_log__mutmut_2 # type: ignore # mutmut generated
mutants_xǁZincAppǁwrite_log__mutmut['xǁZincAppǁwrite_log__mutmut_3'] = ZincApp.xǁZincAppǁwrite_log__mutmut_3 # type: ignore # mutmut generated
mutants_xǁZincAppǁwrite_log__mutmut['xǁZincAppǁwrite_log__mutmut_4'] = ZincApp.xǁZincAppǁwrite_log__mutmut_4 # type: ignore # mutmut generated
mutants_xǁZincAppǁwrite_log__mutmut['xǁZincAppǁwrite_log__mutmut_5'] = ZincApp.xǁZincAppǁwrite_log__mutmut_5 # type: ignore # mutmut generated
mutants_xǁZincAppǁwrite_log__mutmut['xǁZincAppǁwrite_log__mutmut_6'] = ZincApp.xǁZincAppǁwrite_log__mutmut_6 # type: ignore # mutmut generated
mutants_xǁZincAppǁwrite_log__mutmut['xǁZincAppǁwrite_log__mutmut_7'] = ZincApp.xǁZincAppǁwrite_log__mutmut_7 # type: ignore # mutmut generated

mutants_xǁZincAppǁselect_directory__mutmut['_mutmut_orig'] = ZincApp.xǁZincAppǁselect_directory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_1'] = ZincApp.xǁZincAppǁselect_directory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_2'] = ZincApp.xǁZincAppǁselect_directory__mutmut_2 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_3'] = ZincApp.xǁZincAppǁselect_directory__mutmut_3 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_4'] = ZincApp.xǁZincAppǁselect_directory__mutmut_4 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_5'] = ZincApp.xǁZincAppǁselect_directory__mutmut_5 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_6'] = ZincApp.xǁZincAppǁselect_directory__mutmut_6 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_7'] = ZincApp.xǁZincAppǁselect_directory__mutmut_7 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_8'] = ZincApp.xǁZincAppǁselect_directory__mutmut_8 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_9'] = ZincApp.xǁZincAppǁselect_directory__mutmut_9 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_10'] = ZincApp.xǁZincAppǁselect_directory__mutmut_10 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_11'] = ZincApp.xǁZincAppǁselect_directory__mutmut_11 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_12'] = ZincApp.xǁZincAppǁselect_directory__mutmut_12 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_13'] = ZincApp.xǁZincAppǁselect_directory__mutmut_13 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_14'] = ZincApp.xǁZincAppǁselect_directory__mutmut_14 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_15'] = ZincApp.xǁZincAppǁselect_directory__mutmut_15 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_16'] = ZincApp.xǁZincAppǁselect_directory__mutmut_16 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_17'] = ZincApp.xǁZincAppǁselect_directory__mutmut_17 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_18'] = ZincApp.xǁZincAppǁselect_directory__mutmut_18 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_19'] = ZincApp.xǁZincAppǁselect_directory__mutmut_19 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_20'] = ZincApp.xǁZincAppǁselect_directory__mutmut_20 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_21'] = ZincApp.xǁZincAppǁselect_directory__mutmut_21 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_22'] = ZincApp.xǁZincAppǁselect_directory__mutmut_22 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_23'] = ZincApp.xǁZincAppǁselect_directory__mutmut_23 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_24'] = ZincApp.xǁZincAppǁselect_directory__mutmut_24 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_25'] = ZincApp.xǁZincAppǁselect_directory__mutmut_25 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_26'] = ZincApp.xǁZincAppǁselect_directory__mutmut_26 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_27'] = ZincApp.xǁZincAppǁselect_directory__mutmut_27 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_28'] = ZincApp.xǁZincAppǁselect_directory__mutmut_28 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_29'] = ZincApp.xǁZincAppǁselect_directory__mutmut_29 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_30'] = ZincApp.xǁZincAppǁselect_directory__mutmut_30 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_31'] = ZincApp.xǁZincAppǁselect_directory__mutmut_31 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_32'] = ZincApp.xǁZincAppǁselect_directory__mutmut_32 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_33'] = ZincApp.xǁZincAppǁselect_directory__mutmut_33 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_34'] = ZincApp.xǁZincAppǁselect_directory__mutmut_34 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_35'] = ZincApp.xǁZincAppǁselect_directory__mutmut_35 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_36'] = ZincApp.xǁZincAppǁselect_directory__mutmut_36 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_37'] = ZincApp.xǁZincAppǁselect_directory__mutmut_37 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_38'] = ZincApp.xǁZincAppǁselect_directory__mutmut_38 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_39'] = ZincApp.xǁZincAppǁselect_directory__mutmut_39 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_40'] = ZincApp.xǁZincAppǁselect_directory__mutmut_40 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_41'] = ZincApp.xǁZincAppǁselect_directory__mutmut_41 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_42'] = ZincApp.xǁZincAppǁselect_directory__mutmut_42 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_43'] = ZincApp.xǁZincAppǁselect_directory__mutmut_43 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_44'] = ZincApp.xǁZincAppǁselect_directory__mutmut_44 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_45'] = ZincApp.xǁZincAppǁselect_directory__mutmut_45 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_46'] = ZincApp.xǁZincAppǁselect_directory__mutmut_46 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_47'] = ZincApp.xǁZincAppǁselect_directory__mutmut_47 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_48'] = ZincApp.xǁZincAppǁselect_directory__mutmut_48 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_49'] = ZincApp.xǁZincAppǁselect_directory__mutmut_49 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_50'] = ZincApp.xǁZincAppǁselect_directory__mutmut_50 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_51'] = ZincApp.xǁZincAppǁselect_directory__mutmut_51 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_52'] = ZincApp.xǁZincAppǁselect_directory__mutmut_52 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_53'] = ZincApp.xǁZincAppǁselect_directory__mutmut_53 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_54'] = ZincApp.xǁZincAppǁselect_directory__mutmut_54 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_55'] = ZincApp.xǁZincAppǁselect_directory__mutmut_55 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_56'] = ZincApp.xǁZincAppǁselect_directory__mutmut_56 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_57'] = ZincApp.xǁZincAppǁselect_directory__mutmut_57 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_58'] = ZincApp.xǁZincAppǁselect_directory__mutmut_58 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_59'] = ZincApp.xǁZincAppǁselect_directory__mutmut_59 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_60'] = ZincApp.xǁZincAppǁselect_directory__mutmut_60 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_61'] = ZincApp.xǁZincAppǁselect_directory__mutmut_61 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_62'] = ZincApp.xǁZincAppǁselect_directory__mutmut_62 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_63'] = ZincApp.xǁZincAppǁselect_directory__mutmut_63 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_64'] = ZincApp.xǁZincAppǁselect_directory__mutmut_64 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_65'] = ZincApp.xǁZincAppǁselect_directory__mutmut_65 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_66'] = ZincApp.xǁZincAppǁselect_directory__mutmut_66 # type: ignore # mutmut generated
mutants_xǁZincAppǁselect_directory__mutmut['xǁZincAppǁselect_directory__mutmut_67'] = ZincApp.xǁZincAppǁselect_directory__mutmut_67 # type: ignore # mutmut generated

mutants_xǁZincAppǁrun_analysis__mutmut['_mutmut_orig'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_orig # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_1'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_1 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_2'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_2 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_3'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_3 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_4'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_4 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_5'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_5 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_6'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_6 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_7'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_7 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_8'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_8 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_9'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_9 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_10'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_10 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_11'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_11 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_12'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_12 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_13'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_13 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_14'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_14 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_15'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_15 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_16'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_16 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_17'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_17 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_18'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_18 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_19'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_19 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_20'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_20 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_21'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_21 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_22'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_22 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_23'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_23 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_24'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_24 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_25'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_25 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_26'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_26 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_27'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_27 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_28'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_28 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_29'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_29 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_30'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_30 # type: ignore # mutmut generated
mutants_xǁZincAppǁrun_analysis__mutmut['xǁZincAppǁrun_analysis__mutmut_31'] = ZincApp.xǁZincAppǁrun_analysis__mutmut_31 # type: ignore # mutmut generated

mutants_xǁZincAppǁprocess_messages__mutmut['_mutmut_orig'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_orig # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_1'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_1 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_2'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_2 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_3'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_3 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_4'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_4 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_5'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_5 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_6'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_6 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_7'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_7 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_8'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_8 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_9'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_9 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_10'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_10 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_11'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_11 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_12'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_12 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_13'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_13 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_14'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_14 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_15'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_15 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_16'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_16 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_17'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_17 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_18'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_18 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_19'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_19 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_20'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_20 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_21'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_21 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_22'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_22 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_23'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_23 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_24'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_24 # type: ignore # mutmut generated
mutants_xǁZincAppǁprocess_messages__mutmut['xǁZincAppǁprocess_messages__mutmut_25'] = ZincApp.xǁZincAppǁprocess_messages__mutmut_25 # type: ignore # mutmut generated
mutants_x_configure_windows_dpi__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_configure_windows_dpi__mutmut)
def configure_windows_dpi() -> None:
    """Improve Tkinter rendering on Windows when the API is available."""
    if windll is None:
        return
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    except (AttributeError, OSError):
        pass


def x_configure_windows_dpi__mutmut_orig() -> None:
    """Improve Tkinter rendering on Windows when the API is available."""
    if windll is None:
        return
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    except (AttributeError, OSError):
        pass


def x_configure_windows_dpi__mutmut_1() -> None:
    """Improve Tkinter rendering on Windows when the API is available."""
    if windll is not None:
        return
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    except (AttributeError, OSError):
        pass


def x_configure_windows_dpi__mutmut_2() -> None:
    """Improve Tkinter rendering on Windows when the API is available."""
    if windll is None:
        return
    try:
        windll.shcore.SetProcessDpiAwareness(None)
    except (AttributeError, OSError):
        pass


def x_configure_windows_dpi__mutmut_3() -> None:
    """Improve Tkinter rendering on Windows when the API is available."""
    if windll is None:
        return
    try:
        windll.shcore.SetProcessDpiAwareness(2)
    except (AttributeError, OSError):
        pass

mutants_x_configure_windows_dpi__mutmut['_mutmut_orig'] = x_configure_windows_dpi__mutmut_orig # type: ignore # mutmut generated
mutants_x_configure_windows_dpi__mutmut['x_configure_windows_dpi__mutmut_1'] = x_configure_windows_dpi__mutmut_1 # type: ignore # mutmut generated
mutants_x_configure_windows_dpi__mutmut['x_configure_windows_dpi__mutmut_2'] = x_configure_windows_dpi__mutmut_2 # type: ignore # mutmut generated
mutants_x_configure_windows_dpi__mutmut['x_configure_windows_dpi__mutmut_3'] = x_configure_windows_dpi__mutmut_3 # type: ignore # mutmut generated
mutants_x_main__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_main__mutmut)
def main() -> None:
    """Start dell'applicazione"""
    configure_windows_dpi()
    root = tk.Tk()
    ZincApp(root)
    root.mainloop()


def x_main__mutmut_orig() -> None:
    """Start dell'applicazione"""
    configure_windows_dpi()
    root = tk.Tk()
    ZincApp(root)
    root.mainloop()


def x_main__mutmut_1() -> None:
    """Start dell'applicazione"""
    configure_windows_dpi()
    root = None
    ZincApp(root)
    root.mainloop()


def x_main__mutmut_2() -> None:
    """Start dell'applicazione"""
    configure_windows_dpi()
    root = tk.Tk()
    ZincApp(None)
    root.mainloop()

mutants_x_main__mutmut['_mutmut_orig'] = x_main__mutmut_orig # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_1'] = x_main__mutmut_1 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_2'] = x_main__mutmut_2 # type: ignore # mutmut generated
