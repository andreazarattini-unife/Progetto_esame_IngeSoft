# Specifica parziale di progetto

## Obiettivo

ZMTransform supporta l'analisi di misure di zincatura provenienti da file Excel BS e TS.
L'obiettivo e' ridurre il lavoro manuale di confronto, calcolo statistico e produzione
del riepilogo finale.

## Attori

- Operatore qualita': seleziona una cartella dati e produce il report Excel.
- Sistema CI/CD: esegue automaticamente lint, test e coverage.
- Processo batch/container: esegue l'analisi da riga di comando.

## Requisiti funzionali

| ID | Requisito |
| --- | --- |
| RF1 | Il sistema deve leggere file `.xlsx` dalle sottocartelle `BS` e `TS`. |
| RF2 | Il sistema deve estrarre `CoilID`, data/ora, nominale e profilo misure. |
| RF3 | Il sistema deve abbinare un file BS al corrispondente file TS tramite `CoilID`. |
| RF4 | Il sistema deve calcolare media, deviazione standard, minimo e massimo. |
| RF5 | Il sistema deve generare un workbook Excel con un foglio `Dati`. |
| RF6 | Il sistema deve segnalare i file non validi senza interrompere l'intera analisi. |
| RF7 | Il sistema deve essere eseguibile sia tramite GUI sia tramite CLI. |

## Requisiti non funzionali

| ID | Requisito |
| --- | --- |
| RNF1 | La logica di dominio deve essere separata dall'interfaccia grafica. |
| RNF2 | Il progetto deve avere test unitari e test di integrazione. |
| RNF3 | La pipeline CI deve eseguire lint, test e coverage. |
| RNF4 | La modalita' batch deve essere containerizzabile. |
| RNF5 | Il codice deve essere organizzato come package Python installabile. |

## Casi d'uso principali

### UC1 - Analisi manuale da GUI

1. L'operatore avvia l'applicazione.
2. Seleziona la cartella contenente `BS/` e `TS/`.
3. Sceglie il percorso del file di output.
4. Il sistema analizza i file e salva il workbook riepilogativo.
5. Il sistema mostra eventuali errori nel log.

### UC2 - Analisi automatica da CLI

1. L'utente esegue `zmtransform INPUT_DIR OUTPUT_FILE`.
2. Il sistema analizza le sottocartelle `BS/` e `TS/`.
3. Il sistema salva il workbook di output.
4. Il processo restituisce codice `0` se non ci sono errori, `1` altrimenti.

## Decisioni architetturali

- `zmtransform.analysis`: logica di dominio, parsing Excel, matching e generazione report.
- `zmtransform.models`: dataclass immutabili per risultati intermedi.
- `zmtransform.gui`: interfaccia Tkinter.
- `zmtransform.cli`: entry point batch per CI e Docker.
- `tests/unit`: verifica funzioni isolate.
- `tests/integration`: verifica flussi completi con workbook temporanei.
