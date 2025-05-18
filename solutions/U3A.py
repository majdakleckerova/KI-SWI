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