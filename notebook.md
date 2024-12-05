# Table of Contents
- [Table of Contents](#table-of-contents)
- [Note to reader](#note-to-reader)
- [12/5/2024](#1252024)
- [12/3/24 and 12/4/24 - Working with Bart and solo.](#12324-and-12424---working-with-bart-and-solo)
  - [12/3/24 - with Bart](#12324---with-bart)
  - [12/4/24 - with Bart/Solo](#12424---with-bartsolo)
  - [12/4/24 - 3PM](#12424---3pm)
  - [12/4/24 - 7PM](#12424---7pm)
- [12/2/24 - 2:00 PM -\> 6:09 PM - Wrapping the project up today... I hope...](#12224---200-pm---609-pm---wrapping-the-project-up-today-i-hope)
- [12/1/24 - 12:48 PM - About working today...](#12124---1248-pm---about-working-today)
- [11/30/24 - 9:32 AM - Working on Final Project](#113024---932-am---working-on-final-project)
- [11/26/24 - 2:20PM -\> 6:00PM - Setup and Work On Final Portfolio Objective](#112624---220pm---600pm---setup-and-work-on-final-portfolio-objective)
  - [Commence working notes here:](#commence-working-notes-here)
    - [Personal side note and feelings going through the class](#personal-side-note-and-feelings-going-through-the-class)
  - [What else?](#what-else)
- [11/18/24 1:40AM - Final Project Touchups/Verify Windows Install](#111824-140am---final-project-touchupsverify-windows-install)
- [11/7/24 11:30PM - 5:00PM - Final Project Work](#11724-1130pm---500pm---final-project-work)
- [11/5/24 11:30AM - Starting final project/Laying out plans](#11524-1130am---starting-final-projectlaying-out-plans)
- [11/2/2024 - HW2 Continued](#1122024---hw2-continued)
- [10/29/2024 - HW2 Start](#10292024---hw2-start)
- [10/15/2024 - 3pm - Watching recorded lectures](#10152024---3pm---watching-recorded-lectures)
  - [Musical Notes Lecture](#musical-notes-lecture)
  - [FIR Filters (Finite Impulse Response Filters)](#fir-filters-finite-impulse-response-filters)
  - [Audio Filters](#audio-filters)
  - [Fourier Transform](#fourier-transform)
  - [Discrete Fourier Transforms](#discrete-fourier-transforms)
  - [Applying The DFT](#applying-the-dft)
- [10/13/2024 - 9pm - Working on and finishing hw1](#10132024---9pm---working-on-and-finishing-hw1)
- [10/13/2024 - 1:30pm - Saying "Hi"](#10132024---130pm---saying-hi)
- [10/6/2024 - 3pm - Setting Up for Class](#1062024---3pm---setting-up-for-class)

# Note to reader
The table of contents are in order from newest entry to oldest. That is 
the newest entries are at the top of the table of contents while the 
oldest is at the bottom.

Table of contents are generated using a VSCode extension called 
"Markdown All In One." Very useful tool.

# 12/5/2024
- Argparse added to a forked branch and tested.
- Cleaned up code.
- Tested all options and over tuned and under tuned strings on guitar.
  - All tests passed with satisfaction.
  - There is an issue where if a string is ***very*** out of tune, it won't 
  detect the fundamental frequency properly. But this is HIGHLY irregular, and 
  I cannot stress how *bad* the string must be tuned to be incorrect.
- Next step, the writeup.

# 12/3/24 and 12/4/24 - Working with Bart and solo.
## 12/3/24 - with Bart
  - Tried to figure out why the automatic was so problematic with Bart
  - Discovered a million other things...
    - Issues with device selection
    - Issues with audio capturing
    - Issues with sounddevice vs pyaudio
      - Wound up only using sounddevice
    - Issues with laptop microphone being absolutely awful so not able to do 
    a lot of work on it.
    - Issues with Automatic detection and Interactive
  - Regarding interactive
    - It worked when analyzing the dominate frequency, but not the right way to
    do this step.
    - Need to look at the first peak and use it as the fundamental. With this, 
    can then analyze and determine if it's the right choice.

## 12/4/24 - with Bart/Solo
  - Fixed many things I found issues with after speaking with Bart.
  - Moved everything to sounddevice (soooo much easier!!!)
  - Streams aren't a thing in the interactive anymore (awesome!)
  - My laptop microphone is absolutely useless. Not going to do anymore work 
  with it.
    - Absolutely garbage tier microphones.
  - Webcam mic at home is great for this though.
    - Going to do more coding at home with it.
  - Fixed menus
    - Will be replacing with arguments and argparse.
  - Got the OK from Bart to just put the automatic on pause and get the 
  interactive working instead.
    - For the interactive, that's a long term goal. Going to remove it from
    the options entirely.
  - For my experience and knowledge even after going through this class, this 
  is proving to be way harder than I expected for myself.
  - Addressing the fundamental frequency detection though:
    - There's ways I'm coming up with to tackle it...
    - But... The worst way is to hack a function together to parse very 
    specific ranges of the sample and averaging out those frequencies to see if
    they are close enough to the expected fundamental one.
      - Very not ideal...
    - I'm still brewing up solutions though.
  - The overall writeup for the project will be in the [final-project/README.md](final-project/README.md)
  - Going to suspend this work session until I get home. I feel like I'm really 
  close, just need a decent mic that isn't my garbage laptops setup.

## 12/4/24 - 3PM
  - Discovered that the fender tuner app on my phone doesn't produce a high 
  enough quality of any note for the microphone to pick it up properly...
    - I've been banging my head against a wall I constructed...
    - With my guitar at my house, played, recorded, saved, and analyzed and the 
    first peak IS the correct frequency, note, everything!!!!
  - Also learned that sound device lists EVERY possible configuration of a 
  device and had to figure out which one would be the best option for the user
  to read/pick from (even when I put argparse in)
  - Doing a bit more digging and Bart telling me it was a peaks issue, I have
  spent several hours playing with `scipy.signal.find_peaks()` to get the peaks 
  returned object just right for each chord (mostly ignoring noisy neighbor 
  peaks) I feel super confident in what I have.
    - It will committed in a following commit after I commit these notes.
  
## 12/4/24 - 7PM
  - That prev commit mentioned went out. Cleaned up some stuff. 
  Not quite done. Going to do some argparsing stuff tomorrow and getting that
  ball rolling.
  
# 12/2/24 - 2:00 PM -> 6:09 PM - Wrapping the project up today... I hope...
> We'll see...
- Found an article that can help move me forward on writing the automatic 
detection, but it focuses more on a large range of notes, but I'm just focussing
on making a tuner specifically for guitars.
- This involved re-writing a few of the variables to better suit this stage of 
the project.
  - Specifically, what to display with the scaling approximation.
  - You'll see in [projGlobals.py](final-project/resources/projGlobals.py) that 
  it went to specific notes (E2 -> E4) instead of stating "E (low) -> E (high)"
- This is proving to be more difficult than I originally thought...
  - Having issues with live parsing the information because it's inaccurate 
  math (again...)
  - The input is calculated way too high.
  - The nearest note is very wrong (E2 == G3 for some reason????)
  - When adjusting code, it seemingly falls apart.
  - I'm going to commit the broken piece and work on it because I know that's 
  the route I need take.
- In working on the automatic, I found bugs in the interactive! Mostly because I
was jumping back to my previous work to check on how I did it there.
  - The E4 calc when searching for dominate frequencies was wrong.
  - E2 was right
  - However, if you plucked a low note when comparing against a higher, the 
  math was wrong.
    - Vice versa applies too.
- It turns out, this is much harder to do a 'live' listen and parsing than 
expected. I think it requires a better microphone than my webcam as well, but 
we'll see. I'm going to message Bart and ask for some assistance tomorrow after 
class.
- I think... I will want to switch back to PyAudio instead of using sounddevice
for this one. Since you have better control over the byte stream with it. 
  - Sounddevice likes to start and stop a lot, but that doesn't work here I
  think. Again, will need to seek advice/help.

# 12/1/24 - 12:48 PM - About working today...
- I decided I did enough yesterday. The final step can be saved for later this
week.

# 11/30/24 - 9:32 AM - Working on Final Project
- Plans today are the following:
  - Get live audio to be captured and detected on the interactive
  option of the tuner.
  - Do live processing of that data while capturing it to see how close
  it is to the note the user selected.
  - If this all goes well, get started on the automatic detection.
    - Research done on this part shows it's REALLY short and brief to 
    actually implement, but, we'll see.

- (10am) Starting with the live capture though... How did it go?
  - (2:30pm) Well had a few off by one issues so wrong devices were being 
  selected causing many issues.
    - This is where I spent most of my time.
  - This issue took me a long time.
  - During this I was also fighting with the way I was capturing
  audio. Wound up having to sample for 3 seconds and then 
  calculate the dominant frequency.
    - Dominant frequency is proving to be an issue too, but 
    only because it is 2x what the frequency is supposed to be
    
- (2:30pm) Regarding the dominant frequency...
  - For example, a high E note on a guitar (or any instrument, I suppose) 
  is registered at 329 Hz.
  - I tuned my guitar using another app to verify it was tuned correctly.
  - However, the dominant freq according to the python script is ~658 Hz, 
  which obviously isn't correct.
  - I suspect there's just a simple math error somewhere.
  - I do want to finish this step of the project today though. If the math 
  error just requires me to divide by 2, I will. I want to finish this step 
  so I can get started on the (seemingly) more direct and easier 
  automatic detection.

- Did I find the math error?
  - Yes and no. Low E and High E on a guitar are being silly for some reason.
  - So those get divided by 2.
  - All other notes do not.
- Another weird thing is sometimes when you start the recording the first time,
it thinks it's way too high or too low, as if the captured values got cut off at
the start or the end.
  - This is outside my knowledge why it might be happening, but it is.
  - Running the note and recording again shows that there is not an issue at
  all.

- I am **very** happy with how todays progress went and will get started on the
final one soon - if not tomorrow (12/01/24). We'll see.

# 11/26/24 - 2:20PM -> 6:00PM - Setup and Work On Final Portfolio Objective
- Link to the [portfolio objective folder here](code/hw3-popgen).
- Finished setting up for the final portfolio objective.
- Will be working on it and adding comments regarding work done here.
- Would normally have a readme in the directory, but do not want to remove or 
change the one Bart has placed.

## Commence working notes here:
- Played demo.wav, will certainly be finding a way to do enveloping on the 
final results.
- Would like to see about trying different wave forms, we'll see...

### Personal side note and feelings going through the class
- I say "we'll see..." because I'm not very confident nor comfortable in this 
class because it's just been hard for me as a non-musician to *really* 
understand what is going on... 
  - I figured I'd be able to pick up on as the class goes, but I am not a
  musician nor terribly musically inclined and I am missing some key 
  fundamentals that need to be taught to me over a longer period of time.
  - This is due to the fact of just how I learn entirely new concepts, ideas, 
  and content. Slow burns, with time to really dig into what's happening.
  - Not related to the assignment, but I felt it needed to be said as the term 
  gets closer and closer to the end.
  - Doin' my best though!

> Back to the program....
- Researched what it would take to involve to remove that pop and came across 
[this Stack Overflow question](https://stackoverflow.com/questions/78266711/removing-click-and-pop-sounds-in-python) which gave me an idea on how to 
attempt a simple "fade" from one note to another.
  - The current idea is to just take the last 100 or so samples, and get the 
  average from there up to the first 100 of the next note, then find a way to
  distribute that average across the previous 100 samples to lead into that 
  final average.
  - This means if the next note is lower, the previous 100 samples decrease. 
  Higher, it increases.
- Lets see if this works...
  - **It didn't**
- Though realizing the error, I was only focused on the fade out with that 
article. I needed to also take care of the fade in so that both sides of 
the waves are equal.
  - I thought the fade in didn't matter because as long as one side fades out 
  nicely to 0, then it's all good. WRONG!
  - There still seemed to be a pop for whatever reason. Not significant, but 
  enough to be noticeable.
- However, I could tell that the heaviest samples at the start also had pop, so 
I applied a fade to those as well.
- You can find my added code and added comments in commit: 
[`b02873e6d36dfc610666d9f1a039a0bf878f8f52`](https://github.com/NAlexH2/516soundmusic/commit/b02873e6d36dfc610666d9f1a039a0bf878f8f52)
- This isn't perfect. Going from high to low or vice versa still has a subtle 
pop, but it's way better than what it was before!

## What else?
- I played with the program a bit and hadn't realized the bass was an... 
undertone? I believe that is what it's called. I thought each note actually had 
bass added to it, but it's almost as if another sin wave was riding under it. 
I just thought this was neat. You can find the files I generated at the link 
at the top of these notes.
  - This is most noticeable by [this file here.](code/hw3-popgen/fade_bass4_150bpm_C7Root.wav)
  **WARNING**: This is semi-high pitched, but no where near deafening. Keep your 
  volume just a tad low so you're not shocked by it.


# 11/18/24 1:40AM - Final Project Touchups/Verify Windows Install
- Had to reformat PC for a growing number of reasons
- Used the final project to test my Python install
- Fixed a typo.

# 11/7/24 11:30PM - 5:00PM - Final Project Work
- Adjust notes to self
- Added 3 classes to build off of so code is easier to parse
- Worked on the standing wave version. Would like to have a fancy menu to
toggle options on, off, or switch between notes. Would like to have
  - Would like to write this menu once and use in both the places where user
  has a menu to interact with.
  - Though, I recognize I'll probably have to write two different versions of it.
- Worked on menu ensuring that flows correctly and has correct prompts.
- Generated standing wave frequencies, tested each to verify sound is working.
  - Tested against a tuner on my phone to verify as well. Sanity check.
  - The tuner says things are right, but I am not musical and so I have doubts.
  - Did a bit of reading and found that adding harmonics can help. It did! My 
  standing wave of E2 sounds very close to a guitar. Now to repeat it for the 
  other notes for better pitch matching.
  - Had to fight with E4 though. That was hard to pitch match because of 
  **frequency aliasing problem between E4 and D3**. The tuner I was using was 
  detecting D3 when it was supposed to be E4. Adding and tweaking some 
  harmonics based on logic helped out a lot.
  - Also played each with my guitar and they sound REALLY close too! I call 
  this a part of the program a huge success!
- I tried using curses to create an interactive menu, but I need to do some work 
outside of this project to better understand how that works. So each one will 
have to be different.
- Using match/case statements because they are easier to read code wise.
  - YOU NEED PYTHON 3.10 OR NEWER!!!!!!
- Overall, this is a good place to stop. The Standing wave sounds nice. Given 
  enough time, I might make the standing waves sound *more* like a guitar. It 
  doesn't seem like it would be that difficult and I previously found a 
  resource that goes over this too.

# 11/5/24 11:30AM - Starting final project/Laying out plans
- Made notes to myself in code of what I would like to do. Specifically around 
what kind of tuner, and the options the user has. 
  - Do they want automatic detection?
  - Maybe someone would like to try and tune based off a standing wave?
  - Maybe they want to pick which note they are trying to specifically measure
    and give a approximate ratio/points value of how close/far off they are.
- Gave just some silly filler code to test with the current venv.
- This project won't accept and command line args since there's no reason to 
accept a file. Everything will be explained in line.

# 11/2/2024 - HW2 Continued
- Referencing the work I did with Bart on 10/31/24, 
I'm going to continue to work on and play with the 
current portfolio objective (hw2-adaptive)
- Adapted and utilized ideas from zulip to produce audible files 
that can be played back and analyzed. 
[See hw2 readme for more details](./code/hw2-adaptive/README.md)
- Performed more analysis on the data and files.

# 10/29/2024 - HW2 Start
- Setup Jupyter notebook
- Downloaded and added collectathon from class github repo added to this repo
- Made nearly 0 progress on figuring out the assignment.
- Need to ask for direct assistance soon.

# 10/15/2024 - 3pm - Watching recorded lectures
## Musical Notes Lecture
- Notes are sounds with fixed frequencies
- Western music uses a 12-tone scale
  - $note_i(f) = f * 2$<sup>$(i/12)$</sup>
  - $note_0 = f$
  - $note$<sub>$12$</sub>$(f) = 2f$
  - $note$<sub>-24</sub>$(f) = f/4$
- In MIDI `440Hz A` is key 69
  - Call this the `A` in `octave 4` or `A4`.
- Notes have particular time and length.
- "Polyphony" is when notes overlap
- ***Fundamental synthesis plan is to receive requests for notes, turn those into interesting musical sounds.***
## FIR Filters (Finite Impulse Response Filters)
- Convolution
  - Take a sequence of samples, convolve it with a sequence of coefficients.
- Characterize filters as impulse response
  - Impulse is just sample has max amplitude for single sample. As it traverses, it's got all 0 after it.
- Convolve with past samples and past outputs for the future samples.
  - Output of filter is used for input later.
- Some notation...
  - x[i] is the ith sample of input, y[i] is the ith sample of output. Amplitude of sample is assumed -1 .. 1
  - $y[i] = (x[i] + x[i-1])/2$

## Audio Filters
- What is a filter?
  - Changes the amplitude or phase of the frequencies of a sound.
- Ideal filters
  - Usually 0-1 with Passband, Stopband: goal is to block some range of freqs while leaving others alone.
  - low pass
  - high pass, bandpass, band notch

## Fourier Transform
- Lots of ugly math, not taking notes but [will leave myself a link to them for later](https://github.com/pdx-cs-sound/course-notes/blob/main/03-freq/01-fourier.md).

## Discrete Fourier Transforms
- More math, [more links](https://github.com/pdx-cs-sound/course-notes/blob/main/03-freq/02-dft.md).

## Applying The DFT
- FFT is crazy
  - Treat it as a black box
  - $O(N*lg(N))$

# 10/13/2024 - 9pm - Working on and finishing hw1
- I worked on rewriting the readme.md for the assignment. Essentially, moved
what I wrote here to there.

***Assignment completed***


# 10/13/2024 - 1:30pm - Saying "Hi"
- Just said "Hi". I'm not quite sure what to expect from this course 
so I just do not have much to say at this time.

# 10/6/2024 - 3pm - Setting Up for Class
- Just setting up for the class.