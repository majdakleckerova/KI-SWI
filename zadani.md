# Zadání úloh

## 1. Logické úlohy

### U1A – Piškvorky
Implementujte konzolovou verzi hry **Piškvorky** pro **dva** hráče. Hraje se na poli velikosti **3x3**. Hráči se střídají v zadávání souřadnic svého tahu (řádek, sloupec). Po každém tahu program zkontroluje, zda někdo nevyhrál, případně zda nenastala remíza. Vítěz je hráč, který umístí tři své symboly **(X nebo O)** do řady – vodorovně, svisle nebo diagonálně. Program musí umožnit restart hry.

`funkce check_winner(board: list[list[str]]) -> str | None, která přijme aktuální stav herní desky a vrátí "X" nebo "O" při výhře, nebo None, pokud není vítěz.`

### U1B - Kámen-nůžky-papír
úkolem je vytvořit konzolovou aplikaci pro hru **Kámen-nůžky-papír** proti počítači, kde vítězem se stává ten, kdo jako první vyhraje **3** kola.
Počítač vybírá svůj tah **náhodně**. Po každém kole program vypíše výsledek kola a průběžné skóre. Hra končí, jakmile hráč nebo počítač dosáhne **3** vítězství.

`funkce get_winner(player_choice: str, ai_choice: str) -> str, která vrátí "player", "ai" nebo "draw".
Celkovou hru ovládá cyklus, který udržuje skóre a ukončí se při dosažení 3 vítězství.`

---

## 2. Práce s daty

### U2A - Průměrné známky studentů
Zpracujte CSV soubor `SWI-U2A-znamky.csv`, obsahující seznam studentů, předmětů a jejich známek (sloupce: student, predmet, znamka). Vaším úkolem je načíst tento soubor a spočítat **průměrnou známku** pro každý předmět. Výsledky zobrazte přehledně v textovém výstupu.

`funkce prumer_znamek(df: pd.DataFrame) -> pd.Series, která vrátí průměrné známky pro jednotlivé předměty ve formě Pandas Series.`


### U2B - Tržby všech zákazníků za rok 2024
Pracujte s CSV souborem `SWI-U2B-objednavky.csv`, obsahujícím data o objednávkách (sloupce: id, datum, zakaznik, produkt, mnozstvi, cena). Vaším úkolem je:

- Načíst data a vyfiltrovat pouze objednávky z roku **2024**.
- Spočítat **celkové tržby** za každého zákazníka (tržba = množství × cena).

Výsledky zobrazte přehledně v textovém výstupu.

`funkce trzby_za_zakazniky(df: pd.DataFrame) -> pd.Series, která vrátí agregované tržby pro každého zákazníka.`

---

## 3. Algoritmické úlohy

### U31 - FizzBuzz
Vytvořte funkci, která vrátí seznam čísel od **1 do 100**, kde:
- čísla dělitelná **3** budou nahrazena řetězcem **"Fizz"**,
- čísla dělitelná **5** řetězcem **"Buzz"**,
- čísla dělitelná ***3** i **5** současně řetězcem **"FizzBuzz"**.
- Ostatní čísla budou ve výstupním seznamu jako řetězce.

`funkce fizzbuzz(start: int, end: int) -> list[str], kde start=1 a end=100.`

### U3B - Palindrom
Vytvořte funkci, která určí, zda je zadaný text **palindromem**. Funkce musí **ignorovat velikost písmen a mezery**. Pokud je řetězec shodný při čtení zepředu i zezadu, je považován za palindrom.

`funkce is_palindrom(s: str) -> bool, která vrátí True nebo False podle výsledku.`