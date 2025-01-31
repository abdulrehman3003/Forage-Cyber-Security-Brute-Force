from zipfile import ZipFile, BadZipFile

# Attempt to extract the zip file using the provided password
def attempt_extract(zf_handle, password):
    try:
        # Password must be in bytes
        zf_handle.extractall(pwd=password.strip())
        print("[+] Password found: {}".format(password.decode()))
        return True
    except RuntimeError:
        # Incorrect password
        return False
    except BadZipFile:
        print("[-] Corrupted or invalid ZIP file.")
        return True


def main():
    print("[+] Beginning bruteforce")
    try:
        # Open the zip file
        with ZipFile('enc.zip') as zf:
            with open('rockyou.txt', 'rb') as password_list:
                for password in password_list:
                    if attempt_extract(zf, password):
                        break
                else:
                    print("[-] Password not found in the list.")
    except FileNotFoundError as e:
        print(f"[!] File not found: {e}")

if __name__ == "__main__":
    main()