from collections import defaultdict

def configure_grid(stacks):
    return stacks

def get_stack_height(grid):
    return max(len(stack) for stack in grid)

def canonical_string_conversion(grid):
    final_string = ''
    for stack in sorted(grid):
        final_string += stack + ";"
    return final_string

def is_solved(grid, stack_height):
    for stack in grid:
        if not stack:
            continue
        elif len(stack) < stack_height:
            return False
        elif stack.count(stack[0]) != stack_height:
            return False
    return True

def is_valid_move(source_stack, destination_stack, height):
    if not source_stack or len(destination_stack) == height:
        return False

    color_freqs = source_stack.count(source_stack[0])
    if color_freqs == height:
        return False

    if not destination_stack:
        if color_freqs == len(source_stack):
            return False
        return True

    return source_stack[-1] == destination_stack[-1]

def solve_puzzle(grid, stack_height, visited, answer_mod):
    if stack_height == -1:
        stack_height = get_stack_height(grid)

    visited.add(canonical_string_conversion(grid))

    for i, source_stack in enumerate(grid):
        for j, destination_stack in enumerate(grid):
            if i == j:
                continue
            if is_valid_move(source_stack, destination_stack, stack_height):
                new_grid = grid[:]
                new_grid[j] += new_grid[i][-1]
                new_grid[i] = new_grid[i][:-1]

                if is_solved(new_grid, stack_height):
                    answer_mod.append([i, j, 1])
                    return True

                if canonical_string_conversion(new_grid) not in visited:
                    solve_for_the_rest = solve_puzzle(new_grid, stack_height, visited, answer_mod)
                    if solve_for_the_rest:
                        last_move = answer_mod[-1]
                        if last_move[0] == i and last_move[1] == j:
                            answer_mod[-1][2] += 1
                        else:
                            answer_mod.append([i, j, 1])
                        return True
    return False

def check_grid(grid,empty):
    number_of_stacks = len(grid)
    stack_height = get_stack_height(grid)
    num_balls_expected = (number_of_stacks - empty) * stack_height
    num_balls = sum(len(stack) for stack in grid)

    if num_balls != num_balls_expected:
        print("Grid has incorrect # of balls")
        return False

    ball_color_frequency = defaultdict(int)
    for stack in grid:
        for ball in stack:
            ball_color_frequency[ball] += 1

    for ball_color, frequency in ball_color_frequency.items():
        if frequency != stack_height:
            print(f"Color {ball_color} is not {stack_height}")
            return False

    return True

def run(stacksNumber):
    # Including 2 empty stacks
    color = {0: 'r',1: 'b',2: 'g',3:'y',4: 'o',5: 'l',6: 'd',7: 'p'}
    stacks=[]
    empty = 0
    for i in stacksNumber:
        s=""
        for j in i:
            s+=color[j] 
        stacks.append(s)
        if s =="":
            empty+=1
    grid = configure_grid(stacks)

    if not check_grid(grid,empty):
        print("Invalid Grid")
        return

    stack_height = get_stack_height(grid)
    if is_solved(grid, stack_height):
        print("Problem is already solved")
        return

    visited = set()
    answer_mod = []

    solve_puzzle(grid, stack_height, visited, answer_mod)

    # Since the values of Answers are appended
    # When the problem was completely
    # solved and backwards from there
    answer_mod.reverse()
    print(answer_mod)
    for v in answer_mod:
        print(f"Move {v[0] + 1} to {v[1] + 1} {v[2]} times")
    return answer_mod

def main():
    # Including 2 empty stacks
    stacks = ['byloopdb', 'ggrroydp', 'gbboldrg', 'rddloppy', 'yobrlpoo', 'pdggybrr', 'pyybglld', 'pdllygbr', '', '']
   
    grid = configure_grid(stacks)

    if not check_grid(grid,2):
        print("Invalid Grid")
        return

    stack_height = get_stack_height(grid)
    if is_solved(grid, stack_height):
        print("Problem is already solved")
        return

    visited = set()
    answer_mod = []

    solve_puzzle(grid, stack_height, visited, answer_mod)

    # Since the values of Answers are appended
    # When the problem was completely
    # solved and backwards from there
    answer_mod.reverse()
   
    for v in answer_mod:
        print(f"Move {v[0] + 1} to {v[1] + 1} {v[2]} times")
    return answer_mod
if __name__ == "__main__":
    run([[1,3,5,4,4,7,6,1],
                    [2,2,0,0,4,3,6,7],
                    [2,1,1,4,5,6,0,2],
                    [0,6,6,5,4,7,7,3],
                    [3,4,1,0,5,7,4,4],
                    [7,6,2,2,3,1,0,0],
                    [7,3,3,1,2,5,5,6],
                    [7,6,5,5,3,2,1,0],[],[]])
