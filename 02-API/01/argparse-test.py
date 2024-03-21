import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Get a sentence from the user')

# Add an argument to accept the user's sentence
parser.add_argument('--sentence', type=str, help='The sentence provided by the user')

# Parse the command-line arguments
args = parser.parse_args()

# Access the user-provided sentence
user_sentence = args.sentence

# Display the user-provided sentence
print("User-provided sentence:", user_sentence)