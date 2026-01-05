from source.Tokens.token import Token
from source.liquidity_pools.liquidity_pool import LiquidityPool


class Attacker:
    """
    Represents an attacker in the market simulation.
    The attacker has a wallet and can perform malicious actions, such as swapping large
    amounts of tokens to de-peg a stablecoin.
    """

    def __init__(self, initial_wallet: dict[Token, float]):
        """
        Initializes the Attacker with an initial wallet balance.

        Args:
            initial_wallet (dict[Token, float]): A dictionary mapping tokens to their quantities.
        """
        self.wallet = initial_wallet
        self.short_positions = {}  # Stores short positions: {token: {'amount': float, 'entry_price': float}}
        self.realized_pnl = 0.0

    def swap(self, pool: LiquidityPool, token_in: Token, amount_in: float):
        """
        Performs a swap in a given liquidity pool.

        Args:
            pool (LiquidityPool): The liquidity pool to perform the swap in.
            token_in (Token): The token to swap.
            amount_in (float): The amount of the token to swap.

        Returns:
            tuple[Token, float]: The output token and the amount received.
        """
        if self.wallet.get(token_in, 0) < amount_in:
            raise ValueError("Attacker does not have enough tokens to perform the swap.")

        self.wallet[token_in] -= amount_in
        token_out, amount_out = pool.swap(token_in, amount_in)

        self.wallet[token_out] = self.wallet.get(token_out, 0) + amount_out

        return token_out, amount_out

    def open_short(self, token: Token, amount: float):
        """
        Opens a short position on a token.
        Mocks the borrowing and selling process:
        1. Borrow 'amount' of token (adds liability).
        2. Sell 'amount' of token at current price (adds cash to wallet).
        
        For simplicity, we assume infinite liquidity for simple shorting (or OTC).
        """
        entry_price = token.price
        if token not in self.short_positions:
            self.short_positions[token] = {'amount': 0.0, 'entry_price': 0.0} # Weighted average entry
        
        # Update weighted average entry price
        current = self.short_positions[token]
        total_value = (current['amount'] * current['entry_price']) + (amount * entry_price)
        new_amount = current['amount'] + amount
        new_entry_price = total_value / new_amount if new_amount > 0 else 0
        
        self.short_positions[token] = {'amount': new_amount, 'entry_price': new_entry_price}
        
        # In a real short, you get the cash from selling the borrowed asset
        # We assume the attacker effectively holds the USD value of the sold asset
        # But also has the obligation to buy it back.
        # To verify PnL correctly, we track the 'cash from short' separately or just PnL.
        # Let's keep it simple: Profit = (Entry Price - Exit Price) * Amount
        # We won't modify the 'wallet' token balances directly to avoid confusion with the swap logic,
        # unless we introduce a 'USD' token explicitly in the wallet.
        
        # Assuming we are shorting against USD reference
        # self.wallet[reference_token] += amount * entry_price 
        # But we don't have reference to reference token here easily without passing it.
        # So we will just track the position and calculate PnL.
        pass

    def close_short(self, token: Token):
        """
        Closes the entire short position for a token.
        """
        if token not in self.short_positions:
            return 0.0
            
        position = self.short_positions[token]
        amount = position['amount']
        entry_price = position['entry_price']
        exit_price = token.price
        
        pnl = (entry_price - exit_price) * amount
        self.realized_pnl += pnl
        
        del self.short_positions[token]
        return pnl

    def get_portfolio_value(self) -> float:
        """
        Calculates the total value of the attacker's portfolio in terms of the reference currency (USD).
        Includes wallet assets + Unrealized PnL from shorts + Realized PnL.

        Returns:
            float: The total value of the attacker's portfolio.
        """
        total_value = 0.0
        # Wallet Assets
        for token, quantity in self.wallet.items():
            total_value += token.price * quantity
            
        # Unrealized PnL from Shorts
        for token, position in self.short_positions.items():
            price_diff = position['entry_price'] - token.price
            unrealized_pnl = price_diff * position['amount']
            total_value += unrealized_pnl
            
        # Realized PnL
        total_value += self.realized_pnl
        
        return total_value
