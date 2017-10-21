# spdx-licenses

This module exports the license information from https://spdx.org/licenses/.

```python
import licenses from 'spdx-licenses'
for lic in licenses:
  print(lic['name'])
```

## Development

Install the development dependencies via `nodepy-pm install`. Then run
the following to update the `licenses.json` file.

    $ nodepy generate > licenses.json
