import urllib.request

# Perform a simple GET request to the AWS homepage
response = urllib.request.urlopen('https://aws.amazon.com')

# Read and print the response
data = response.read()
print(data)
