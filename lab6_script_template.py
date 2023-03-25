import requests
import hashlib
import subprocess
import os

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
   file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/SHA256SUMS'
   resp_msg = requests.get(file_url)
   expected_hash = ''
   for line in resp_msg.text.splitlines():
        if 'vlc-3.0.17.4-win64.exe' in line:
            expected_hash = line.split()[0]
        return expected_hash


def download_installer():
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    return resp_msg.content

def installer_ok(installer_data, expected_sha256):
    calculated_hash = hashlib.sha256(installer_data).hexdigest()
    return calculated_hash == expected_sha256

def save_installer(installer_data):
    temp_folder = os.getenv('TEMP')
    installer_path = os.path.join(temp_folder, 'vlc-3.0.17.4-win64.exe')
    with open(installer_path, 'wb') as file:
        file.write(installer_data)
    return installer_path

def run_installer(installer_path):
  subprocess.run([installer_path, '/L=1033', '/S'])
  return 
    
def delete_installer(installer_path):
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()