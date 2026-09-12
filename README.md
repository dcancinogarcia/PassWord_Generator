Password Generator
A secure, auto-rotating password generator written in Python. It continuously generates strong random passwords at random intervals (5–15 seconds), making it useful for demonstrations, testing, or generating multiple secure passwords on the fly.

 Features
Cryptographically secure — uses Python's secrets module instead of random
Auto-rotating — generates a new password every 5–15 seconds (randomized interval)
Guaranteed complexity — every password contains at least one uppercase letter, lowercase letter, digit, and symbol
Shuffled output — character positions are randomized using a Fisher–Yates shuffle with secrets.randbelow
Cross-platform — clears the console on both Windows (cls) and Unix-like systems (clear)
Press Enter to stop — gracefully stops and shows the last generated password
Non-blocking input — a background thread listens for Enter while passwords rotate

Requirements
Python 3.6+ (uses secrets module, available since Python 3.6)

No third-party dependencies — standard library only

Usage
Clone the repository and run the script:

bash
git clone https://github.com/dcancinogarcia/password-generator.git
cd password-generator
python Password_Generator.py
Once running, the terminal will display a new password every 5–15 seconds:

text
Auto-rotating secure password generator
   (new password every 5-15 seconds)
   Press Enter to stop.

[001] A8k#mP2vQ!zL9xR4

      ↳ next password in 12 seconds...
Press Enter (or Ctrl+C) to stop. The last generated password will remain on screen.

Configuration
You can tweak the behavior by editing the variables inside main():

Variable	Default	Description
length	16	Length of each generated password
min_delay	5	Minimum seconds between passwords
max_delay	15	Maximum seconds between passwords
You can also import the function directly in your own code:

python
from Password_Generator import generate_password

pwd = generate_password(length=24)
print(pwd)

Security Notes
Uses secrets.choice and secrets.randbelow — suitable for cryptographic use.

Each password is guaranteed to include at least one character from every category (uppercase, lowercase, digits, symbols).

The character set includes: A-Z, a-z, 0-9, and !@#$%^&*()-_=+[]{};:,.<>?/

This tool is intended for local use. Avoid displaying sensitive passwords on shared or recorded screens.

How It Works
Initialization — one character is picked from each required category.

Filling — the remaining characters are randomly chosen from the full alphabet.

Shuffle — the list is shuffled using a secure Fisher–Yates algorithm.

Loop — the password is displayed, then the script sleeps for a random delay before generating the next one.

Stopping — a daemon thread waits for Enter and signals the main loop via a threading.Event.
