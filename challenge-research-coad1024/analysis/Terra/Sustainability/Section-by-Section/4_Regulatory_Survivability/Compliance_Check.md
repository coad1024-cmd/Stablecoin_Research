# 4. Regulatory Survivability (The Moat)

Terra operated under the assumption of "DeFi Immunity." This assumption was false.

## 1. Custody & Banking Exposure
*   **The Risk**: Reliance on centralized rails (CEXs) for LUNA liquidity.
*   **Terra State**: Heavy dependence on Binance and Curve (technically DeFi, but large pools).
*   **LFG Reserves**: The BTC reserves were held in custody or multi-sigs that could theoretically be targeted, though LFG was a Singaporean non-profit.
*   **Score**: **Medium**. The protocol itself was decentralized code, but the *liquidity* required to maintain the peg lived on regulated venues.

## 2. Centralization of Control (The "TFL" Factor)
*   **The Entity**: Terraform Labs (Do Kwon).
*   **The Risk**: "Key Person Risk" and regulatory enforcement.
*   **Terra State**: TFL effectively controlled development, governance proposals, and the LFG reserve strategy.
*   **Impact**: When the crash happened, the market looked to *Do Kwon* for updates, not the protocol.
*   **Verdict**: **High Risk**. The system was not sovereign; it was TFL-dependent.

## 3. Securities Law
*   **The Test**: Howey Test.
*   **Terra State**:
    *   **Investment of Money**: Yes (buying LUNA/UST).
    *   **Common Enterprise**: Yes (TFL/LFG).
    *   **Expectation of Profit**: Yes (Anchor 20% APY).
    *   **Effort of Others**: Yes (TFL's management of the peg).
*   **Verdict**: **Failed**. The structure was highly likely to be classified as an unregistered securities offering (as later charged by the SEC).

## 4. Censorship Resistance
*   **The validators**: Top validators were often institutional entities.
*   **The Risk**: Coordinate shutdown.
*   **Reality**: During the crash, the chain *was* halted by validators to prevent governance attacks. This proves the chain was not censorship-resistant; it was a managed database under stress.

## 5. On-Ramp/Off-Ramp Dependencies
*   **The Bridge**: Shuttle Bridge (ETH), IBC (Cosmos).
*   **The Risk**: Bridge hacks or freezes.
*   **Terra State**: Robust bridging, but the value flowed *out* during the crash, draining the ecosystem.
