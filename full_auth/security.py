from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Takes a plain-text password and returns a secure hash.
    Used during Registration.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares a plain-text password with a stored hash.
    Used during Login.
    """
    return pwd_context.verify(plain_password, hashed_password)