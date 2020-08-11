# DualFM-Python
## A python module for the DualFM API

### Examples:

#### Song, artist and encoderError:
```py
import dualapi

print(dualapi.Now.song)
print(dualapi.Now.artist)
print(dualapi.Now.encoderError)
```
#### Listeners:
```py
import dualapi

print(dualapi.Listeners.current)
print(dualapi.Listeners.peak)
```
#### Presenter and if `AutoDJ` is live:
```py
import dualapi

print(dualapi.Presenter.username)
print(dualapi.Presenter.autodj)
```
#### Version:
```py
import dualapi

print(dualapi.version)
```
