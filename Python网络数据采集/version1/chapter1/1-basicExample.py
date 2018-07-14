from urllib.request import urlopen

# Retrieve HTML string from the URL
html = urlopen("https://www.google.com.hk/?gws_rd=ssl")
print(html.read())
print("\n\n\n\n\n")
html = urlopen("https://pythonscraping.com/pages/page1.html")
print(html.read())