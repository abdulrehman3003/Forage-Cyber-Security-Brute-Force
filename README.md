# AIG Cybersecurity Program - Bruteforce Decryption Task

## Overview
This project is part of the AIG Cybersecurity Program by Forage. It simulates a real-world cybersecurity scenario involving encrypted files and password recovery using brute force techniques.

In this task, the goal is to decrypt a password-protected ZIP file (`enc.zip`) without prior knowledge of the password. This mimics a scenario where ransomware may have encrypted sensitive data, and the decryption key must be recovered.

## How the Program Works
The provided Python script (`bruteforce.py`) performs the following tasks:

1. **Reading Passwords:** The script reads a list of potential passwords from a subset of the widely known `rockyou.txt` wordlist.
2. **Brute Force Extraction:** It attempts to extract the contents of `enc.zip` using each password from the list.
3. **Successful Decryption:** If the correct password is found, the program prints it and extracts the file contents.
4. **Error Handling:** The script gracefully handles incorrect password attempts and invalid or corrupted ZIP files.

## Usage Instructions
### Prerequisites
- Python 3+
- The following files in the same directory as the script:
  - `enc.zip`: Encrypted file
  - `rockyou.txt`: Password list file

### Running the Script
To run the program:

```bash
python3 bruteforce.py
```

### Expected Output
- If the correct password is found, the program will display:
  ```
  [+] Password found: <password>
  ```
- If no password in the list matches, it will print:
  ```
  [-] Password not found in the list.
  ```
- In case of missing files or invalid ZIP format, appropriate error messages will be displayed.

## Learning Objectives
Through this simulation, participants gain insights into:

- **Cybersecurity Practices:** Understanding the risks of weak passwords and encryption vulnerabilities.
- **Brute Force Techniques:** Hands-on experience in password recovery using brute force.
- **Error Handling:** Writing robust code that handles exceptions and provides meaningful feedback.

## Disclaimer
This project is for educational purposes only. Unauthorized access to protected data or systems is illegal and unethical.

## About Forage
Forage offers job simulations in collaboration with leading companies like AIG to help learners develop practical skills for their careers.

## About AIG
American International Group (AIG) is a leading global insurance organization, providing a wide range of property-casualty insurance, life insurance, retirement solutions, and other financial services.

