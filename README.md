# Audioizer
Summary:
Graphing calculators are programs that visualize functions. Analogously, this program sonifies functions, outputting waveforms with frequency that evolves with respect to time based on the function. I was inspired to make this program to create more sensory intuition in mathematics.

Usage:
In order to use the program, type in a function of t after lambda t; there is a comment of code indicating this. This program will produces a .wav audio file. The program starts the file t=0, and ends at t=duration (duration is a parameter the user can set). The range of output frequencies is arbitrary, but limited by your speakers and ears.

Limitations and Warnings:
This program currently sonifies the derivative of whatever function is inputted. I tried to fix this with integration (by scipy quad), but this led to a huge increase in the runtime of the program. Thus, it is best to integrate whatever you want to sonify before you input it into the calculator. This limits the program to functions that have a closed-form antiderivative. A clever way of avoiding this is to input a partial taylor/fourier approximation of the function, and then integrate that. 

Since frequency is always positive, this program is not capable of outputting frequencies that correspond to negative numbers. If you use a function with negative values, the program will map them to frequencies based on their absolute value. 

Make sure that the output frequencies of the function are within the range of human hearing, otherwise the program will output something that can't be heard. For reference, this is about 20 Hz to 20 kHz. The output of the function corresponds to the frequency of a sound at an instant of time.

Do not listen to loud and high pitched sounds, and exercise caution while using headphones. Misuse of the program can lead to permanent hearing loss.
