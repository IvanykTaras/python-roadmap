# Python — typy danych i struktury danych

Ściąga według [Python for Data Analysis — roadmap.sh](https://roadmap.sh/python-data-analysis), z porównaniami do JS/TS i C#.

Kolejność: **Data Types → Data Structures → Type Casting → Working with Strings → List Comprehensions**.

Python nie wymaga deklaracji typu, średników ani `let`/`const`. Bloki kodu wyznaczają **wcięcia**, zwykle 4 spacje.

```python
price = 99.90
name = "Anna"

if price > 50:
    print(name)
```

## 1. Data Types — typy danych

| Z roadmapy | Python | Przykład | Do czego |
|---|---|---|---|
| Integers | `int` | `quantity = 3` | Liczby całkowite |
| Floats | `float` | `temperature = 21.5` | Liczby zmiennoprzecinkowe |
| Strings | `str` | `name = "Anna"` | Tekst |
| Booleans | `bool` | `is_active = True` | Prawda / fałsz |
| Null | `None` | `result = None` | Brak wartości |

```python
type(42)        # <class 'int'>
type("42")      # <class 'str'>
```

**Liczby — ważna składnia:**

```python
7 / 2     # 3.5 — dzielenie zawsze zwraca float
7 // 2    # 3   — dzielenie z zaokrągleniem w dół
7 % 2     # 1   — reszta
2 ** 3    # 8   — potęgowanie; ^ oznacza XOR
```

**Różnice względem JS/TS/C#:**

- Python rozróżnia `int` i `float`; JS używa zwykle `number`.
- `int` nie ma stałego limitu jak `int` w C# — ogranicza go dostępna pamięć.
- Pisz `True`, `False`, `None`, z wielkiej litery.
- Nie ma osobnego odpowiednika JS `undefined`.
- `float` ma błędy reprezentacji jak JS `number` i C# `double`: `0.1 + 0.2 != 0.3`.

```python
result = None

if result is None:       # standardowe sprawdzanie braku wartości
    print("Brak wyniku")

# == porównuje wartości, is sprawdza tożsamość obiektów.
# Dla liczb i tekstów używaj ==.
```

## 2. Data Structures — struktury danych

### Szybki wybór

| Struktura | Składnia | Kiedy używać | Najbliższe skojarzenie |
|---|---|---|---|
| `list` | `[a, b]` | Kolekcja, którą zmieniasz | JS `Array`, C# `List<T>` |
| `tuple` | `(a, b)` | Stały zestaw pozycji | Tuple w C# |
| `dict` | `{"key": value}` | Dane pod kluczami | JS `Map` / obiekt, C# `Dictionary` |
| `set` | `{a, b}` | Unikalne elementy | JS `Set`, C# `HashSet<T>` |

### Lists → list

**Uporządkowana, zmienialna kolekcja.** Dopuszcza duplikaty.

```python
prices = [10, 20, 20]

prices[0]          # 10 — indeksowanie od zera
prices[-1]         # 20 — ostatni element
prices[0:2]        # [10, 20] — koniec zakresu wyłączony

prices.append(30)   # dodaj jeden element — jak push()
prices.extend([40, 50])  # dodaj wiele elementów
prices.remove(20)  # usuń pierwsze wystąpienie wartości 20
last = prices.pop()     # usuń i zwróć ostatni element

len(prices)        # liczba elementów — zamiast .length / .Count
30 in prices       # sprawdzenie obecności — zamiast .includes()
```

**Pułapka: przypisanie nie kopiuje kolekcji**, podobnie jak w JS/C#.

```python
original = [1, 2]
alias = original
alias.append(3)       # original też ma teraz [1, 2, 3]

copy = original.copy()  # płytka kopia
# Zagnieżdżone listy lub słowniki nadal są współdzielone.
```

### Tuples → tuple

**Uporządkowana kolekcja, której pozycji nie zmieniasz.**

```python
point = (10, 20)
x, y = point         # rozpakowanie — podobne do destructuring

point[0]             # 10
# point[0] = 99      # TypeError

single = (10,)       # przecinek tworzy tuple jednoelementową
```

Dobre dla współrzędnych albo wyniku zawierającego kilka wartości. Tuple może zawierać zmienialny obiekt, np. listę — ta lista nadal może się zmieniać.

### Dictionaries → dict

**Zmienialne mapowanie klucz → wartość.** Zachowuje kolejność dodawania kluczy.

```python
user = {
    "name": "Anna",
    "age": 25,
    "city": None,
}

user["name"]            # "Anna"
user["age"] = 26         # aktualizacja
user["active"] = True   # nowy klucz

user.get("email")       # None, jeśli klucza nie ma
user.get("role", "user")  # wartość domyślna
# user["email"]         # KeyError, jeśli klucza nie ma

"name" in user          # sprawdza KLUCZE
del user["city"]

for key, value in user.items():
    print(key, value)
```

**Różnice:** używasz `user["name"]`, a nie `user.name`. Klucze muszą być hashowalne — typowo `str` lub `int`; lista nie może być kluczem.

### Sets → set

**Zmienialny zbiór unikalnych elementów.** Nie zapewnia kolejności ani indeksowania.

```python
tags = {"python", "api", "python"}
# Zawiera dwa elementy: "python" i "api".

tags.add("data")
tags.discard("api")    # brak błędu, jeśli elementu nie ma

a = {1, 2, 3}
b = {3, 4}

a | b                 # suma: {1, 2, 3, 4}
a & b                 # część wspólna: {3}
a - b                 # różnica: {1, 2}

unique_ids = set([1, 1, 2])  # {1, 2}
```

**Pułapka:** `{}` tworzy pusty `dict`. Pusty zbiór to `set()`.

## 3. Type Casting — konwersje typów

```python
int("42")          # 42
float("19.99")     # 19.99
str(42)            # "42"
int(3.9)           # 3 — obcina część ułamkową
list("abc")        # ["a", "b", "c"]
tuple([1, 2])      # (1, 2)
set([1, 1, 2])     # {1, 2}
```

**Pułapki przy przejściu z JS:**

```python
# "Cena: " + 10     # TypeError — brak automatycznej konwersji
f"Cena: {10}"      # "Cena: 10"

# int("3.5")       # ValueError
# float("3,5")     # ValueError — separatorem jest kropka

bool("")           # False
bool("False")      # True — to niepusty tekst!
bool([])           # False
```

Fałszywe są m.in. `None`, `False`, zero i puste kolekcje. **Puste listy i słowniki są falsy**, inaczej niż w JS.

## 4. Working with Strings — praca z tekstem

String jest **niemutowalny** — operacje tworzą nowy tekst.

```python
text = "  Python Data  "

text.strip()                 # "Python Data" — jak trim()
text.lower()                 # "  python data  "
text.replace("Data", "API")   # "  Python API  "

"Anna,Jan,Ola".split(",")     # ["Anna", "Jan", "Ola"]
", ".join(["Anna", "Jan"])    # "Anna, Jan"

"Python" in text             # True
text.strip().startswith("Py")  # True

name = "Anna"
score = 92.456
message = f"{name}: {score:.2f}%"  # "Anna: 92.46%"
```

**Slicing** działa dla tekstów, list i tuples:

```python
word = "Python"

word[:3]     # "Pyt"
word[3:]     # "hon"
word[-2:]    # "on"
word[::2]    # "Pto" — co drugi znak
word[::-1]   # "nohtyP" — odwrócenie
```

Wzór: `kolekcja[start:stop:step]`. Pozycja `stop` jest wyłączona.

## 5. List Comprehensions — tworzenie list

Zwięzły sposób na **przekształcanie i filtrowanie**.

```python
prices = [10, 20, 30]

# JS: prices.map(p => p * 2)
# C#: prices.Select(p => p * 2).ToList()
doubled = [price * 2 for price in prices]

# JS: prices.filter(p => p >= 20)
# C#: prices.Where(p => p >= 20).ToList()
expensive = [price for price in prices if price >= 20]
```

Schemat:

```python
wynik = [wyrażenie for element in kolekcja if warunek]
```

Przykład łączący struktury:

```python
users = [
    {"name": "Anna", "active": True},
    {"name": "Jan", "active": False},
    {"name": "Ola", "active": True},
]

active_names = [user["name"] for user in users if user["active"]]
# ["Anna", "Ola"]
```

Comprehension od razu tworzy listę — w odróżnieniu od odroczonego wykonania wielu operacji LINQ.

## Minićwiczenia — napisz samodzielnie

1. **Typy:** utwórz zmienne reprezentujące liczbę zamówień, temperaturę, nazwę klienta, aktywność konta i brak wyniku. Wypisz ich typy.
2. **List:** dla `[12, 8, 15]` dodaj `20`, usuń `8`, odczytaj ostatni element i utwórz niezależną kopię.
3. **Tuple:** zapisz współrzędne `(52.23, 21.01)` i rozpakuj je do dwóch zmiennych.
4. **Dict:** utwórz zamówienie z kluczami `id`, `total`, `paid`. Zmień `paid` i odczytaj brakujący `discount` z domyślną wartością `0`.
5. **Set:** usuń duplikaty z `["api", "python", "api", "data"]`, a potem znajdź wspólne elementy z `{"python", "sql"}`.
6. **Konwersje i tekst:** z `"  anna,19.90  "` uzyskaj imię `"Anna"` oraz cenę jako `float`.
7. **Comprehension:** z poniższych danych utwórz listę identyfikatorów opłaconych zamówień o wartości przynajmniej `100`:

```python
orders = [
    {"id": 1, "total": 120, "paid": True},
    {"id": 2, "total": 80, "paid": True},
    {"id": 3, "total": 200, "paid": False},
    {"id": 4, "total": 150, "paid": True},
]
```
