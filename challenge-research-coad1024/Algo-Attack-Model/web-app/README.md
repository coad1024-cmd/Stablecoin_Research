# Algo-Attack-Model Web App

A React-based interactive simulator for visualizing algorithmic stablecoin de-pegging dynamics (inspired by Terra/LUNA).

## Features
*   **Interactive Simulation**: Start/Stop/Reset the simulation engine.
*   **Attack Trigger**: Simulate a $100M market dump to trigger de-pegging.
*   **Real-time Visualization**: Watch UST price, LUNA price, and Supply dynamics on live charts.
*   **Client-Side Engine**: The entire simulation runs in your browser (`src/engine/StablecoinSystem.ts`).

## Setup

1.  **Install Dependencies**:
    ```bash
    npm install
    ```

2.  **Run Development Server**:
    ```bash
    npm run dev
    ```

3.  **Open Browser**:
    Navigate to the URL shown in the terminal (usually `http://localhost:5173`).

## Simulation Controls
*   **Start**: Begins the simulation loop.
*   **Execute Attack**: Sells 100M UST for USD, creating immediate sell pressure. Watch how the Arbitrage loop attempts (and potentially fails) to restore the peg.
