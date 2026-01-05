from source.Tokens.token import Token

class LendingPool:
    """
    A simplified model of a lending pool.
    Allows users to deposit collateral and borrow other assets.
    """
    def __init__(self, interest_rate: float = 0.02):
        """
        Initializes the LendingPool.
        Args:
            interest_rate (float): The interest rate for borrowing from the pool.
        """
        self.deposits = {}
        self.loans = {}
        self.interest_rate = interest_rate

    def deposit(self, user: object, token: Token, amount: float):
        """
        Deposits collateral into the lending pool.
        """
        if user not in self.deposits:
            self.deposits[user] = {}
        self.deposits[user][token] = self.deposits[user].get(token, 0) + amount

    def borrow(self, user: object, token: Token, amount: float, ltv_limit: float = 0.5):
        """
        Borrows an asset from the pool.
        """
        if user not in self.deposits:
            raise ValueError("User has no collateral to borrow against.")

        collateral_value = 0
        for collateral_token, collateral_amount in self.deposits[user].items():
            collateral_value += collateral_token.price * collateral_amount
        
        borrow_power = collateral_value * ltv_limit

        if token.price * amount > borrow_power:
            raise ValueError("Borrow amount exceeds borrow power.")

        if user not in self.loans:
            self.loans[user] = {}
        self.loans[user][token] = self.loans[user].get(token, 0) + amount
        
        return True

    def repay(self, user: object, token: Token, amount: float):
        """
        Repays a loan.
        """
        if user not in self.loans or token not in self.loans[user]:
            raise ValueError("User has no loan for this token.")

        if amount > self.loans[user][token]:
            amount = self.loans[user][token] # Repay the full loan if amount is greater

        self.loans[user][token] -= amount
        
        # Simple interest calculation
        interest = amount * self.interest_rate
        return interest
