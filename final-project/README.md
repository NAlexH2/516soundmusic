# Table of Contents
- [Table of Contents](#table-of-contents)
- [Python Version](#python-version)
    - [**This project absolutely requires Python 3.10 or newer!**](#this-project-absolutely-requires-python-310-or-newer)
- [About This Project](#about-this-project)
- [How to Run](#how-to-run)
- [Writeup - Experience, Lessons Learned, Future Work](#writeup---experience-lessons-learned-future-work)
  - [Experience](#experience)
    - [Standing Wave](#standing-wave)
    - [Interactive](#interactive)


# Python Version
### **This project absolutely requires Python 3.10 or newer!**

# About This Project
This project is 2 different types of guitar tuners.
1. Standing wave - listen to the generated tone and play the relevant string
2. Interactive - use a microphone plugged into your computer to do a short
recording to automatically detect how close it is to the note picked.


# How to Run
Before running highly recommend creating a python virtual environment.
After that, start the virtual env, then install `requirements.txt` like so:
```BASH
(.venv).../$ pip install -r requirements.txt
```

From here you can run the script with the following:

`python tuner.py` - On Windows

`python3 tuner.py` - On *most* POSIX like (Mac, Linux) based systems.

To see the usage run `python tuner.py -h` for all the relevant and command line
options.

# Writeup - Experience, Lessons Learned, Future Work

## Experience
This was a lot harder and more involved that I thought it would be. When I asked
Bart about doing this project he said:
> "Sure just make it fancy!"

Which left me with a major question mark of "How do you make a fancy tuner?" 
I decided that making a tuner that was multi-modal would be pretty neat. Turns 
out that was the right way to go.

The three I wanted to (axed the last one) were...
1. **Standing Wave** - simply listen and play the same note on the instrument and 
tune accordingly
2. **Interactive** - provided a note and a recording device, do a short recording of
the note on the instrument and see how close they are by comparing the fundamental
frequency to the actual frequency and letting the user know how close they are.
3. **Automatic** (not done, removed due to Bart saying don't sweat it) - Provided 
a recording device, the user can play a note and the script will automatically 
detect which note was played, and how far off it was from the frequency that 
note is normally. No input or menu selection from the user required, runs 
constantly until the user stops.

### Standing Wave
I started with the standing wave version to get my feet wet. This was simple 
enough and worked out really well. When I started working on the project, this 
version had issues of a pop in the audio loop, asking Bart he said I would need 
to do enveloping, and that we hadn't learned that yet. Eventually I taught 
myself how to do it.

In the `apply_fade` function, using fractional sizing, that then is applied to 
the multiplicative for both the fade in and fade out sections of the wave being 
generated. This both starts and stops at absolute 0 because of the setup.

```python
if note.size < 2 * fade_samples:
    half = note.size // 2
    fade_in = np.linspace(0, 1, half)
    fade_out = np.linspace(1, 0, half)
else:
    fade_in = global_fade_in
    fade_out = global_fade_out
note[: fade_in.size] *= fade_in
note[-fade_out.size :] *= fade_out
return note
```

The note wave is generated before this step, this is the last step before it's 
played out to the systems default output device (sounddevice does this by 
default.)

That's really the extent of the work I had to do, and didn't take most of my 
time overall in the project. That's reserved for the next two sections.

### Interactive
This was revisited several times and ultimately the final step of the project.

