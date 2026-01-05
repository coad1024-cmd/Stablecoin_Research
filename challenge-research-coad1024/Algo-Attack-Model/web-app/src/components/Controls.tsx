import React from 'react';
import type { SimulationConfig } from '../engine/types';
import { Play, RotateCcw, Settings2 } from 'lucide-react';

interface ControlsProps {
    config: SimulationConfig;
    setConfig: React.Dispatch<React.SetStateAction<SimulationConfig>>;
    onStart: () => void;
    isRunning: boolean;
    onReset: () => void;
}

// 1. Defined Outside to prevent re-mounting on every render
const InputField = ({ 
    label, 
    name, 
    value, 
    onChange, 
    disabled, 
    type = "number",
    onQuickSet,
    step = 1
}: { 
    label: string, 
    name: keyof SimulationConfig, 
    value: any,
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void,
    disabled: boolean,
    type?: string,
    onQuickSet?: (val: number) => void,
    step?: number
}) => {
    const handleStep = (direction: 1 | -1) => {
        if (disabled) return;
        const currentVal = parseFloat(value) || 0;
        // Smart stepping: if value > 1M, step by 10M. If < 100, step by 1.
        let dynamicStep = step;
        if (currentVal >= 1_000_000) dynamicStep = 10_000_000;
        else if (currentVal >= 1000) dynamicStep = 100;
        
        const newVal = currentVal + (dynamicStep * direction);
        // Create a synthetic event to reuse the onChange handler
        const event = {
            target: { name, value: newVal.toString() }
        } as React.ChangeEvent<HTMLInputElement>;
        onChange(event);
    };

    return (
        <div className="space-y-1">
            <label className="text-xs font-medium text-slate-500 uppercase tracking-wide flex justify-between">
                {label}
                {onQuickSet && (
                    <div className="flex gap-1">
                        <button onClick={() => onQuickSet(100_000_000)} className="text-[10px] bg-slate-800 px-1 rounded hover:bg-slate-700 text-indigo-400">100M</button>
                        <button onClick={() => onQuickSet(500_000_000)} className="text-[10px] bg-slate-800 px-1 rounded hover:bg-slate-700 text-indigo-400">500M</button>
                        <button onClick={() => onQuickSet(1_000_000_000)} className="text-[10px] bg-slate-800 px-1 rounded hover:bg-slate-700 text-indigo-400">1B</button>
                    </div>
                )}
            </label>
            <div className="relative flex items-center">
                <button 
                    onClick={() => handleStep(-1)}
                    disabled={disabled}
                    className="absolute left-0 w-8 h-full bg-slate-800/50 hover:bg-slate-700 text-slate-400 rounded-l-md border-r border-slate-700 flex items-center justify-center transition-colors disabled:opacity-50"
                >
                    -
                </button>
                <input
                    type={type}
                    name={name}
                    value={value}
                    onChange={onChange}
                    disabled={disabled}
                    className="w-full bg-slate-950 border border-slate-700 rounded-md py-2 px-10 text-center text-sm text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-indigo-500 transition-all disabled:opacity-50 disabled:cursor-not-allowed font-mono"
                />
                <button 
                    onClick={() => handleStep(1)}
                    disabled={disabled}
                    className="absolute right-0 w-8 h-full bg-slate-800/50 hover:bg-slate-700 text-slate-400 rounded-r-md border-l border-slate-700 flex items-center justify-center transition-colors disabled:opacity-50"
                >
                    +
                </button>
            </div>
        </div>
    );
};
export const Controls: React.FC<ControlsProps> = ({ config, setConfig, onStart, isRunning, onReset }) => {
    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setConfig(prev => ({
            ...prev,
            [name]: name === 'marketDepth' ? value : parseFloat(value)
        }));
    };

    const handleQuickSet = (name: keyof SimulationConfig) => (val: number) => {
        if (!isRunning) {
            setConfig(prev => ({ ...prev, [name]: val }));
        }
    };

    return (
        <div className="p-5">
            <div className="flex items-center gap-2 mb-6 border-b border-slate-800 pb-4">
                <Settings2 className="w-5 h-5 text-indigo-400" />
                <h2 className="text-lg font-bold text-white">Configuration</h2>
            </div>

            <div className="space-y-6">
                {/* Section 1: Token Specs */}
                <div className="space-y-3">
                    <h3 className="text-sm font-semibold text-slate-300 flex items-center gap-2">
                        <span className="w-1 h-1 bg-indigo-500 rounded-full"></span>
                        Initial Prices
                    </h3>
                    <div className="grid grid-cols-2 gap-4">
                        <InputField label="Stablecoin Price ($)" name="initialUstPrice" value={config.initialUstPrice} onChange={handleChange} disabled={isRunning} />
                        <InputField label="Collateral Price ($)" name="initialLunaPrice" value={config.initialLunaPrice} onChange={handleChange} disabled={isRunning} />
                    </div>
                </div>

                {/* Section 2: Supply & Pools */}
                <div className="space-y-3">
                    <h3 className="text-sm font-semibold text-slate-300 flex items-center gap-2">
                        <span className="w-1 h-1 bg-emerald-500 rounded-full"></span>
                        Liquidity & Supply
                    </h3>
                    <div className="grid grid-cols-2 gap-4">
                        <InputField label="Stablecoin Pool ($)" name="ustPoolSizeUsd" value={config.ustPoolSizeUsd} onChange={handleChange} disabled={isRunning} onQuickSet={handleQuickSet('ustPoolSizeUsd')} />
                        <InputField label="Collateral Pool ($)" name="lunaPoolSizeUsd" value={config.lunaPoolSizeUsd} onChange={handleChange} disabled={isRunning} onQuickSet={handleQuickSet('lunaPoolSizeUsd')} />
                    </div>
                    <div className="grid grid-cols-2 gap-4">
                         <InputField label="Stablecoin Supply" name="initialUstSupply" value={config.initialUstSupply} onChange={handleChange} disabled={isRunning} />
                         <InputField label="Collateral Supply" name="initialLunaSupply" value={config.initialLunaSupply} onChange={handleChange} disabled={isRunning} />
                    </div>
                </div>

                {/* Section 3: Environment */}
                <div className="space-y-3">
                     <h3 className="text-sm font-semibold text-slate-300 flex items-center gap-2">
                        <span className="w-1 h-1 bg-amber-500 rounded-full"></span>
                        Market Environment
                    </h3>
                    <div>
                        <label className="text-xs font-medium text-slate-500 uppercase tracking-wide">Market Depth</label>
                        <select
                            name="marketDepth"
                            value={config.marketDepth}
                            onChange={handleChange}
                            disabled={isRunning}
                            className="w-full mt-1 bg-slate-950 border border-slate-700 rounded-md px-3 py-2 text-sm text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-indigo-500 disabled:opacity-50"
                        >
                            <option value="moderate">Moderate</option>
                            <option value="shallow">Shallow (Volatile)</option>
                            <option value="deep">Deep (Stable)</option>
                        </select>
                    </div>
                </div>

                {/* Section 4: Attack Strategy */}
                <div className="space-y-3">
                    <h3 className="text-sm font-semibold text-rose-400 flex items-center gap-2">
                        <span className="w-1 h-1 bg-rose-500 rounded-full"></span>
                        Attack Strategy
                    </h3>
                    <div className="grid grid-cols-2 gap-4">
                        <InputField label="Attack Size (Stablecoin)" name="attackSize" value={config.attackSize} onChange={handleChange} disabled={isRunning} onQuickSet={handleQuickSet('attackSize')} />
                        <InputField label="Short Size ($ USD)" name="shortSize" value={config.shortSize} onChange={handleChange} disabled={isRunning} onQuickSet={handleQuickSet('shortSize')} />
                    </div>                    <div>
                        <div className="flex justify-between items-center mb-1">
                            <label className="text-xs font-medium text-slate-500 uppercase tracking-wide">Leverage Multiplier</label>
                            <span className="text-xs font-bold text-rose-400">{config.leverage}x</span>
                        </div>
                        <input
                            type="range"
                            name="leverage"
                            min="1"
                            max="3"
                            step="0.1"
                            value={config.leverage}
                            onChange={handleChange}
                            disabled={isRunning}
                            className="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-rose-500"
                        />
                    </div>
                </div>

                {/* Action Buttons */}
                <div className="pt-4 flex gap-3">
                    {isRunning ? (
                         <button
                            onClick={onStart}
                            className="flex-1 flex items-center justify-center gap-2 py-2.5 rounded-lg font-semibold bg-amber-600 hover:bg-amber-500 text-white shadow-lg transition-all"
                         >
                            <span className="animate-pulse">Running... (Click to Pause)</span>
                         </button>
                    ) : (
                        <button
                            onClick={onStart}
                            className="flex-1 flex items-center justify-center gap-2 py-2.5 rounded-lg font-semibold bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-500/20 active:translate-y-0.5 transition-all"
                        >
                            <Play className="w-4 h-4 fill-current" /> {config ? 'Resume Sim' : 'Start Sim'}
                        </button>
                    )}
                    
                    <button
                        onClick={onReset}
                        className="px-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg font-medium transition-colors border border-slate-700 flex items-center justify-center"
                        title="Reset Simulation"
                    >
                        <RotateCcw className="w-4 h-4" />
                    </button>
                </div>
            </div>
        </div>
    );
};
