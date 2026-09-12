import secrets
import string
import time
import os
import sys
import threading


def generate_password(length: int = 16) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    alphabet = uppercase + lowercase + digits + symbols

    password += [secrets.choice(alphabet) for _ in range(length - len(password))]

    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    return "".join(password)


def random_delay(min_seconds: int = 5, max_seconds: int = 15) -> int:
    return min_seconds + secrets.randbelow(max_seconds - min_seconds + 1)


def clear_console() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def wait_for_enter(stop_event: threading.Event) -> None:
    try:
        input()
        stop_event.set()
    except (EOFError, KeyboardInterrupt):
        stop_event.set()


def main():
    length = 16
    min_delay = 5
    max_delay = 15

    counter = 1
    stop_event = threading.Event()

    listener = threading.Thread(target=wait_for_enter, args=(stop_event,), daemon=True)
    listener.start()

    last_password = ""
    last_counter = 0

    try:
        while not stop_event.is_set():
            clear_console()

            password = generate_password(length)
            last_password = password
            last_counter = counter

            print("Auto-rotating secure password generator")
            print(f"   (new password every {min_delay}-{max_delay} seconds)")
            print("   Press Enter to stop.\n")
            print(f"[{counter:03d}] {password}\n")

            delay = random_delay(min_delay, max_delay)
            print(f"      ↳ next password in {delay} seconds...")

            if stop_event.wait(timeout=delay):
                break

            counter += 1

    except KeyboardInterrupt:
        stop_event.set()

    clear_console()
    print(" Stopped. Last generated password:\n")
    if last_password:
        print(f"[{last_counter:03d}] {last_password}\n")
    else:
        print("(no password was generated)\n")


if __name__ == "__main__":
    main()