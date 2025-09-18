def print_string(s: str) -> None:
    if not isinstance(s, str):
        print("Помилка: аргумент має бути рядком!")
        return
    print(s)

def analyze_string(s: str) -> None:
    if not isinstance(s, str):
        print("Помилка: аргумент має бути рядком!")
        return
    if s.isupper():
        print("Усі літери у верхньому регістрі.")
    elif s.islower():
        print("Усі літери у нижньому регістрі.")
    else:
        print("Рядок містить як великі, так і малі літери.")

def uppercase_list(word: str) -> list[str]:
    if not isinstance(word, str):
        print("Помилка: аргумент має бути рядком!")
        return []
    return [ch.upper() for ch in word]
