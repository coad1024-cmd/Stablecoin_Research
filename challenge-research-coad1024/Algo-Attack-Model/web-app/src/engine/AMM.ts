import type { AMMPoolState } from './types';

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
        const aIn = Number(amountIn);
        const rIn = Number(reserveIn);
        const rOut = Number(reserveOut);
        
        const amountInWithFee = aIn * 0.997; 
        const numerator = amountInWithFee * rOut;
        const denominator = rIn + amountInWithFee;
        
        if (denominator === 0) return 0;
        const out = numerator / denominator;
        
        // Safety: Never drain more than 99.9% of liquidity in one swap
        return out >= rOut ? rOut * 0.999 : out;
    }

    static swapTokenForUsd(pool: AMMPoolState, tokenAmountIn: number): { usdOut: number; newPool: AMMPoolState } {
        const tIn = Number(tokenAmountIn);
        const usdOut = this.getAmountOut(tIn, pool.tokenReserve, pool.usdReserve);
        return {
            usdOut,
            newPool: {
                ...pool,
                tokenReserve: Number(pool.tokenReserve) + tIn,
                usdReserve: Number(pool.usdReserve) - usdOut,
                k: pool.k 
            }
        };
    }

    static swapUsdForToken(pool: AMMPoolState, usdAmountIn: number): { tokenOut: number; newPool: AMMPoolState } {
        const uIn = Number(usdAmountIn);
        const tokenOut = this.getAmountOut(uIn, pool.usdReserve, pool.tokenReserve);
        return {
            tokenOut,
            newPool: {
                ...pool,
                usdReserve: Number(pool.usdReserve) + uIn,
                tokenReserve: Number(pool.tokenReserve) - tokenOut,
                k: pool.k
            }
        };
    }

    static getPrice(pool: AMMPoolState): number {
        return pool.usdReserve / pool.tokenReserve;
    }
}
