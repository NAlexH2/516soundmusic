# Table of Contents
- [Table of Contents](#table-of-contents)
- [Python Version](#python-version)
    - [**This project absolutely requires Python 3.10 or newer!**](#this-project-absolutely-requires-python-310-or-newer)
- [About This Project](#about-this-project)
- [How to Run](#how-to-run)
- [Writeup - Experience, Lessons Learned, Future Work](#writeup---experience-lessons-learned-future-work)


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
