import requests

# Send GET message to download the file
file_url = 'https://raw.githubusercontent.com/JeremyDalby/SampleFiles/main/dog.jpg'
resp_msg = requests.get(file_url)

# Check whether the download was successful
if resp_msg.status_code == requests.codes.ok:

    # Extract binary file content from response message
    file_content = resp_msg.content

    # Save the binary file to disk
    with open(r'C:\temp\dog.jpg', 'wb') as file:
         file.write(file_content)
