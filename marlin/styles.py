from colorama import init
from colorama import Fore, Style

init(autoreset=True)


def label(label):
    labels = {
        "info": Fore.YELLOW + Style.BRIGHT + "[!]" + Style.RESET_ALL,
        "bad": Fore.RED + Style.BRIGHT + "[-]" + Style.RESET_ALL,
        "good": Fore.GREEN + Style.BRIGHT + "[+]" + Style.RESET_ALL,
        "run": Fore.WHITE + Style.BRIGHT + "[~]" + Style.RESET_ALL,
        "list": Fore.YELLOW + Style.BRIGHT + ">" + Style.RESET_ALL,
    }
    return labels[label]


def color(color, text):
    colors = {
        "yellow": Fore.YELLOW + Style.BRIGHT + text + Style.RESET_ALL,
        "red": Fore.RED + Style.BRIGHT + text + Style.RESET_ALL,
    }
    return colors[color]
