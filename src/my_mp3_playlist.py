import os

def write_to_file(lines):
  out_string = '\n'.join(lines)
  out_filename = 'adam_mp3s.html' 
  with open(out_filename, 'w') as outf:
    outf.write(out_string)
  result_file = os.getcwd() + '/' + out_filename
  print "\nCheck out this file:\n\n", result_file

mp3dir = "/storage/6339-6436/Music/"
mp3s = os.listdir(mp3dir)
mp3s.sort()

# Number each mp3 song in our list
for i in range(len(mp3s)):
  song = os.path.splitext(mp3s[i])[0] # strip ".mp3" from the filename
  mp3s[i] = str(i+1) +". " + song + "<br />" # add an HTML line break tag for websites that mess up line spacing

out_dir ="/sdcard/Download/"
os.chdir(out_dir)
write_to_file(mp3s)
