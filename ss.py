import sys
import re
from downloader import Downloader

phpsessid= sys.argv[1]
cookie = "PHPSESSID="+phpsessid
dl = Downloader(cookie=cookie)

# download by class URL:
course_url = sys.argv[2]
dl.download_course_by_url(course_url)

if len(sys.argv) != 3:
    raise Exception('Invalid arguments. Usage : {program} <cookie> <url_or_class_id>'.format(program=sys.argv[0]))

if re.match(r'^[0-9]+$', sys.argv[2]):
	dl.download_course_by_class_id(sys.argv[2])

else:
	dl.download_course_by_url(sys.argv[2])
