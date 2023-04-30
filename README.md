# Audioizer
Summary:
Graphing calculators are programs that visualize functions. Analogously, this program sonifies functions, outputting waveforms with frequency that evolves with respect to time based on the function. I was inspired to make this program to create more sensory intuition in mathematics.

Notes for using the program:
This program currently sonifies the derivative of whatever function is put in. I tried to fix this with integration (by scipy quad), but this led to a huge increase in the runtime of the program. Thus, you should integrate whatever you want to sonify before you input it into the calculator. This means thay you can only sonify functions that have a closed-form antiderivative. 

Since frequency is always positive, this program is not capable of outputting frequencies that correspond to negative numbers. If you use a function with negative values, the program will map them to frequencies based on their absolute value. 

Make sure that the output frequencies of the function are within the range of human hearing, otherwise it will seem like the program does not work. For reference, this is about 20 Hz to 20 kHz. 

Do not listen to loud and high pitched sounds, and exercise caution while using headphones. Misuse of the program can lead to permanent hearing loss.
