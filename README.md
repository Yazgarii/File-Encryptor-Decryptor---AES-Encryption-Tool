
# File Encryptor & Decryptor - AES Encryption Tool

This Python-based tool allows you to encrypt and decrypt your files with the **AES (Advanced Encryption Standard)** encryption algorithm. Users can select and securely encrypt their files, making them decryptable only with the correct password.

## Features
- File encryption and decryption
- High security using AES encryption algorithm
- Automatic saving of encrypted files with `.enc` extension
- Simple command line interface for easy operation

## Usage

#### Requirements
- Python 3.x
- PyCryptodome library

### Step 1: Install Requirements
To use this project you need to install the `PyCryptodome` library. You can install it with the following command:

```bash
pip install pycryptodome
```

### Step 2: File Encryption
To encrypt your file, you will need to enter the name of the file you want to encrypt and a password. You can encrypt your file by following the commands below:

1. Encrypt your file with the `encrypt_file` function.
2. The encrypted file will be saved with `.enc` extension.

```bash
python encrypt_decrypt.py
```

### Step 3: File Decryption
To decrypt the encrypted file, simply enter the correct password. The name of the encrypted file will have the extension `.enc`.

```bash
python encrypt_decrypt.py
```

### Step 4: Outputs
- Encrypted file: `filename.enc`
- Decrypted file: `decrypted_filename`

## Encryption Algorithm You Use

This tool encrypts files using the **AES (Advanced Encryption Standard)** encryption algorithm. AES is a symmetric key encryption algorithm with proven security and speed.

## Contributing

If you would like to contribute to this project, please follow the steps below:
1. Fork this project.
2. Add a new feature or fix a bug.
3. Create pull request.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
