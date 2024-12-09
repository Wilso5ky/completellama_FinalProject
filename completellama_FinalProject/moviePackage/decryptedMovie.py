from cryptography.fernet import Fernet

def decrypt_movie_title(encrypted_message, key):
    """Decrypt movie title using the provided encryption key."""
    try:
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        return decrypted_message
    except Exception as e:
        return f"Failed to decrypt movie title: {str(e)}"
