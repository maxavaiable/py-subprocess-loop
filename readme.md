# [subprocess-loop](https://pypi.org/project/subprocess-loop)

<!-- change above url according to repo -->

This is a project for exchanging data with the main process using standard input and output (stdio) in JSON format

## Installation

```bash
pip install subprocess-loop
```

### Running subprocess code:

```python
# child.py
import subprocess_loop

def on_request(request):
    return request+1

subprocess_loop.Child.run(on_request)
```
