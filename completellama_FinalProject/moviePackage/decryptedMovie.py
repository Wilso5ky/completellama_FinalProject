# Name: Alexis Tipkemper-Sparks / Kayla Wilson / Jared Rababy 
# email:  tipkemam@mail.uc.edu / wilso5ky@mail.uc.edu /rababyjd@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/2024
# Course #/Section:  IS 4010
# Semester/Year: Fall 2024
# Brief Description of the assignment:  Decrypting codes from JSON files + scavenging 

# Brief Description of what this module does: Practice reading JSON files, Python, and outputting photos
# Citations: GeeksforGeeks / W3Schools / InClass from last week
# Anything else that's relevant: N/A Github makes us sad

#decryptedMovie

from cryptography.fernet import Fernet

def decrypt_movie_title(encrypted_message, key):
    """Decrypt movie title using the provided encryption key."""
    try:
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        return decrypted_message
    except Exception as e:
        return f"Failed to decrypt movie title: {str(e)}"
