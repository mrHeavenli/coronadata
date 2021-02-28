# coronadata

Hardcoded python script that gets covid cases and deaths from [here](https://www.worldometers.info/coronavirus/)

## How to use
```python
from covid_data import get_globaldata
print(get_global_data())

```
The output will look something like this:
```json
{'cases': 114427110, 'deaths': 2538469}
```
