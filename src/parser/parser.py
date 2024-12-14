from src.lexer.lexer import TokenType
from src.ast.nodes import BinaryOperationNode, NumberNode

class Parser:
    """Converts tokens into an Abstract Syntax Tree"""
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        """Raise a syntax error"""
        raise Exception('Invalid syntax')
    
    def eat(self, token_type):
        """Validate and consume the current token"""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def factor(self):
        """Parse a factor (number or parenthesized expression)"""
        token = self.current_token
        
        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return NumberNode(token)
        
        if token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        
        self.error()
    
    def term(self):
        """Parse multiplication and division"""
        node = self.factor()
        
        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            
            if token.type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
            else:
                self.eat(TokenType.DIVIDE)
            
            node = BinaryOperationNode(left=node, operator=token, right=self.factor())
        
        return node
    
    def expr(self):
        """Parse addition and subtraction"""
        node = self.term()
        
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            else:
                self.eat(TokenType.MINUS)
            
            node = BinaryOperationNode(left=node, operator=token, right=self.term())
        
        return node
    
    def parse(self):
        """Parse the entire input and return the AST"""
        return self.expr()