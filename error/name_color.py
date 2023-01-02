import pyfiglet
from termcolor import colored
mes = input('type a text: ')
color = input('input a color: ')
ascii_text = pyfiglet.figlet_format(mes)
text = colored(ascii_text, color= color)
print(text)