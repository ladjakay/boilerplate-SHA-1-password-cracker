import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Read the top 10,000 passwords
    with open("top-10000-passwords.txt", "r") as f:
        passwords = [line.strip() for line in f]

    # If use_salts is True, read the known salts
    if use_salts:
        with open("known-salts.txt", "r") as f:
            salts = [line.strip() for line in f]

        for salt in salts:
            for password in passwords:
                # Check salt prepended: salt + password
                prepended = salt + password
                if hashlib.sha1(prepended.encode('utf-8')).hexdigest() == hash:
                    return password
                
                # Check salt appended: password + salt
                appended = password + salt
                if hashlib.sha1(appended.encode('utf-8')).hexdigest() == hash:
                    return password
    else:
        # Check standard passwords without salts
        for password in passwords:
            hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
            if hashed == hash:
                return password

    return "PASSWORD NOT IN DATABASE"