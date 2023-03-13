import subprocess
import os


def main():
    expected_sha256 = get_expected_sha256()
    installer_data = download_installer()
    if installer_ok(installer_data, expected_sha256):
        installer_path = save_installer(installer_data)
        run_installer(installer_path)
        delete_installer(installer_path)

def get_expected_sha256():
    url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/SHA256SUMS'
    response = requests.get(url)
    expected_hash = ''
    for line in response.text.splitlines():
        if 'vlc-3.0.17.4-win64.exe' in line:
            expected_hash = line.split()[0]
            break
    return expected_hash

def download_installer():
    url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    response = requests.get(url)
    return response.content

def installer_ok(installer_data, expected_sha256):
 computed_hash = hashlib.sha256(installer_data).hexdigest()
 return computed_hash == expected_sha256

def save_installer(installer_data):
    temp_folder = os.getenv('TEMP')
    installer_path = os.path.join(temp_folder, 'vlc-3.0.17.4-win64.exe')
    with open(installer_path, 'wb') as f:
        f.write(installer_data)
    return installer_path

def run_installer(installer_path):
    subprocess.run([installer_path, '/L=1033', '/S'])

def delete_installer(installer_path):
    os.remove(installer_path)

if __name__ == '__main__':
    main()

    
   

