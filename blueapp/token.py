from itsdangerous import URLSafeTimedSerializer
from init_app import app

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PWD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    try:
        email = serializer.loads(token,
                                 salt=app.config['SECURITY_PWD_SALT'],
                                 max_age=expiration
        )
    except:
        return False
    return email
