import sys
import os

#os.system('cd ~/dev/scripts/XKCD')
first = int(sys.argv[1]) if len(sys.argv) > 1 else 1
last = int(sys.argv[2]) if len(sys.argv) > 2 else 1537

for i in range(first,last+1):
    os.system('wget -o log.txt http://www.xkcd.com/' + str(i))
    file = open(str(i), 'r')
    file_text = file.read()
    image_url = file_text.split('<img src="//')[2].split('"')[0]
    os.system('wget -o log.txt "' + image_url + '"')
    file_name = image_url.split("/")[-1].replace("(", "\(").replace(")", "\)")
    ext = file_name.split(".")[-1]
    os.system('mv ' + file_name + ' comic_' + str(i) + "." + ext)
    os.system('rm -f ' + str(i))
