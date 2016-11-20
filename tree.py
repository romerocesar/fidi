class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def reconstruct(pre, inorder):
    relem = pre[0]
    ri = index(root, inorder)
    left = [:ri]
    right = [ri+1:]
    rleft = reconstruct(pre[1:len(left)], left)
    rright = reconstruct(pre[len(left)+1:], right)
    return BTree(left = rleft, right= rright, root=relem)


def search(dag, x):
    '''returns a path as a list of values from the root of the tree to x
    or -1 if x is not in dag. Assumes values in dag are unique.'''
    if not dag:
        return (False, -1)
    if dag.val == x:
        return (True, [x])
    found, path = search(dag.left, x)
    if found:
        return (True, [dag.val] + path)
    found, path = search(dag.right, x)
    if found:
        return (True, [dag.val] + path)

    return (False, -1)


def lca(dag, v, w):
    '''The lowest common ancestor (LCA) of two nodes is the lowest
    (i.e. deepest) node that has both v and w as descendants.
    '''
    vfound, vpath = search(dag, v)
    wfound, wpath = search(dag, w)
    if not vfound or not wfound:
        return -1
    path = vpath if len(vpath) <= len(wpath) else wpath
    ans = -1
    for i, x in enumerate(path):
        if vpath[i] != wpath[i]:
            break
        ans = vpath[i]
    return ans


def invertTree(root):
    '''Swaps left and right children for every node in the tree'''
    if not root:
        return root
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
