def guess_number():
    min = 1
    max = 100
    attempts = 0
    num_attempts = []

    while True:
        guess = (min + max) // 2
        attempts += 1
        num_attempts.append(guess)

        print(f"Попытка {attempts}: {guess}")
        user_input = input("Ваше число больше, меньше или равно? (больше/меньше/да): ")

        if user_input == "да":
            print(f"Угадал за {attempts} попыток(ки)")
            with open("results.txt", "w") as file:
                file.write(f"Загаданное число: {guess}\n")
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Попытки: {num_attempts}\n")
            break
        elif user_input == "больше":
            min = guess + 1
        elif user_input == "меньше":
            max = guess - 1
        else:
            print("Некорректный ввод. Пожалуйста, введите 'больше', 'меньше' или 'да'.")

if __name__ == "__main__":
    guess_number()