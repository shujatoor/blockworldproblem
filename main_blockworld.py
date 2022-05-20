import copy
from blockworldAgent import block_moves
from blockworldAgent import calc_goal_heuristic
from blockworldAgent import create_tuples
from blockworldAgent import difference
    
initial = [["A", "B", "C"], ["D", "E"]]
goal =    [["A", "C"], ["D", "E", "B"]]
              
goal_heuristic_val = calc_goal_heuristic(goal)

moves = []
diff = []

while True:
    
    possible_states, temp_heuristic_values = block_moves(initial,goal) #all the possible state and their heuristic values   
    i = temp_heuristic_values.index(max(temp_heuristic_values))    
    temp_state =  possible_states[i]   #the best state as its heuristic value will be the maximum of all possible states
    
    initial_tuple = create_tuples(initial)   #tuples of initial state
    temp_tuple = create_tuples(temp_state)   #tuples of temp state
    d = difference(initial_tuple, temp_tuple)
    [diff.extend(list) for list in d]  #the move tgat achived the new state
    moves.append(diff[len(diff)-1])
    
    
    temp_heuristic_val = temp_heuristic_values[i]
    initial = copy.deepcopy(temp_state)
    
    if temp_heuristic_val == goal_heuristic_val:
        
        break
    
    else:
        
        continue

print('\n\nFinal State as it has achieved the goal state: ', initial)
print('\n\nAll the block moves to achieve the goal state: ', moves)