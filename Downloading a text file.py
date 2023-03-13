import requests
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
