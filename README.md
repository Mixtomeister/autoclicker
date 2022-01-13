# autoclicker
I developed this autoclicker script made in Python to farm cookies in the Cookie Clicker.

I use the two mouse buttons to activate the autoclicker. One clicks intermittently until I stop pressing it and the other leaves the mouse clicking until I press it again or it moves 200 px in any direction to avoid missclicks because I forgot it was activated.

Dependencies:
- [pynput](https://github.com/moses-palmer/pynput)

Install and run:

- Create a virtualenv
```
~$ python -m virtualenv .venv
```

- Activate virtualenv
```
~$ source .venv/bin/activate
```

- Run script
```
(venv) ~$ python autoclicker.py
```