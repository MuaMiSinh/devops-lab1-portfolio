"""Check required portfolio content and basic HTML structure using stdlib only."""
from html.parser import HTMLParser
from pathlib import Path


class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.text = []
        self.lang = None
        self.viewport = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'meta' and attrs.get('name') == 'viewport':
            self.viewport = True

    def handle_data(self, data):
        self.text.append(data)


source = Path('index.html').read_text(encoding='utf-8')
parser = PortfolioParser()
parser.feed(source)
assert source.lstrip().lower().startswith('<!doctype html>'), 'Missing HTML5 doctype'
assert parser.lang == 'vi', 'Expected Vietnamese document language'
assert parser.viewport, 'Missing responsive viewport'
assert all(tag in parser.tags for tag in ['title', 'main', 'h1']), 'Missing page landmarks'
text = ' '.join(parser.text)
for required in ['Mua Mí Sính', 'DTC235180159', 'KTPM K22C', 'DevOps', 'GitHub Actions']:
    assert required in text, f'Missing portfolio content: {required}'
assert '</html>' in source.lower(), 'Document is incomplete'
print(f'PASS: index.html ({len(source.encode("utf-8"))} bytes), student content, landmarks, viewport')
