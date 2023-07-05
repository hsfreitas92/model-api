class User:
    def __init__(self, id, name, email, email_verified_at, password, password_recovery_code,remember_token, created_at, updated_at, status_id, profile_id, document, token_2fa):
        self.id = id
        self.name = name
        self.email = email
        self.email_verified_at = email_verified_at
        self.password = password        
        self.password_recovery_code = password_recovery_code
        self.remember_token = remember_token
        self.created_at = created_at
        self.updated_at = updated_at
        self.status_id = status_id
        self.profile_id = profile_id
        self.document = document
        self.token_2fa = token_2fa        

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'email_verified_at': self.email_verified_at,
            'password': self.password,            
            'password_recovery_code': self.password_recovery_code,
            'remember_token': self.remember_token,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'status_id': self.status_id,
            'profile_id': self.profile_id,
            'document': self.document,
            'token_2fa': self.token_2fa,
        }
