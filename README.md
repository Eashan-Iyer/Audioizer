# Audioizer
Summary:
Graphing calculators are programs that visualize functions. Analogously, this program sonifies functions, outputting waveforms with a frequency that evolves with respect to time, based on the function. I was inspired to make this program to answer the question, "what does math sound like?". I have included two sample outputs, converted to .mp3 files. 

Usage:
In order to use the program, type in a function of t after lambda t; there is a comment of code indicating this line. This program will produce a .wav audio file once you run it. The program starts the file t=0, and ends at t=duration (duration is a parameter the user can set). The range of output frequencies is theoretically arbitrary but limited by your speakers and ears (aim for an output range between 20 Hz and 20 kHz and try to make more use of the lower end of this spectrum).

Limitations and Warnings:
This program currently sonifies the derivative of a function that is inputted. I tried to fix this with integration (with SciPy quad), but this led to a huge increase in the runtime of the program. Thus, it is best to integrate whatever you want to sonify before you input it into the calculator. This limits the program to functions that have a closed-form antiderivative. If you wish to work with a function that does not have a closed-form antiderivative, my recommendation is to input the integral of a partial Taylor Series. If there does not exist a locally convergent Taylor Series (the function is non-analytic), then there are other methods that could be used (i.e. Fourier Series). 

Since frequency is always positive, this program is not capable of outputting frequencies that correspond to negative numbers. If you use a function with negative values, the program will map them to frequencies based on their absolute value. 

Make sure that the output frequencies of the function are within the range of human hearing, otherwise, the program will output something that can't be heard. For reference, this is about 20 Hz to 20 kHz. The output of the function corresponds to the frequency of a sound at a particular time.

Do not listen to loud and high-pitched sounds, and exercise caution while using headphones. Misuse of the program can lead to permanent hearing loss.
