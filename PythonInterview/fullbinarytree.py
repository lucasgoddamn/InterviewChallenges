

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
   def tree2str(self, t: Node):
      ans = ''
      def pot(node, s):
         if node == None or node.data == 0:
            return ''
         if node.left == node.right == None:
            return str(node.data)
         ss = str(node.data)
         if node.left != None:
            ss = ss + '(' + pot(node.left, '') + ')'
         else:
            ss = ss + '()'
         if node.right != None:
            ss = ss + '(' + pot(node.right, '') + ')'
         return ss
      return pot(t, '')


def fullbinary(node):
    if not node:
        return None
    left = fullbinary(node.left)
    right = node.right(node.right)
    if (left and right) or (not left and not right):
        node.left = left
        node.right = right
        return node
    if left:
        return left
    if right:
        return right


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.right.left = Node(5)
tree.right.right = Node(6)
ob = Solution()
x = fullbinary(tree)
print(ob.tree2str(x))