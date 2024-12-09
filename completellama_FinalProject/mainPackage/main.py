import dataPackage
from locationPackage.decryptedLocation import findLocation
from moviePackage.decryptedMovie import decrypt_movie_title
import json
from PIL import Image

def main():
    # Paths to files
    json_file = 'dataPackage/EncryptedGroupHints Fall 2024 Section 001.json'
    english_file = 'dataPackage/UCEnglish.txt'
    team_file = 'dataPackage/TeamsAndEncryptedMessagesForDistribution.json'  # JSON with encrypted messages
    project_team_name = "CompleteLlama"

    # Load encrypted message dynamically from the JSON file
    with open(team_file, 'r') as f:
        team_data = json.load(f)

    # Retrieve the encrypted message for the team
    encrypted_message_list = team_data.get(project_team_name)

    if isinstance(encrypted_message_list, list) and len(encrypted_message_list) > 0:
        encrypted_message = encrypted_message_list[0]  # Get the first (and only) message
        movie_key = "oSQSToOvQLs-_7SRDonuB1xB7K10RwCF7MdIQa1MCdc="  # You may still need to handle this dynamically
    else:
        print(f"Error: Team '{project_team_name}' not found or data is not in the correct format.")
        return

    # Decrypt the location
    location_finder = findLocation(json_file, english_file)
    location = location_finder.decrypt_location(project_team_name)
    print(f"Decrypted UC Location: {location}")

    # Decrypt the movie title
    movie_title = decrypt_movie_title(encrypted_message, movie_key)
    print(f"Decrypted Movie Title: {movie_title}")

     #Open our selfie 
    image_path = ('dataPackage/us.jfif')
    image = Image.open(image_path)

    #Display our awesome selfie 
    image.show()

if __name__ == "__main__":
    main()
