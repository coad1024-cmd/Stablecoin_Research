export type MarketDepth = 'deep' | 'moderate' | 'shallow';

export interface SimulationConfig {
    initialUstPrice: number;
    initialLunaPrice: number;
    initialUstSupply: number;
    initialLunaSupply: number;
    ustPoolSizeUsd: number;
    lunaPoolSizeUsd: number;
    marketDepth: MarketDepth;
    attackSize: number;
    shortSize: number;
    leverage: number;
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
    attackerCash: number;
    debtValue: number;
    shortPosition: number;
    shortEntryPrice: number;
    ustLiability: number;
    lunaLiability: number;
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
