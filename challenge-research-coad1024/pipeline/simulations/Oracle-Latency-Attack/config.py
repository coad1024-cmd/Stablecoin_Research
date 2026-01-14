"""
Oracle Latency Attack Simulation - Configuration

Model parameters derived from Terra Core x/oracle and x/market modules.
"""

# =============================================================================
# ORACLE PARAMETERS (x/oracle)
# =============================================================================
VOTE_PERIOD_BLOCKS = 5          # Number of blocks per oracle vote period
BLOCK_TIME_SECONDS = 6          # Average block time on Terra Classic
ORACLE_DELAY_SECONDS = VOTE_PERIOD_BLOCKS * BLOCK_TIME_SECONDS  # ~30 seconds

# Oracle price tolerance
ORACLE_REWARD_BAND = 0.02       # 2% price deviation tolerance for rewards

# =============================================================================
# MARKET PARAMETERS (x/market)
# =============================================================================
BASE_POOL_USD = 1_000_000_000   # $1B initial virtual pool size
MIN_SPREAD = 0.005              # 0.5% minimum stability spread (Tobin tax)
MAX_SPREAD = 0.60               # 60% maximum spread during stress

# Pool recovery (spread decay)
POOL_RECOVERY_PERIOD_BLOCKS = 14400  # ~24 hours at 6s blocks

# =============================================================================
# ATTACK SCENARIO PARAMETERS
# =============================================================================
# Price crash scenarios to model
PRICE_CRASH_SCENARIOS = [
    0.05,   # 5% crash
    0.10,   # 10% crash
    0.15,   # 15% crash
    0.20,   # 20% crash (from Deep Dive example)
    0.30,   # 30% crash
    0.50,   # 50% flash crash
]

# Crash speed (how fast LUNA drops)
CRASH_DURATION_SECONDS = 15     # Price crashes in 15 seconds

# Attacker capital (USD)
ATTACKER_CAPITAL = 10_000_000   # $10M attack capital

# Transaction costs
GAS_COST_USD = 0.50             # Average gas cost per swap
SLIPPAGE_TOLERANCE = 0.01       # 1% slippage tolerance

# =============================================================================
# SIMULATION PARAMETERS
# =============================================================================
NUM_SIMULATIONS = 1000          # Monte Carlo runs
RANDOM_SEED = 42                # Reproducibility

# Time discretization
TIMESTEP_SECONDS = 1            # 1 second resolution
SIMULATION_DURATION_SECONDS = 120  # 2 minute window around crash
