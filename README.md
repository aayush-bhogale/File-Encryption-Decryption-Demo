# File Encryption & Decryption Demo (Python)

A simple Python project demonstrating file encryption and decryption using the `cryptography` library's Fernet symmetric encryption.

> **Disclaimer**
>
> This project is for educational purposes only. It demonstrates how symmetric encryption works in Python. Do not use it on important files or systems you do not own.

## Features

* Encrypts files in the current directory using Fernet encryption.
* Generates and stores an encryption key.
* Decrypts files using the stored key.
* Password-protected decryption process.
* Fun terminal output using the `cowsay` library.

## Requirements

* cryptography
* cowsay

Install dependencies:

```bash
pip install cryptography cowsay
```


### Encryption

Running `ransome.py`:

1. Scans files in the current directory.
2. Generates a Fernet encryption key.
3. Saves the key to `thekey.key`.
4. Encrypts all eligible files.
5. Displays a cowsay message.

Run:

```bash
python ransome.py
```

### Decryption

Running `decrypt.py`:

1. Loads the encryption key from `thekey.key`.
2. Prompts the user for the secret phrase.
3. Gives up to 3 attempts.
4. Decrypts all encrypted files if the correct phrase is entered.

Run:

```bash
python decrypt.py
```

Secret phrase:

```text
KhulJaaSimSim
```


## Notes

* Do not delete `thekey.key` after encryption.
* Losing the key means encrypted files cannot be recovered.
* This project is intended only for learning about file encryption and Python file handling.

## Technologies Used

* Python
* Cryptography (Fernet)
* Cowsay

## License

This project is provided for educational and learning purposes.
