export type MarketDepth = 'deep' | 'moderate' | 'shallow';

export interface SimulationConfig {
    initialUstPrice: number;
    initialLunaPrice: number;
    initialUstSupply: number;
    initialLunaSupply: number;
    ustPoolSizeUsd: number;
    lunaPoolSizeUsd: number;
    marketDepth: MarketDepth;
}

export interface SystemState {
    step: number;
    ustPrice: number;
    lunaPrice: number;
    ustSupply: number;
    lunaSupply: number;
    ustPool: AMMPoolState;
    lunaPool: AMMPoolState;
    attackerPnl: number;
    pegStatus: 'Stable' | 'De-pegged' | 'Collapsed';
}

export interface AMMPoolState {
    tokenReserve: number;
    usdReserve: number;
    k: number;
}

export interface SimulationLogEntry extends SystemState {
    action: string;
}
