print("Water Jug Problem")

def goal(state, target):
    return target in state  

def next_states(state, capacities):
    next_states = []
    x, y = state  
    a, b = capacities  
    
    next_states.append((a, y))
    next_states.append((x, b))
    next_states.append((0, y))
    next_states.append((x, 0))
    pour = min(x, b - y)  
    next_states.append((x - pour, y + pour))
    
    pour = min(y, a - x)  
    next_states.append((x + pour, y - pour))
    
    return next_states

def dfs(start, capacities, target):
    stack = [start]
    visited = set()
    parent = {start: None}
    
    while stack:
        state = stack.pop()
        
        if goal(state, target):
            path = []
            while state:
                path.append(state)
                state = parent[state]
            path.reverse()
            return path  # Return solution path
        
        if state in visited:
            continue
        
        visited.add(state)
        
        for next_state in next_states(state, capacities):
            if next_state not in visited and next_state not in parent:
                parent[next_state] = state
                stack.append(next_state)
    
    return None  # No solution found

def print_solution(path):
    if path:
        print("Solution Found:")
        for step in path:
            print(f"Jug 1: {step[0]}L, Jug 2: {step[1]}L")
    else:
        print("No solution water jug problem")

jug1_capacity = 5
jug2_capacity = 4
target_amount = 3

solution = dfs((0, 0), (jug1_capacity, jug2_capacity), target_amount)
print_solution(solution )


