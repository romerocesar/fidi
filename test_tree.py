import tree
import logging

logging.basicConfig(level=logging.DEBUG)

def test_from_array():
     A = list(range(9))
     actual = tree.from_array(A)
     logging.debug(actual)
     logging.debug(tree.from_array([1, 2]))
     assert 0


def test_lca():
    # arrange
    dag = tree.TreeNode(3)


def test_every_bst():
    assert len(tree.every_bst(1, 3)) == 5
