# DualFM-Python
## A python module for the DualFM API

### Examples:

#### Song and artist:
```py
import dualapi

print(dualapi.Now.song)
print(dualapi.Now.artist)
```
#### Listeners:
```py
import dualapi

print(dualapi.Listeners.current)
print(dualapi.Listeners.Peak)
```
#### Presenter:
```py
import dualapi

print(dualapi.Presenter.username)
```
