import sys, os
from downloader import Downloader
phpsessid= sys.argv[1]
cookie = "PHPSESSID="+phpsessid

dl = Downloader(cookie=cookie)

# download by class URL:
course_url = sys.argv[2]
dl.download_course_by_url(course_url)

# or by class ID:
# dl.download_course_by_class_id(189505397)
