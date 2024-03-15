import requests

# Get info
info = requests.__dict__

# Extract
version = info['__version__']
license = info['__license__']
copyright = info['__copyright__']
author = info['__author__']
author_email = info['__author_email__']
doc_url = info['__url__']
title = info['__title__']
description = info['__description__']

# Print 
print("Requests Module Information:")
print("Version:", version)
print("License:", license)
print("Copyright:", copyright)
print("Author:", author)
print("Author Email:", author_email)
print("Document URL:", doc_url)
print("Title:", title)
print("Description:", description)