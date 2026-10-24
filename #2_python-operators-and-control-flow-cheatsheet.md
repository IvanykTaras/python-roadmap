# Python — operatory, wypisywanie zmiennych, warunki i pętle

Druga ściąga według [Python for Data Analysis — roadmap.sh](https://roadmap.sh/python-data-analysis), w zakresie z załączonego zdjęcia.

Kolejność: **Operators (Arithmetic, Comparison, Logical) → Printing Variables → Conditionals → Loops**.

Przykłady dotyczą zwykłego Pythona: liczb, tekstów, list i słowników. Porównania do JS/TS i C# pomagają przełożyć znaną składnię.

## 1. Operators — operatory

### Arithmetic — arytmetyczne

| Operator | Znaczenie | Przykład → wynik |
|---|---|---|
| `+` | Dodawanie | `7 + 2` → `9` |
| `-` | Odejmowanie | `7 - 2` → `5` |
| `*` | Mnożenie | `7 * 2` → `14` |
| `/` | Dzielenie | `7 / 2` → `3.5` |
| `//` | Dzielenie z zaokrągleniem w dół | `7 // 2` → `3` |
| `%` | Modulo | `7 % 2` → `1` |
| `**` | Potęgowanie | `2 ** 3` → `8` |

```python
price = 20
quantity = 3
total = price * quantity   # 60

count = 0
count += 1                 # 1
total -= 10                # 50
```

**Różnice i pułapki:**

- Nie ma operatorów `++` i `--`. Używaj `+= 1` i `-= 1`.
- `6 / 2` daje `3.0` (`float`), także gdy oba argumenty są `int`.
- `//` zaokrągla w stronę minus nieskończoności: `-7 // 2` daje `-4`. Dzielenie liczb całkowitych w C# obcina w stronę zera.
- Dla ujemnych liczb modulo może różnić się od JS/C#: `-7 % 2` daje `1`.
- Potęgowanie to `**`, a `^` to bitowy XOR.
- Dzielenie przez zero dla tych liczb zgłasza `ZeroDivisionError`, także dla `float`.

### Comparison — porównania

| Operator | Znaczenie | Przykład → wynik |
|---|---|---|
| `==` | Równa wartość | `3 == 3` → `True` |
| `!=` | Różna wartość | `3 != 4` → `True` |
| `<`, `<=` | Mniejsze, mniejsze lub równe | `3 <= 3` → `True` |
| `>`, `>=` | Większe, większe lub równe | `5 > 3` → `True` |

```python
age = 25
is_adult = age >= 18       # True
is_in_range = 18 <= age < 65  # True — porównanie łańcuchowe

3 == "3"                  # False — brak konwersji jak przy JS ==
3 == 3.0                  # True — różne typy liczb, równa wartość
[1, 2] == [1, 2]          # True — listy porównywane po zawartości
```

Python nie ma `===`. `==` nie wymaga identycznego typu, więc nie traktuj go jako dokładnego odpowiednika JS `===`.

**Przydatne operatory obecności i tożsamości:**

```python
"python" in ["python", "sql"]  # True
"email" not in {"name": "Anna"}  # True — dict sprawdza klucze

result = None
result is None                # True
result is not None            # False
```

`==` porównuje wartości, a `is` sprawdza, czy to ten sam obiekt. Do sprawdzania `None` używaj `is None`; do porównywania liczb i tekstów — `==`.

### Logical — logiczne

| Python | JS/TS i C# | Znaczenie |
|---|---|---|
| `and` | `&&` | Oba warunki spełnione |
| `or` | `\|\|` | Przynajmniej jeden warunek spełniony |
| `not` | `!` | Negacja |

```python
age = 25
is_active = True
is_admin = False

can_order = age >= 18 and is_active  # True
can_enter = is_admin or is_active   # True
is_blocked = not is_active          # False
```

`and` i `or` działają ze skróconym obliczaniem: prawa strona jest obliczana tylko wtedy, gdy jest potrzebna.

```python
user = None
has_access = user is not None and user["active"]
# False — Python nie próbuje odczytać user["active"].
```

Podobnie jak w JS, `and` i `or` mogą zwracać operand zamiast `bool`:

```python
name = ""
display_name = name or "Gość"  # "Gość"
0 or 100                      # 100 — zero jest falsy
```

`or` nie jest odpowiednikiem `??`: zastępuje też `0`, `False`, pusty tekst i puste kolekcje. Gdy domyślna wartość ma zastępować tylko `None`:

```python
value = 0
result = 100 if value is None else value  # 0
```

**Kolejność:** arytmetyka → porównania → `not` → `and` → `or`. Używaj nawiasów, gdy ułatwiają czytanie:

```python
is_admin = False
is_owner = True
is_active = False
can_edit = (is_admin or is_owner) and is_active  # False
```

Nie zastępuj `and` i `or` operatorami `&` i `|` — dla zwykłych liczb są bitowe, a dla zbiorów oznaczają operacje na zbiorach.

## 2. Printing Variables — wypisywanie zmiennych

`print()` jest podstawowym odpowiednikiem `console.log()` i `Console.WriteLine()`.

```python
name = "Anna"
total = 123.456

print(name)                       # Anna
print("Klient:", name)            # Klient: Anna
print(f"{name}: {total:.2f} PLN")  # Anna: 123.46 PLN
print(f"{total=}")                # total=123.456 — wygodne do debugowania
```

**F-string:** prefiks `f`, a zmienne i wyrażenia w `{}`. Podobny do template literals w JS i `$"..."` w C#.

```python
print(f"Podatek: {total * 0.23:.2f}")

print("A", "B", "C", sep=" | ")  # A | B | C
print("Ładowanie", end="...")     # bez końcowego znaku nowej linii
print("gotowe")                   # razem: Ładowanie...gotowe
```

Domyślnie `sep=" "`, a `end="\n"`. Format `:.2f` zmienia sposób wyświetlenia, a nie wartość zmiennej.

## 3. Conditionals — instrukcje warunkowe

```python
total = 120

if total >= 200:
    print("Rabat 20%")
elif total >= 100:
    print("Rabat 10%")
else:
    print("Bez rabatu")
# Rabat 10%
```

- `elif` zamiast `else if`.
- Dwukropek `:` rozpoczyna blok, wcięcia określają jego zawartość.
- Nawiasy wokół warunku nie są wymagane; nie używasz `{}` do bloków.
- W jednym łańcuchu `if/elif/else` wykona się pierwsza pasująca gałąź.
- Kilka osobnych `if` oznacza kilka niezależnych sprawdzeń.

### Truthiness — co jest traktowane jako fałsz

`None`, `False`, zera oraz puste teksty i kolekcje są falsy.

```python
orders = []

if not orders:
    print("Brak zamówień")

# Uwaga: "False" i "0" są niepustymi stringami, więc są truthy.
```

W JS puste tablice i obiekty są truthy. W C# warunek `if` wymaga wartości `bool`; Python dopuszcza sprawdzanie prawdziwości innych obiektów.

### Wyrażenie warunkowe — odpowiednik ternary

```python
age = 20
status = "adult" if age >= 18 else "minor"
# JS/TS/C#: age >= 18 ? "adult" : "minor"
```

Schemat: `wartość_jeśli_prawda if warunek else wartość_jeśli_fałsz`.

## 4. Loops — pętle

### for — przechodzenie po elementach

Pythonowy `for` przypomina JS `for...of` i C# `foreach`.

```python
prices = [10, 20, 30]

for price in prices:
    print(price)
```

Do powtarzania określoną liczbę razy używaj `range(start, stop, step)`. Koniec jest wyłączony.

```python
for i in range(3):
    print(i)              # 0, 1, 2 — każdy w osobnej linii

for i in range(2, 7, 2):
    print(i)              # 2, 4, 6

for i in range(3, 0, -1):
    print(i)              # 3, 2, 1
```

`range()` nie tworzy od razu listy wszystkich liczb. Aby ją uzyskać, użyj np. `list(range(3))`.

### Indeks + element: enumerate()

```python
names = ["Anna", "Jan"]

for index, name in enumerate(names):
    print(index, name)     # 0 Anna; 1 Jan

for number, name in enumerate(names, start=1):
    print(f"{number}. {name}")  # 1. Anna; 2. Jan
```

Preferuj `enumerate()` zamiast ręcznego indeksowania przez `range(len(names))`, gdy potrzebujesz indeksu i wartości.

### Słowniki i dwie kolekcje

```python
user = {"name": "Anna", "age": 25}

for key in user:
    print(key)            # domyślnie iterujesz po kluczach

for key, value in user.items():
    print(key, value)

names = ["Anna", "Jan"]
scores = [90, 75]

for name, score in zip(names, scores):
    print(name, score)
```

Domyślnie `zip()` kończy na krótszej kolekcji. Gdy długości muszą być równe, użyj `zip(names, scores, strict=True)` — dostępne od Pythona 3.10.

### while — powtarzanie, dopóki warunek jest prawdziwy

```python
remaining = 3

while remaining > 0:
    print(remaining)       # 3, 2, 1
    remaining -= 1
```

Zadbaj o zmianę warunku albo `break`, żeby uniknąć nieskończonej pętli. Python nie ma osobnej instrukcji `do...while`.

### break i continue

```python
values = [10, None, 20, -1, 30]

for value in values:
    if value is None:
        continue          # pomiń bieżący element
    if value < 0:
        break             # zakończ całą najbliższą pętlę
    print(value)
# Wypisze 10 i 20.
```

### Pułapka: zmienianie kolekcji w trakcie iterowania

Nie usuwaj elementów z tej samej listy, po której aktualnie iterujesz — możesz pominąć elementy. Utwórz przefiltrowaną listę:

```python
values = [10, None, 20, None]
clean_values = [value for value in values if value is not None]
# [10, 20]
```

## Minićwiczenia — napisz samodzielnie

1. **Arytmetyka:** masz `17` rekordów i strony po `5` rekordów. Oblicz liczbę pełnych stron i liczbę rekordów na ostatniej niepełnej stronie, używając `//` i `%`.
2. **Porównania:** dla `temperature = 21` sprawdź jednym porównaniem łańcuchowym, czy temperatura mieści się w przedziale od `18` włącznie do `25` wyłącznie.
3. **Logika:** użytkownik może edytować zamówienie, gdy jest aktywny i jest administratorem lub właścicielem zamówienia. Użyj trzech zmiennych `bool` i zapisz warunek. Sprawdź też nieaktywnego administratora.
4. **Print:** dla `name = "Anna"`, `total = 123.456` wypisz dokładnie `Klient Anna | Kwota: 123.46 PLN`, używając f-stringa.
5. **Warunki:** ustal etykietę zamówienia: poniżej `100` → `small`, od `100` do poniżej `500` → `medium`, od `500` → `large`. Sprawdź granice `99`, `100`, `499`, `500`.
6. **For:** przejdź po `[12, None, 0, 18, None]` i policz sumę oraz liczbę pomiarów innych niż `None`. Zero jest poprawnym pomiarem. Użyj pętli i `continue`.
7. **While:** zacznij od `balance = 100` i odejmuj `30`, dopóki saldo pozwala na kolejne odjęcie. Po zakończeniu wypisz pozostałe saldo.
8. **Enumerate:** wypisz `["Anna", "Jan", "Ola"]` jako numerowaną listę od `1`.
9. **Łączenie tematów:** dla danych poniżej wypisz identyfikatory opłaconych zamówień o wartości przynajmniej `100`, a potem ich łączną wartość. Użyj `for`, `if` i `print`.

```python
orders = [
    {"id": 1, "total": 120, "paid": True},
    {"id": 2, "total": 80, "paid": True},
    {"id": 3, "total": 200, "paid": False},
    {"id": 4, "total": 150, "paid": True},
]
```

Rozwiązania dopisz samodzielnie. Przy sprawdzaniu zwracaj uwagę na granice przedziałów, zero, `None` i puste kolekcje.
