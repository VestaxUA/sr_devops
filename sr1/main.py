from sr1.string_utils import print_string, analyze_string, uppercase_list
from generator import even_odd_generator


def main():
    print("--- Приклад 1 ---")
    print_string("Привіт, світ!")
    print_string(123)

    print("\n--- Приклад 2 ---")
    analyze_string("HELLO")
    analyze_string("hello")
    analyze_string("HeLLo")

    print("\n--- Приклад 3 ---")
    print(uppercase_list("smogtether"))

    print("\n--- Приклад 4 ---")
    gen = even_odd_generator()
    for _ in range(6):
        print(next(gen))


if __name__ == "__main__":
    main()