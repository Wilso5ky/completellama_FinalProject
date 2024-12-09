#decryptedLocation.py

import json


class findLocation():
    def __init__(self, json_file, english_file):
        self.json_file = json_file
        self.english_file = english_file

    def searchTeam(self, teamName):
        # Load encryption data from JSON hints
        with open(self.json_file, 'r') as f:
            encrypted_data = json.load(f)
           
        if teamName in encrypted_data:
            return encrypted_data[teamName]
        else:
            print("error finding CompleteLlama as teamName")
     
    def decrypt_location(self, teamName):
       
        # Search for team, CompleteLlama in encryption data
        encrypted_location = self.searchTeam(teamName)
       
        with open(self.english_file, 'r') as f:
            english_lines = f.readlines()
       
        # Decrypt location
        decrypted_location = []
        for index in encrypted_location:
            # To convert index to integer - use to create word
            word = english_lines[int(index)].strip()
            decrypted_location.append(word)
       
        return ' '.join(decrypted_location)\
