class DPDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transitions, start_state, start_stack_symbol, accept_states):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol
        self.accept_states = accept_states
    
    def accepts_with_trace(self, input_string):
        stack = [self.start_stack_symbol]
        current_state = self.start_state
        trace = [(current_state, input_string, stack[:])]

        for input_symbol in input_string:

            if (current_state, input_symbol) not in self.transitions:
                print("false")
                return False, trace
            new_state, pop_symbol, push_symbol = self.transitions[(current_state, input_symbol)]
            if pop_symbol != '':
                stack.pop()
            if push_symbol != '':
                stack.extend(list(push_symbol)[::-1])
            current_state = new_state
            trace.append((current_state, input_string, stack[:]))
            # print(trace)
            
            
        if input_string == '':
            input_symbol = ''
            while (current_state, input_symbol) in self.transitions:
                if (current_state, input_symbol) not in self.transitions:
                    print("false")
                    return False, trace
                new_state, pop_symbol, push_symbol = self.transitions[(current_state, input_symbol)]
                if pop_symbol != '':
                    stack.pop()
                if push_symbol != '':
                    stack.extend(list(push_symbol)[::-1])
                current_state = new_state
                trace.append((current_state, input_string, stack[:]))
                # print(trace)
            
        if stack and stack[-1] == 'Z':
            input_symbol = ''
            new_state, pop_symbol, push_symbol = self.transitions[(current_state, input_symbol)]
            stack.pop()
            current_state = new_state
            trace.append((current_state, input_string, stack[:]))

        print("current: "+current_state)
        result = current_state in self.accept_states and len(stack) == 0
        # print(result, trace)
        return result, trace

# # Read DPDA definition from file
# filename = "dpda2.txt"

# with open(filename, 'r') as file:
#     lines = file.readlines()

# states = set(lines[0].strip().split(','))
# input_alphabet = set(lines[1].strip().split(','))
# stack_alphabet = set(lines[2].strip().split(','))
# start_state = lines[3].strip()
# start_stack_symbol = lines[4].strip()
# accept_states = set(lines[5].strip().split(','))
# transitions = {}
# for line in lines[6:]:
#     parts = line.strip().split(',')
#     current_state = parts[0]
#     input_symbol = parts[1]
#     pop_symbol = parts[2]
#     new_state = parts[3]
#     push_symbol = parts[4]
#     transitions[(current_state, input_symbol)] = (new_state, pop_symbol, push_symbol)
# dpda = DPDA(states, input_alphabet, stack_alphabet, transitions, start_state, start_stack_symbol, accept_states)
# # Prompt user for input string0
# input_string = input("Enter input string: ")
# result = dpda.accepts_with_trace(input_string)
# if result:
#     print("Accepted")
# else:
#     print("Rejected")