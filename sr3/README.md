# fire_expose

Цей інструмент використовує бібліотеку **Fire** для автоматичного створення CLI з функцій у файлі `utils.py`.

---

## 🆘 Допомога (--help)

Щоб побачити доступні команди:

```bash
python src/fire_expose.py --help
💡 Приклад виводу:
usage: fire_expose.py <command> [<args>...]

Available commands:
  greet     Привітати користувача.
  goodbye   Попрощатись із користувачем.

Use "python src/fire_expose.py <command> --help" for more information on a command.

💡 Приклади використання
python src/fire_expose.py greet Alice
# → Привіт, Alice!

python src/fire_expose.py goodbye Bob
# → До побачення, Bob!