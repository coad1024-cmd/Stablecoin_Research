# Detailed Architecture & Logic Diagram

```mermaid
graph LR
    classDef logic fill:#f9f,stroke:#333,stroke-width:2px;
    classDef storage fill:#ff9,stroke:#333,stroke-width:2px;
    classDef actor fill:#9cf,stroke:#333,stroke-width:2px;
    classDef event fill:#f99,stroke:#333,stroke-width:2px;

    User[User]:::actor
    Market[Secondary Market]:::actor
    Oracle[Price Oracle]:::actor
    Keeper[Keeper Bot]:::actor

    subgraph CoreContract [Core Smart Contract]
        direction TB
        State[State Variables]:::storage
        Logic[Logic Engine]:::logic
        
        State <--> Logic
        
        subgraph InternalState [Internal State]
            beta["Conversion (β)"]
            v["Time (v_t)"]
            Assets["ETH Balance"]
        end
    end

    %% --- Interaction Flows ---
    User -->|Deposit| Logic
    User -->|Redeem| Logic
    Oracle -->|Price P_t| Logic
    Keeper -->|Trigger Reset| Logic
    User -->|Trade| Market

    %% --- Connect Logic to Detailed Engine ---
    Logic -.->|Executes| CalcNAV

    %% --- Detailed Calculation Logic ---
    subgraph LogicEngine [Internal Logic Flow]
        direction TB
        
        CalcNAV[1. Calculate NAV]
        
        CheckTriggers[2. Check Triggers]
        
        Trigger1{"Payout?"}
        Trigger2{"Up Reset?"}
        Trigger3{"Down Reset?"}

        CalcNAV -->|V_A, V_B| CheckTriggers
        CheckTriggers --> Trigger1
        Trigger1 -- No --> Trigger2
        Trigger2 -- No --> Trigger3
        
        EventReg[Regular Payout]:::event
        Trigger1 -- Yes --> EventReg
        
        EventUp[Upward Reset]:::event
        Trigger2 -- Yes --> EventUp
        
        EventDown[Downward Reset]:::event
        Trigger3 -- Yes --> EventDown
    end
    
    %% --- Tranching ---
    subgraph TokenClasses [Token Classes]
        direction TB
        ClassA[Class A Stable]
        ClassB[Class B Lev]
    end
    
    Logic -->|Mint/Burn| ClassA
    Logic -->|Mint/Burn| ClassB
```

## Key Equations & Parameters

### 1. Leverage Parameter ($\alpha$)

The leverage is determined by the initial split ratio.

- **Formula**: Initial Leverage $= \frac{1}{1 - \alpha}$
- **In this Paper**: $\alpha = 0.5$ (Implies a 50/50 split of capital).
- **Result**: Initial Leverage = 2x. Class B invests \$1 (his own) + \$1 (borrowed from A) = \$2 exposure.

### 2. Beta ($\beta$) Calculation

Beta adjusts the "Quantity of Coins" to keep the "Value per Coin" at $\$1.00$ immediately after a reset.

- **Regular Payout Update**:
  $$ \beta_{new} = \beta_{old} \times \frac{2 P_t}{2 P_t - \beta_{old} P_0 R T} $$
- **Reset Update (Up/Down)**:
  $$ \beta_{new} = \frac{P_t}{P_0} $$

### 3. Net Asset Value (NAV)

Used **only** for triggers (not for trading).

- **Class A**: $V_A(t) = 1 + (R \times v_t)$
- **Class B**: $V_B(t) = \frac{2 P_t}{\beta_t P_0} - V_A(t)$

### 4. Triggers

- **Regular Payout**: $v_t \ge T$
- **Upward Reset**: $V_B \ge H_u$ (e.g., $2.0$)
- **Downward Reset**: $V_B \le H_d$ (e.g., $0.25$)
