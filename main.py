english_letters = "abcdefghijklmnopqrstuvwxyz"
ukr_letters = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"


def main():
    text = input("Введіть текст: ").lower()
    runtype = input("Виберіть як запустити програму 1 2: ")

    chars = ""

    if runtype == "1":
        lang = input("Оберіть мову us ua: ")
        chardict = {}

        if lang == "us":
            chars = english_letters
        elif lang == "ua":
            chars = ukr_letters
        else:
            print("Ви ввели неправильну мову")
            main()

        print(f"Кількість символів: len(text)")

        for char in chars.lower():
            chardict[char] = 0

        for char in text:
            if char in chars:
                chardict[char] += 1

        for key, value in chardict.items():
            print(f"Кількість букв '{key}': {value}")

    elif runtype == "2":
        words = text.split(" ")

        dictlist = [word.lower() for word in words if len(word) > 3]
        dictlist = sorted(set(dictlist))

        print(dictlist)

        for num, word in enumerate(dictlist):
            print(f"{num+1}. {word}")

    else:
        main()

main()

