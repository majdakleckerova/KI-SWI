# Řešení

## 1. Logické úlohy

### U1A – Piškvorky (lidský partner)
```python
def check_winner(board: list[list[str]]) -> str | None:
    # Zkontroluj řádky
    for row in board:
        if row[0] != "" and row[0] == row[1] == row[2]:
            return row[0]
    
    # Zkontroluj sloupce
    for col in range(3):
        if board[0][col] != "" and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    # Zkontroluj diagonály
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None
```

**Styl řešení:** Lidský partner  
**Doba potřebná k úspěšnému projití testy:** 28 minut  
**Počet iterací:** 6x spuštění testu

---

### U1B – Kámen-nůžky-papír (GitHub Copilot)
```python
import random

def get_winner(player_choice: str, ai_choice: str) -> str:
    if player_choice == ai_choice:
        return "draw"
    if (player_choice == "rock" and ai_choice == "scissors") or \
       (player_choice == "scissors" and ai_choice == "paper") or \
       (player_choice == "paper" and ai_choice == "rock"):
        return "player"
    return "ai"

def play_game():
    player_score = 0
    ai_score = 0

    while player_score < 3 and ai_score < 3:
        player_choice = input("rock, paper, scissors: ").lower()
        ai_choice = random.choice(["rock", "paper", "scissors"])
        winner = get_winner(player_choice, ai_choice)
        print(f"You chose {player_choice}, AI chose {ai_choice}. Result: {winner}")

        if winner == "player":
            player_score += 1
        elif winner == "ai":
            ai_score += 1
        
        print(f"Score - You: {player_score}, AI: {ai_score}")

    print("Game over!")
```

**Styl řešení:** GitHub Copilot  
**Doba potřebná k úspěšnému projití testy:** 12 minut  
**Počet iterací:** 3x spuštění testu

---

## 2. Práce s daty

### U2A – Průměrné známky (lidský partner)
```python
import pandas as pd

def prumer_znamek(df: pd.DataFrame) -> pd.Series:
    df["znamka"] = pd.to_numeric(df["znamka"], errors="coerce")
    prumerne_znamky = df.groupby("predmet")["znamka"].mean()
    
    return prumerne_znamky
```

**Styl řešení:** Lidský partner  
**Doba potřebná k úspěšnému projití testy:** 10 minut  
**Počet iterací:** 2x spuštění testu

---

### U2B – Tržby za zákazníky (GitHub Copilot)
```python
import pandas as pd

def trzby_za_zakazniky(df: pd.DataFrame) -> pd.Series:
    # filtr 2024
    df["datum"] = pd.to_datetime(df["datum"])
    df_2024 = df[df["datum"].dt.year == 2024]
    
    # trzba == mnozstvi * cena
    df_2024["trzba"] = df_2024["mnozstvi"] * df_2024["cena"]
    
    # agregace podle zakaznika
    trzby = df_2024.groupby("zakaznik")["trzba"].sum()
    
    return trzby
```

**Styl řešení:** GitHub Copilot  
**Doba potřebná k úspěšnému projití testy:** 6 minut  
**Počet iterací:** 1x spuštění testu

---

## 3. Algoritmické úlohy

### U3A – FizzBuzz (lidský partner)
```python
def fizzbuzz(start: int, end: int) -> list[str]:
    vysledky = []
    for cislo in range(start, end):
        if cislo % 3 == 0 and cislo % 5 == 0:
            vysledky.append("FizzBuzz")
        elif cislo % 3 == 0:
            vysledky.append("Fizz")
        elif cislo % 5 == 0:
            vysledky.append("Buzz")
        else:
            vysledky.append(str(cislo))
    return vysledky
```

**Styl řešení:** Lidský partner  
**Doba potřebná k úspěšnému projití testy:** 12 minut  
**Počet iterací:** 3x spuštění testu

---

### U3B – Palindrom (GitHub Copilot)
```python
def is_palindrom(s: str) -> bool:
    s_clean = s.replace(" ", "").lower()
    return s_clean == s_clean[::-1]
```

**Styl řešení:** GitHub Copilot  
**Doba potřebná k úspěšnému projití testy:** 3 minut  
**Počet iterací:** 1x spuštění testu

---

## Shrnutí výsledků

| Úloha | Kategorie       | Styl řešení     | Čas (min) | Iterace | Komentář |
|-------|------------------|------------------|-----------|----------|----------|
| U1A   | Logická          | Lidský partner   | 28        | 6        | Delší diskuse o logice a validaci vstupů, více oprav v průběhu. |
| U1B   | Logická          | GitHub Copilot   | 12        | 3        | Copilot dobře navrhl strukturu, úpravy se týkaly hlavně vstupu a výpisu. |
| U2A   | Práce s daty     | Lidský partner   | 10        | 2        | Rychlé, ale vyžadovalo zamyšlení nad převodem dat a groupby logikou. |
| U2B   | Práce s daty     | GitHub Copilot   | 6         | 1        | Copilot navrhl skoro celý kód správně, pouze drobné ladění syntaxe. |
| U3A   | Algoritmická     | Lidský partner   | 12        | 3        | Známá úloha, ale potřeba ručně ošetřit podmínky a správně ladit výstup. |
| U3B   | Algoritmická     | GitHub Copilot   | 3         | 1        | Copilot navrhl celé řešení přesně, nebylo potřeba nic měnit. |

## Subjektivní hodnocení kvality kódu (Jan Čmuchař)

| Úloha | Styl řešení     | Srozumitelnost | Technická kvalita | Celkové skóre |
|-------|------------------|----------------|--------------------|----------------|
| U1A   | Lidský partner   | 4              | 3                  | 7 / 10         |
| U1B   | GitHub Copilot   | 5              | 4                  | 9 / 10         |
| U2A   | Lidský partner   | 4              | 4                  | 8 / 10         |
| U2B   | GitHub Copilot   | 5              | 5                  | 10 / 10        |
| U3A   | Lidský partner   | 4              | 3                  | 7 / 10         |
| U3B   | GitHub Copilot   | 5              | 4                  | 9 / 10         |

## Introspektivní hodnocení po dokončení každé úlohy

| Úloha | Styl řešení     | PAS – míra úzkosti (1–5) | IMI – motivace (1–5) | CLS – vnímaná spolupráce (1–5) |
|-------|------------------|---------------------------|-----------------------|-------------------------------|
| U1A   | Lidský partner   | 3.4                       | 4.5                   | 4.8                           |
| U1B   | GitHub Copilot   | 2.2                       | 4.2                   | 3.7                           |
| U2A   | Lidský partner   | 3.1                       | 4.3                   | 4.5                           |
| U2B   | GitHub Copilot   | 1.9                       | 4.0                   | 3.5                           |
| U3A   | Lidský partner   | 3.3                       | 4.6                   | 4.9                           |
| U3B   | GitHub Copilot   | 2.1                       | 4.1                   | 3.6                           |
