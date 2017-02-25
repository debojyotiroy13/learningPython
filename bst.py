class Node:
    def __init__(self,val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data :
            if(root.l_child == None):
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if(root.r_child == None):
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)



def findLcaDepth(root,start,end,distanceToLCA):
    if root is None:
        return 0
    else:
        if start.data < root.data and end.data < root.data :
            return findLcaDepth(root.l_child,start,end,distanceToLCA+1)
        if start.data > root.data and end.data > root.data :
            return findLcaDepth(root.r_child,start,end,distanceToLCA+1)
        return distanceToLCA

def findDepthOfElement(root,node,depth):
    if root is None : 
        return 0
    else:
        if(root.data > node.data):
            return findDepthOfElement(root.l_child,node, depth + 1)
        if(root.data < node.data):
            return findDepthOfElement(root.r_child,node, depth + 1)
        return depth

def findElementsBetween(root,start,end):
    lcaNodeDepth = findLcaDepth(root,start,end,0)
    print 'lcaNodeDepth ' + str(lcaNodeDepth)
    depthStart = findDepthOfElement(root,start,0)
    depthEnd = findDepthOfElement(root,end,0)
    print depthStart
    print depthEnd
    print "distance between " + str(start.data) + " and " + str(end.data) + " is " + str(depthStart + depthEnd - 2* lcaNodeDepth)
root = Node(18)
arr = [36, 9, 6, 12, 10, 1, 8]
for item in arr:
    binary_insert(root,Node(item))

pre_order_print(root)
print "length from lca"
findElementsBetween(root,Node(1),Node(10))