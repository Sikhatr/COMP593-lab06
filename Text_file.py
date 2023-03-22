import requests
import hashlib

# Send GET message to download the file
file_url = 'https://raw.githubusercontent.com/JeremyDalby/SampleFiles/main/jokes.txt'
resp_msg = requests.get(file_url)

# Check whether the download was successful
if resp_msg.status_code == requests.codes.ok:

    # Extract text file content from response message
    file_content = resp_msg.text

    # Save the text file to disk
    with open(r'C:\temp\jokes.txt', 'w') as file:
     file.write(file_content)

      # Extract binary file content from response message
    file_content = resp_msg.content

    # Save the binary file to disk
    with open(r'C:\temp\dog.jpg', 'wb') as file:
         file.write(file_content)

         # Extract text file content from response message body
    file_content = resp_msg.text

    # Split the text file content into a list of jokes
    jokes = file_content.split('~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
    # Print the 5th joke in the list
    print(jokes[4])

    # Extract binary file content from response message body
    file_content = resp_msg.content

    # Calculate SHA-256 hash value
    image_hash = hashlib.sha256(file_content).hexdigest()

    # Print the hash value
    print(image_hash)

    

