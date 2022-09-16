
class Node():

    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None




#recursive 
def depth_first_rec(root):
    if root is None:
        return []
    # stack = [root]
    # current = stack.pop
    lefttree = depth_first_rec(root.left) # [c]
    rightree = depth_first_rec(root.right) #[b,d,e]
    return [root.val, *lefttree,*rightree] #[a,c,b,d,e]



# iterative 
def depth_first_it(root):
    if root is None:
        return []
    
    stack = [root]
    res = []

    while(stack):
        
        current = stack.pop()
        res.append(current.val)


        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return res
        



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')


a.right = b
a.left = c
b.left = d
b.right = e



print(depth_first_it(a))
print(depth_first_rec(a))

        