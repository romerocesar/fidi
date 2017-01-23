class TreeNode:

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


    def __str__(self):
        return '({} {} {})'.format(self.left, self.val, self.right)


def from_array(A, l=0, u=None):
    'from sorted array A'
    if u is None:
        u = len(A) - 1
    if u < l:
        return None
    elif u == l:
        return TreeNode(A[l])
    root = (l + u) // 2
    ans = TreeNode(A[root])
    ans.left = from_array(A, l, root - 1)
    ans.right = from_array(A, root + 1, u)
    return ans


def reconstruct(pre, inorder):
    relem = pre[0]
    ri = index(root, inorder)
    left = inorder[:ri]
    right = inorder[ri+1:]
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


def every_bst(lo=1, hi=3):
    '''Generates all structurally unique BSTs that store values 1..n'''
    # import pdb;pdb.set_trace()
    ans = []
    for root in range(lo, hi+1):
        for right in every_bst(root+1, hi):
            for left in every_bst(lo, root-1):
                ans.append(TreeNode(root, left=left, right=right))
    ans = ans or [None]
    return ans
