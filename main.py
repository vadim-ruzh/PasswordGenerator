
import argparse
import secrets
import string

def generate_password(length:int,uppercase:bool,digits:bool,special:bool):
    alphabet = string.ascii_lowercase
    if uppercase:
        alphabet += string.ascii_uppercase
    if digits:
        alphabet += string.digits
    if special:
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for i in range(length))

    return password

parser = argparse.ArgumentParser(
    prog="Password generator",
    description="Консольный генератор паролей."
)

parser.add_argument(
    "-u",
    "--uppercase",
    action="store_true",
    default=False,
    help="Добавляет специальные буквы в верхнем регистре."
)
parser.add_argument(
    "-s",
    "--special",
    action="store_true",
    default=False,
    help="Добавляет специальные символы в пароль."
)
parser.add_argument(
    "-d",
    "--digits",
    action="store_true",
    default=False,
    help="Добавляет цифры в пароль."
)
parser.add_argument(
    "-l",
    "--length",
    type=int,
    default=8,
    help="Длина пароля"
)

args = parser.parse_args()
password = generate_password(args.length,args.uppercase,args.digits,args.special)

print(password)