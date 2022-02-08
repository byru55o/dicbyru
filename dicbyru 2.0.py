from colorama import Fore, Back, init
from pyfiglet import Figlet

init(autoreset=True)


def banner():
    custom_fig = Figlet(font='lean')
    print(Fore.RED + custom_fig.renderText("DicByRu"))


def main():
    num = 0
    output = input(Fore.CYAN + "DICTIONARY OUTPUT: ")
    keywords = input(Fore.CYAN + "ENTER KEYWORDS SEPARATED WITH \",\": ")
    capitalize = input(Fore.CYAN + "AUTO CAPS MODE [1] // [0]: ")
    maxnumber = input(Fore.CYAN + "MAX NUMBER {f.e.: 3 --> hola; hola0 ; hola1; hola2; hola3}: ")
    specialchar = input(Fore.CYAN + "SPECIAL CHARS AT THE END OF THE PASSWORDS [1] // [0]: ")
    keylist = keywords.split(",")
    for key in keylist:
        with open(output, "a") as dictionary:
            dictionary.write(key)
            dictionary.write("\n")
    while num <= int(maxnumber):
        for key in keylist:
            key = key + str(num)
            with open(output, "a") as dictionary:
                dictionary.write(key)
                dictionary.write("\n")
                if capitalize == "1":
                    dictionary.write(key.capitalize())
                    dictionary.write("\n")
                    dictionary.write(key.upper())
                    dictionary.write("\n")
                if specialchar == "1":
                    dictionary.write(key + ".")
                    dictionary.write("\n")
                    dictionary.write(key + ",")
                    dictionary.write("\n")
                    dictionary.write(key + "!")
                    dictionary.write("\n")
                    dictionary.write(key + "?")
                    dictionary.write("\n")
                    dictionary.write(key + "#")
                    dictionary.write("\n")
                    dictionary.write(key + "$")
                    dictionary.write("\n")
                    dictionary.write(key + "@")
                    dictionary.write("\n")
                    dictionary.write(key + "+")
                    dictionary.write("\n")
                    dictionary.write(key + "*")
                    dictionary.write("\n")
                    dictionary.write(key + "=")
                    dictionary.write("\n")
                    dictionary.write(key + "%")
                    dictionary.write("\n")
        num = num + 1
    print(Back.RED + "DICTIONARY CREATED SUCCESSFULLY:")
    print(Fore.LIGHTGREEN_EX + "saved in " + output)

banner()

main()