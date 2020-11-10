# dunst-scripts

## Installation

1. Clone the repository
```
$ git clone https://github.com/turbo5353/dunst-scripts.git
```
2. Install pyalsaaudio
```
$ pip install pyalsaaudio
```

## volume.py

This script changes the current volume and displays a notification using dunstify.
Configuration is done by changing the variables at the beginning of the script.

### Example usage

Display the current volume in a notification

```
$ ./volume.py
```

Increase the current volume by  5

```
$ ./volume.py 5
```

Decrease the current volume by 10
```
$ ./volume.py -10
```

Toggle mute
```
$ ./volume.py toggle
```
