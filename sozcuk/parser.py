from bs4 import BeautifulSoup
import re
import html2text
TITLE = ""


def run(arg, html_code, div="div"):
    dizi = []
    soup = BeautifulSoup(arg, "html.parser")
    global TITLE
    TITLE = soup.title.text
    entry = soup.find_all(div, html_code)
    for i in entry:
        dizi.append(parser(i))
    return dizi


def parser(arg):
    arg = str(arg)
    ht = html2text.HTML2Text()
    ht.ignore_links = True
    sonuc = ht.handle(arg)
    sonuc = re.sub(r"[\s]+", " ", sonuc)
    return sonuc.strip()


#def pager(html_code):
#    soup = BeautifulSoup(html_code, "html.parser")
#    page = str(soup.find("div", "pager"))
#    son_sayfa = re.findall("\d", page)
#    if son_sayfa:
#        return son_sayfa[1]
#    else:
#        return 0
