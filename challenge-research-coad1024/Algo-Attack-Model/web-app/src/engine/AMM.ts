import { AMMPoolState } from './types';

export class AMM {
    static createPool(tokenPrice: number, liquidityUsd: number): AMMPoolState {
        const usdReserve = liquidityUsd / 2;
        const tokenReserve = usdReserve / tokenPrice;
        return {
            tokenReserve,
            usdReserve,
            k: tokenReserve * usdReserve,
        };
    }

    static getAmountOut(amountIn: number, reserveIn: number, reserveOut: number): number {
        const amountInWithFee = amountIn * 0.997; // 0.3% fee
        const numerator = amountInWithFee * reserveOut;
        const denominator = reserveIn + amountInWithFee;
        return numerator / denominator;
    }

    static swapTokenForUsd(pool: AMMPoolState, tokenAmountIn: number): { usdOut: number; newPool: AMMPoolState } {
        const usdOut = this.getAmountOut(tokenAmountIn, pool.tokenReserve, pool.usdReserve);
        return {
            usdOut,
            newPool: {
                ...pool,
                tokenReserve: pool.tokenReserve + tokenAmountIn,
                usdReserve: pool.usdReserve - usdOut,
                k: pool.k // k slightly increases due to fees
            }
        };
    }

    static swapUsdForToken(pool: AMMPoolState, usdAmountIn: number): { tokenOut: number; newPool: AMMPoolState } {
        const tokenOut = this.getAmountOut(usdAmountIn, pool.usdReserve, pool.tokenReserve);
        return {
            tokenOut,
            newPool: {
                ...pool,
                usdReserve: pool.usdReserve + usdAmountIn,
                tokenReserve: pool.tokenReserve - tokenOut,
                k: pool.k
            }
        };
    }

    static getPrice(pool: AMMPoolState): number {
        return pool.usdReserve / pool.tokenReserve;
    }
}
