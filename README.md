# ZMTransform

Per conto di Marcegaglia Ravenna, il più grande stabilimento metallurgico del gruppo e il principale polo logistico intermodale dell’azienda, nasce l’esigenza di sviluppare uno strumento software dedicato alla lettura, all’elaborazione e all’analisi dei dati relativi ai rivestimenti di zinco applicati sui coil prodotti presso lo stabilimento situato in Tunisia.

ZMTransform è un’applicazione sviluppata in Python per l’analisi automatizzata delle misure di zincatura rilevate sui materiali lavorati. Il sistema consente di acquisire i dati provenienti dai file Excel generati dal processo produttivo, elaborarli in modo strutturato e produrre report riepilogativi utili al controllo qualità e all’analisi delle prestazioni del processo di zincatura.

## Funzionalita'

- Interfaccia desktop Tkinter per uso manuale.
- Modalita' CLI per esecuzioni automatiche, CI e container.
- Lettura delle cartelle `BS/` e `TS/`.
- Matching BS/TS tramite cella `Values!B5`.
- Calcolo di media, deviazione standard, minimo e massimo da `LengthProfiles`.
- Generazione workbook finale con foglio `Dati`.
- Test unitari, test di integrazione e misura di copertura.
- Pipeline CI/CD con lint, test e coverage.
- Dockerfile per deployment batch in container.

## Struttura attesa dei dati

```text
dati/
  BS/
    coil_001.xlsx
  TS/
    coil_001.xlsx
```

Ogni file Excel deve contenere:

- foglio `Values`
- cella `B2`: data/ora misura
- cella `B4`: valore nominale
- cella `B5`: `CoilID`
- foglio `LengthProfiles`
- colonna 1: progressiva/lunghezza
- colonna 2: valori numerici di misura, dalla riga 2

## Avvio applicazione desktop

```powershell
python main.py
```

oppure, dopo installazione del package:

```powershell
zmtransform-gui
```

## Uso CLI

```powershell
zmtransform .\dati .\out\Misurazioni_Zinco.xlsx
```

La CLI restituisce codice `0` se tutti i file sono validi, `1` se alcuni file sono stati
scartati per errori di formato.

## Ambiente di sviluppo

```powershell
python -m pip install -e .[dev]
pytest
coverage run -m pytest
coverage report
ruff check .
pylint src tests
```

## Docker

Build:

```powershell
docker build -t zmtransform .
```

Esecuzione batch:

```powershell
docker run --rm -v ${PWD}\dati:/data -v ${PWD}\out:/out zmtransform /data /out/Misurazioni_Zinco.xlsx
```

## Requisiti d'esame coperti

- Complessita': GUI desktop, CLI batch, parsing Excel, matching BS/TS, validazione e report.
- Repository strutturato: package `src/`, test separati, documentazione, CI, Docker.
- Specifica: vedere `docs/SPECIFICA.md`.
- Test unita': `tests/unit`.
- Test integrazione: `tests/integration`.
- Coverage: configurazione in `pyproject.toml`.
- CI/CD: workflow GitHub Actions in `.github/workflows/ci.yml`.
- Container: `Dockerfile` per esecuzione batch.
