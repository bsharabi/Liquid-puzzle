class Inode:
   
    def __init__(self) -> None:
        pass
    
    def getValue(self):
        pass
    
    def setValue(self):
        pass
    
    def getNeighbors(self):
        pass
    
    def setNeighbors(self):
        pass
    
    
class node:
    
    def __init__(self,value:list[list[int]],neighbors:list[Inode]=None) -> None:
        self.value=value
        self.neighbors=neighbors    
        
        
    def getValue(self) ->list[list[int]]:
        return self.value
    
    def setValue(self,value:list[list[int]])->None:
        self.value=value
    
    def getNeighbors(self)->list[Inode]:
        return self.neighbors
    
    def setNeighbors(self,neighbors:list[Inode])->None:
        self.neighbors=   neighbors 


def init(tube_number:int,color_number:int,empty_tube_number:int):
    if tube_number+empty_tube_number <=color_number:
        return None
    tubes = [[i for _ in range(4)] if i < tube_number else [] for i in range(tube_number + empty_tube_number)]
    return tubes
        
    

def build(root: Inode, color_diff: int = 2, element_in_tube: int = 4) -> None:
    if root is None:
        return

    # Get the current node's value
    current_value = root.getValue()

    # Generate neighbors
    neighbors = []

    # Iterate over each tube in the current node's value
    for i in range(len(current_value)):
        current_tube:list = current_value[i]

        if not bool(current_tube):
            continue
        if len(current_tube)>=2 and current_tube[0]!=current_tube[1]:
            continue
        
        
        

    # Set the generated neighbors for the current node
    root.setNeighbors(neighbors)

    # Recursively build neighbors for each generated node
    for neighbor in neighbors:
        build(neighbor, color_diff, element_in_tube)
    

    
def print_tree(root: Inode, depth: int = 0) -> None:
    if root is None:
        return

    # Print the current node's value
    print("  " * depth, root.getValue())

    # Print children recursively
    for neighbor in root.getNeighbors():
        print_tree(neighbor, depth + 1)

tubes = init(2,2,1)
root =node(tubes)   
print(tubes)
build(root,1)

print_tree(root)