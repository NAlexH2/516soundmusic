# popgen: play a pop music loop
Bart Massey 2024

This Python program generates a pseudo-melody using chord
and bass notes from the [Axis
Progression](https://en.wikipedia.org/wiki/axis_progression).

Right now, the controls are limited and the output is pretty
terrible.

A sample is available in [`demo.wav`](demo.wav).

# License

This work is licensed under the "MIT License". Please see the file
`LICENSE.txt` in this distribution for license terms.


# Changes by Alex
I added enveloping to fade between notes. You can find most of it under 
this commit id:
[`b02873e6d36dfc610666d9f1a039a0bf878f8f52`](https://github.com/NAlexH2/516soundmusic/commit/b02873e6d36dfc610666d9f1a039a0bf878f8f52)

If that doesn't satisfy you, you can also find my changes in `popgen.py` 
on lines 206 -> 266.