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
