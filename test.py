import os
import re

# specify the root directory to start searching for music files
root_directory = '/path'

# specify the output file name
output_file = 'song_titles.txt'

# initialize an empty regex pattern for matching music file extensions
pattern = re.compile('.(mp3|wav|flac|m4a)$')

# initialize an empty list to store song titles
song_titles = []

# recursively search for music files in the directory tree
for root, dirs, files in os.walk(root_directory):
    # loop through each file in the current directory
    for file in files:
        # check if the file matches the music file extension pattern
        if pattern.match(file):
            # construct the full file path
            file_path = os.path.join(root, file)
            # get the song title by removing the file extension
            song_title = file[:-4]
            # add the song title to the list
            song_titles.append(song_title)

# write the song titles to the output file
with open(output_file, 'a') as f:
    for title in song_titles:
        f.write(f'{title}\n')

print(f'Song titles written to {output_file}')
