import React from 'react';
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer,
    ReferenceLine
} from 'recharts';
import type { SimulationLogEntry } from '../engine/types';

interface ChartsProps {
    data: SimulationLogEntry[];
}

const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
        return (
            <div className="bg-slate-900 border border-slate-700 p-3 rounded-lg shadow-xl text-xs">
                <p className="text-slate-400 mb-2">Step: {label}</p>
                {payload.map((entry: any, index: number) => (
                    <div key={index} className="flex items-center gap-2 mb-1" style={{ color: entry.color }}>
                        <span className="font-semibold">{entry.name}:</span>
                        <span className="font-mono">
                            {entry.value.toLocaleString(undefined, { 
                                minimumFractionDigits: entry.name.includes('Supply') ? 0 : 2, 
                                maximumFractionDigits: entry.name.includes('Supply') ? 0 : 4 
                            })}
                        </span>
                    </div>
                ))}
            </div>
        );
    }
    return null;
};

export const Charts: React.FC<ChartsProps> = ({ data }) => {
    const attackStep = data.find(d => d.action === 'Attack')?.step;

    return (
        <div className="space-y-8">
            
            {/* 1. Collateral Collapse Subplots */}
            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl shadow-lg flex flex-col space-y-4">
                <h2 className="text-slate-200 font-bold text-lg border-b border-slate-800 pb-2">Collateral Token Dynamics</h2>
                
                <div className="h-48 flex flex-col">
                    <h3 className="text-xs font-semibold text-orange-400 uppercase mb-1">Collateral Price (USD)</h3>
                    <div className="flex-1 min-h-0">
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                                <XAxis dataKey="step" hide />
                                <YAxis stroke="#94a3b8" fontSize={10} tickFormatter={(v) => `$${v}`} />
                                <Tooltip content={<CustomTooltip />} />
                                {attackStep && <ReferenceLine x={attackStep} stroke="#ef4444" strokeDasharray="5 5" />}
                                <Line type="monotone" dataKey="lunaPrice" stroke="#f97316" strokeWidth={2} name="Collateral Price" dot={false} isAnimationActive={false} />
                            </LineChart>
                        </ResponsiveContainer>
                    </div>
                </div>

                <div className="h-48 flex flex-col border-t border-slate-800 pt-4">
                    <h3 className="text-xs font-semibold text-amber-700 uppercase mb-1">Collateral Supply (Tokens)</h3>
                    <div className="flex-1 min-h-0">
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                                <XAxis dataKey="step" fontSize={10} stroke="#475569" />
                                <YAxis stroke="#94a3b8" fontSize={10} tickFormatter={(v) => v.toExponential(1)} domain={['dataMin', 'auto']} />
                                <Tooltip content={<CustomTooltip />} />
                                {attackStep && <ReferenceLine x={attackStep} stroke="#ef4444" strokeDasharray="5 5" />}
                                <Line type="monotone" dataKey="lunaSupply" stroke="#92400e" strokeWidth={2} name="Collateral Supply" dot={false} isAnimationActive={false} />
                            </LineChart>
                        </ResponsiveContainer>
                    </div>
                </div>
            </div>

            {/* 2. Stablecoin Price De-peg */}
            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl shadow-lg h-64 flex flex-col">
                <h2 className="text-slate-200 font-bold text-lg border-b border-slate-800 pb-2 mb-4">Algorithmic Stablecoin Peg Stability</h2>
                <div className="flex-1 min-h-0">
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                            <XAxis dataKey="step" fontSize={10} stroke="#475569" />
                            <YAxis domain={[0, 1.2]} stroke="#94a3b8" fontSize={10} tickFormatter={(v) => `$${v.toFixed(2)}`} />
                            <Tooltip content={<CustomTooltip />} />
                            <ReferenceLine y={1} stroke="#10b981" strokeDasharray="3 3" opacity={0.3} />
                            {attackStep && <ReferenceLine x={attackStep} stroke="#ef4444" strokeDasharray="5 5" />}
                            <Line type="monotone" dataKey="ustPrice" stroke="#2563eb" strokeWidth={2.5} name="Stablecoin Price" dot={false} isAnimationActive={false} />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>

            {/* 3. Dual-Axis Supply Inflation */}
            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl shadow-lg h-80 flex flex-col">
                <h2 className="text-slate-200 font-bold text-lg border-b border-slate-800 pb-2 mb-4">Total Supply Dynamics (Dual Axis)</h2>
                <div className="flex-1 min-h-0">
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                            <XAxis dataKey="step" fontSize={10} stroke="#475569" />
                            
                            {/* Left Y-Axis for Stablecoin (Billions) */}
                            <YAxis yAxisId="left" stroke="#38bdf8" fontSize={10} tickFormatter={(v) => `${(v/1e9).toFixed(1)}B`} />
                            
                            {/* Right Y-Axis for Collateral (Millions/Billions) */}
                            <YAxis yAxisId="right" orientation="right" stroke="#f472b6" fontSize={10} tickFormatter={(v) => v > 1e9 ? `${(v/1e9).toFixed(1)}B` : `${(v/1e6).toFixed(0)}M`} />
                            
                            <Tooltip content={<CustomTooltip />} />
                            <Legend />
                            
                            <Line yAxisId="left" type="monotone" dataKey="ustSupply" stroke="#38bdf8" strokeWidth={2} name="Stablecoin Supply (Left)" dot={false} isAnimationActive={false} />
                            <Line yAxisId="right" type="monotone" dataKey="lunaSupply" stroke="#f472b6" strokeWidth={2} name="Collateral Supply (Right)" dot={false} isAnimationActive={false} />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>

            {/* 4. Attacker Portfolio History */}
            <div className="bg-slate-900 border border-slate-800 p-5 rounded-xl shadow-lg h-64 flex flex-col">
                <h2 className="text-slate-200 font-bold text-lg border-b border-slate-800 pb-2 mb-4">Attacker Portfolio History</h2>
                <div className="flex-1 min-h-0">
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                            <XAxis dataKey="step" fontSize={10} stroke="#475569" />
                            <YAxis stroke="#94a3b8" fontSize={10} tickFormatter={(v) => `$${(v/1e6).toFixed(0)}M`} />
                            <Tooltip content={<CustomTooltip />} />
                            {attackStep && <ReferenceLine x={attackStep} stroke="#ef4444" strokeDasharray="5 5" />}
                            <Line type="monotone" dataKey="attackerPnl" stroke="#16a34a" strokeWidth={2.5} name="Portfolio Value" dot={false} isAnimationActive={false} />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>

        </div>
    );
};