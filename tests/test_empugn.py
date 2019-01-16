from yattag import indent

from empugn import empugn
from empugn.input import parse


def test_empugn():
    data = parse('''
html:
  - head:
      - title: Empugn example
      - link:
          rel: stylesheet
          href: foo.css
      - script: |
          alert('Hello, World');
  - body:
      - h1: Sole text child may be specified as-is
      - p:
          - "Separating links by "
          - a:
              href: https://google.com
              target: _blank
              children: space
          - " may require quoting"
      - div:
    '''.strip())
    assert indent(empugn(data), '  ').strip() == '''
<!DOCTYPE html>
<html>
  <head>
    <title>Empugn example</title>
    <link rel="stylesheet" href="foo.css" />
    <script>alert('Hello, World');
</script>
  </head>
  <body>
    <h1>Sole text child may be specified as-is</h1>
    <p>Separating links by <a href="https://google.com" target="_blank">space</a> may require quoting</p>
    <div></div>
  </body>
</html>
    '''.strip()
