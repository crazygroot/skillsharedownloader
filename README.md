# Skillshare video downloader in python (Updated)

I needed offline access to some skillshare courses I wanted to take while on vacation.
Video download is only available in the skillshare mobile apps and I didn't want to
choose between shaky 3G streaming or watching on a tiny mobile screen so I put together a
quick and dirty video downloader in python.

### Support your content creators, do NOT use this for piracy!

You will need a skillshare premium account to access premium content.
This script will not handle login for you.

1. Download the [chrome extension](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm/related "Cookie-Editor")

2. Log-in to skillshare in your browser click on the cookie-editor icon and copy the PHPSESSID


3. Grab the PHPSESSID id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#### Example:
```
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

```
