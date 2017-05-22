# nodepy/spdx-licenses

This module exports the license information from https://spdx.org/licenses/.

```python
licenses = require('@nodepy/spdx-licenses')
for lic in licenses:
  print(lic['name'])
```

## Development

Install the development dependencies via `nppm install --dev`. Then run
the following to update the `licenses.json` file.

    $ nodepy generate > licenses.json
