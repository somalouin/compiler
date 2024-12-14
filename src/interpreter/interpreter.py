from src.lexer.lexer import TokenType

class Interpreter:
    """Evaluates the Abstract Syntax Tree"""
    def visit_binary_operation(self, node):
        """Handle binary operations"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if node.operator.type == TokenType.PLUS:
            return left + right
        elif node.operator.type == TokenType.MINUS:
            return left - right
        elif node.operator.type == TokenType.MULTIPLY:
            return left * right
        elif node.operator.type == TokenType.DIVIDE:
            return left / right
    
    def visit_number(self, node):
        """Return the numeric value"""
        return node.value
    
    def visit(self, node):
        """Dispatch to the appropriate visit method"""
        method_name = f'visit_{node.__class__.__name__.lower()}'
        method = getattr(self, method_name)
        return method(node)
    
    def interpret(self, tree):
        """Interpret the entire AST"""
        return self.visit(tree)