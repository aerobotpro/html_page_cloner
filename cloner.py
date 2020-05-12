from requests_html import HTMLSession
import webbrowser
from os import getcwd

site = input("Enter a URL to clone >>>:")

session = HTMLSession()
r = session.get(site)

r.html.render()
#print(r.text)
fileloc = f'{getcwd()}/index.html'
with open(fileloc, "w+", encoding="utf-8") as f:
    f.write(r.text)

webbrowser.open("file:///" + fileloc)
