# Postup

1. vytvoření `zadani.md` se zadáním úloh
2. vytvoření složky `/tests`
3. vytvoření jednotkových testů pro každou úlohu, `tests/test_Uxy.py` (celkem 6 souborů, 26 testů)
4. vytvoření wrapper skriptu `track_solutions.py`
5. vytvoření `/solutions/Uxy.py` filů pro každou úlohu s předepsanou funkcí `def ...(): pass`

### Struktura projektu
```bash
KI-SWI/
├── solutions/                
│   ├── u1a.py                
│   ├── u3b.py                
│
├── tests/                    # testovací skripty
│   ├── test_U1A_piskvorky.py
│   ├── test_U3B_palindrom.py
│
├── track_solution.py         # měření času + iterací
├── README.md                 # návod
├── zadani.md                 # zadání úloh
```

## Spuštění testu
```bash
python3 -m tests/test_U1A.py
```
## Postup
1. Otevři řešení úlohy v `/solutions`
2. Spusť trackovací skript v terminálu
```bash
python3 track_solution.py solutions/U3B.py tests/test_U3B.py
```
3. Vyřeš úlohu, po každém uložení se automaticky spustí test
4. Sleduj výstup v terminálu
5. Jestli test selže, opravuj funkci a znovu ukládej – skript pokaždé test znovu spustí a počítá iterace.
6. Jakmile test projde, terminál vypíše: Testy úspěšné, Počet iterací, Celkový čas od první úpravy


