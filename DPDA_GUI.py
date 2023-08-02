import tkinter as tk
from tkinter import filedialog
from DPDA import DPDA

class DPDA_GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DPDA Simulator")

        # Create file button and label
        file_button = tk.Button(self.window, text="Select DPDA file", command=self.select_file)
        file_button.grid(row=0, column=0, padx=5, pady=5)
        
        definition_label = tk.Label(self.window, text="DPDA Definition:")
        definition_label.grid(row=0, column=1, padx=5, pady=5, sticky="S")

        self.dpda_text = tk.Text(self.window, height=15, width=30)
        self.dpda_text.grid(row=1, column=1, rowspan=8, padx=5, pady=5, sticky="N")

        self.file_label = tk.Label(self.window, text="")
        self.file_label.grid(row=1, column=0, padx=5, pady=5)

        # Create input label and text field
        input_label = tk.Label(self.window, text="Input:")
        input_label.grid(row=2, column=0, padx=5, pady=5)

        self.input_entry = tk.Entry(self.window)
        self.input_entry.grid(row=3, column=0, padx=5, pady=5)

        # Create output label and text field
        output_label = tk.Label(self.window, text="Output:")
        output_label.grid(row=4, column=0, padx=5, pady=5)

        self.output_text = tk.Text(self.window, height=1, width=20)
        self.output_text.grid(row=5, column=0, padx=5, pady=5)

        # Create trace label and text field
        trace_label = tk.Label(self.window, text="Trace:")
        trace_label.grid(row=6, column=0, padx=5, pady=5)

        self.trace_text = tk.Text(self.window, height=10, width=50)
        self.trace_text.grid(row=7, column=0, padx=5, pady=5)

        # Create accept button
        accept_button = tk.Button(self.window, text="Accept", command=self.accept_input)
        accept_button.grid(row=8, column=0, padx=5, pady=5)

        # Create reset button
        reset_button = tk.Button(self.window, text="Reset", command=self.reset_input)
        reset_button.grid(row=9, column=0, padx=5, pady=5)

        self.dpda = None

    def select_file(self):
        # Open file dialog to select DPDA definition file
        filename = filedialog.askopenfilename()
        self.file_label.config(text=filename)

        # Read DPDA definition from file
        with open(filename, 'r') as f:
            lines = f.readlines()

        states = set(lines[0].strip().split(','))
        input_alphabet = set(lines[1].strip().split(','))
        stack_alphabet = set(lines[2].strip().split(','))
        start_state = lines[3].strip()
        start_stack_symbol = lines[4].strip()
        accept_states = set(lines[5].strip().split(','))

        transitions = {}
        for line in lines[6:]:
            parts = line.strip().split(',')
            current_state = parts[0]
            input_symbol = parts[1]
            stack_symbol = parts[2]
            new_state = parts[3]
            new_stack_symbol = parts[4]
            transitions[(current_state, input_symbol)] = (new_state, stack_symbol, new_stack_symbol)

        self.dpda = DPDA(states, input_alphabet, stack_alphabet, transitions, start_state, start_stack_symbol, accept_states)

        # Display DPDA definition in text field
        self.dpda_text.delete(1.0, tk.END)
        self.dpda_text.insert(tk.END, "States: " + ', '.join(states) + "\n")
        self.dpda_text.insert(tk.END, "Input alphabet: " + ', '.join(input_alphabet) + "\n")
        self.dpda_text.insert(tk.END, "Stack alphabet: " + ', '.join(stack_alphabet) + "\n")
        self.dpda_text.insert(tk.END, "Start state: " + start_state + "\n")
        self.dpda_text.insert(tk.END, "Start stack symbol: " + start_stack_symbol + "\n")
        self.dpda_text.insert(tk.END, "Accept states: " + ', '.join(accept_states) + "\n")
        self.dpda_text.insert(tk.END, "Transitions:\n")
        # for transition, new_state in transitions.items():
        #     self.dpda_text.insert(tk.END, ','.join(transition) + ',' + ','.join(new_state) + "\n")
        
        # print(transitions.items())
            
        for transition, new_state in transitions.items():
            formatted_transition = f"({transition[0]}, {transition[1]}) = ({new_state[0]}, {new_state[1]}, {new_state[2]})"
            self.dpda_text.insert(tk.END, formatted_transition + "\n")

    def accept_input(self):
        # Run DPDA on input string
        input_string = self.input_entry.get()
        result, trace = self.dpda.accepts_with_trace(input_string)

        # Display output
        if result:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Accepted")
        else:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Rejected")

        # Display DPDA trace
        self.trace_index = 0
        self.trace_text.delete(1.0, tk.END)
        remaining_input = input_string
        for state, _, stack in trace:
            step = [state, remaining_input, str(stack)]
            self.trace_text.insert(tk.END, ','.join(step) + "\n")
            remaining_input = remaining_input[1:]

    def reset_input(self):
        self.dpda = None
        self.file_label.config(text="")
        self.dpda_text.delete(1.0, tk.END)
        self.input_entry.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.trace_text.delete(1.0, tk.END)

    def run(self):
        self.window.mainloop()
        
gui = DPDA_GUI()
gui.run()