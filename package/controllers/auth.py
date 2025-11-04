import hashlib, secrets
from .dbjson import JSONDB

class Auth:
    def __init__(self, db_path):
        self.db = JSONDB(db_path)

    def _hash_password(self, password, salt):
        return hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

    def register(self, nome, email, password):
        users = self.db.get_list('users')
        email = email.strip().lower()
        if not email or not password:
            raise ValueError("email e password obrigatórios")
        if any(u['email'] == email for u in users):
            raise ValueError("email já cadastrado")
        salt = secrets.token_hex(16)
        pw_hash = self._hash_password(password, salt)
        user = {'nome': nome, 'email': email, 'salt': salt, 'pw_hash': pw_hash}
        self.db.append_to_list('users', user)
        return True

    def authenticate(self, email, password):
        users = self.db.get_list('users')
        email = email.strip().lower()
        for u in users:
            if u['email'] == email:
                return u['pw_hash'] == self._hash_password(password, u['salt'])
        return False
