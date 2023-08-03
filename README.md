# stalgcm-abstractmodel
STALGCM Machine Project: Abstract Model of Computation

A python implementation of a Deterministic Pushdown Automata.

To run, simply open up the **DPDA_GUI.py** file and run said file. 

The program requires a text file that contains a machine definition. The machine definition should have the following format:
{states}
{input symbols}
{stack symbols}
{start state}
{initial stack symbol}
{final state}
{transitions}
...

After selecting which machine definition to use, enter an input string to be tested on the machine. Once done, click on the "Check" button to obtain the results of whether or not the machine accepts or rejects the string, and the step-by-step tracing of the machine.

The package should also contain numerous sample files for how a machine definition should be constructed. The said samples also have the following definitions for easier comprehension.
- dpda.txt - balanced pairs of ( and )
- dpda2.txt - 0^n, 1^n; n >= 0
- dpda3.txt - empty string (for testing purposes)
- dpda4.txt - wcw^R, where w = {a,b}*

You may also create your own machine definition file. Do note that it should follow the format stated above.

Lastly, the "Reset" button is to simply reset the text fields. You may or may not use the button when using a new machine definition or entering a new input, as doing so or not will not break the machine.

---
Created by: Adrian Yung Cheng, Krizchelle Wong, and Angelo Guerra<br>
Date Submitted: August 2023
