# Copyright (c) 2017 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
Generates the list of licenses by parsing the HTML from
https://spdx.org/licenses/. Requires the development dependencies
and Python 3.
"""

from bs4 import BeautifulSoup
import json
import requests
import sys

def error(message, code=1):
  print('Error:', message)
  sys.exit(code)

def gettext(node):
  return ''.join(node.find_all(text=True, recursive=True))

def main():
  doc = BeautifulSoup(requests.get('https://spdx.org/licenses/').text, 'html.parser')
  tables = doc.find_all('table')
  if len(tables) != 2:
    error('expected two <table/> nodes')

  licenses = []
  for row in tables[0].find_all('tr'):
    if row.parent.name != 'tbody': continue
    cells = row.find_all('td')
    licenses.append({
      'name': gettext(cells[0]),
      'identifier': gettext(cells[1]).strip(),
      'osi_approved': gettext(cells[2]).strip() == 'Y',
      'deprecated': False
    })
  for row in tables[1].find_all('tr'):
    if row.parent.name != 'tbody': continue
    cells = row.find_all('td')
    licenses.append({
      'name': gettext(cells[0]),
      'identifier': gettext(cells[1]).strip(),
      'osi_approved': False,
      'deprecated': True
    })

  json.dump(licenses, sys.stdout, indent=2)

if require.main == module:
  main()
