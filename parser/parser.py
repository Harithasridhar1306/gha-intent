import markdown
from bs4 import BeautifulSoup

def parse_md(file):
    with open(file) as f:
        html = markdown.markdown(f.read())

    soup = BeautifulSoup(html, "html.parser")
    spec = {}

    for h2 in soup.find_all("h2"):
        section = h2.text.lower()
        items = {}

        ul = h2.find_next_sibling("ul")
        if ul:
            for li in ul.find_all("li"):
                if ":" in li.text:
                    key, value = li.text.split(":", 1)
                    items[key.strip()] = value.strip()

        spec[section] = items

    return spec
