# Postup

1. vytvoření `zadani.md` se zadáním úloh
2. vytvoření složky `/tests`
3. vytvoření jednotkových testů pro každou úlohu, `tests/test_Uxy.py` (celkem 6 souborů, 26 testů)
4. vytvoření wrapper skriptu `track_solutions.py`
5. vytvoření `/solutions/Uxy.py` filů pro každou úlohu s předepsanou funkcí `def ...(): pass`

### Struktura projektu
/solutions/
    u1a.py       # řešení Piškvorky
    u1b.py       # řešení Kámen-nůžky-papír
    u2a.py       # řešení známky
    u2b.py       # řešení tržby
    u3a.py       # řešení FizzBuzz
    u3b.py       # řešení Palindrom

/tests/
    test_U1A_piskvorky.py
    test_U1B_kamen_nuzky_papir.py
    test_U2A_znamky.py
    test_U2B_trzby.py
    test_U3A_fizzbuzz.py
    test_U3B_palindrom.py

track_solution.py   ...

┌──────────────────────────┐
│      track_solution.py   │
│  - sleduje změny souboru │
│  - spouští testy         │
│  - měří čas a iterace    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   solutions/u3b.py       │   <-- (příklad úlohy - Palindrom)
│  - tvoje řešení úlohy    │
│  - funkce is_palindrom() │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   tests/test_U3B_palindrom.py │
│  - importuje u3b.py      │
│  - spouští unittesty     │
│  - ověřuje správnost     │
└────────────┬─────────────┘
             │
             ▼
      Výsledek testu:
   ┌──────────────────────┐
   │  ❌ Test fail → čekám │
   │  ✅ Test success →   │
   │     - vypíšu čas     │
   │     - počet iterací  │
   └──────────────────────┘
