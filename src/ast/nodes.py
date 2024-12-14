class AST:
    """Base class for Abstract Syntax Tree nodes"""
    pass

class BinaryOperationNode(AST):
    """Represents binary operations like addition, subtraction"""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class NumberNode(AST):
    """Represents a numeric value"""
    def __init__(self, token):
        self.token = token
        self.value = token.value