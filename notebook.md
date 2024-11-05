# Table of Contents
- [Table of Contents](#table-of-contents)
- [Note to reader](#note-to-reader)
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