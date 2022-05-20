import copy


def create_tuples(state):
    
    tuples = []
    temp = []
    
    for lst in state:
        
        if len(lst) == 1:
            
            temp.append((0, lst[0]))  #the block is on the table
            
        else:
    
            for i in (range(len(lst)-1)):
                temp.append((lst[i], lst[i+1]))     #the block in on another block
            
        tuples.append(temp)
        temp = []   
        
    return tuples

def difference(old_state,new_state): 
    diff = [element for element in new_state if element not in old_state] 
    return diff


def calc_goal_heuristic(state):
    
    l = len(state)
    h_counter = 0
    heu = 0
    
    for lst in state:
        
        l = len(lst)
        h_counter = sum(range(l))
        heu  = heu +  h_counter
            
    return heu

def calc_state_heuristic(state,goal):  
            
    h_counter = 0
    heu = 0
    unmatch = 0
   
    
    for lst_state in state:
        for lst_goal in goal:
                
            match_index_of_state = [i for i, el in enumerate(lst_state) if el in lst_goal]
            
            if lst_state!= lst_goal[:len(match_index_of_state)]:
                
                unmatch+=1
                
            elif lst_state == lst_goal[:len(match_index_of_state)]:
                    
                unmatch-=1
                
        if unmatch == len(goal):
            
            h_counter = -1*sum(range(len(lst_state)))
            heu  = heu +  h_counter
            unmatch = 0
            
        elif unmatch < len(goal):
            
            h_counter = sum(range(len(lst_state)))
            heu  = heu +  h_counter
            unmatch = 0
            
            
                 
    return heu        

def block_moves(curr_state,goal):
    
    len_curr_state = len(curr_state)  #total list(s) of blocks
    temp_heuristic_values = []
    temp =  []
    temp_state = []
    
    
    for lst in curr_state:
            
        for i in range(len_curr_state):
                
            lst_index  = curr_state.index(lst)
            
            if i == lst_index:
                
                len_lst = len(lst)
                temp = copy.deepcopy(curr_state)
                temp[lst_index].pop() #pick the block
                place = lst[len_lst-1]
                temp.append([place]) #place the block on table
                temp = [ele for ele in temp if ele != []]
                temp_state.append(temp)
                temp_heuristic = calc_state_heuristic(temp,goal)
                temp_heuristic_values.append(temp_heuristic)
                
            else:
                
                len_lst = len(lst)
                temp = copy.deepcopy(curr_state)
                temp[lst_index].pop() #pick the block
                place = lst[len_lst-1]
                temp[i].append(place) #place the block on another block
                temp = [ele for ele in temp if ele != []]
                temp_state.append(temp)
                
                temp_heuristic = calc_state_heuristic(temp,goal)
                temp_heuristic_values.append(temp_heuristic)
                
                
    return temp_state, temp_heuristic_values       