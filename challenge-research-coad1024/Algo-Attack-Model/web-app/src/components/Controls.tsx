import React from 'react';
import { SimulationConfig } from '../engine/types';

interface ControlsProps {
    config: SimulationConfig;
    setConfig: React.Dispatch<React.SetStateAction<SimulationConfig>>;
    onStart: () => void;
    isRunning: boolean;
    onReset: () => void;
}

export const Controls: React.FC<ControlsProps> = ({ config, setConfig, onStart, isRunning, onReset }) => {
    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setConfig(prev => ({
            ...prev,
            [name]: name === 'marketDepth' ? value : parseFloat(value)
        }));
    };

    return (
        <div className="bg-white p-6 rounded-2xl shadow-lg space-y-8">
            <div>
                <h2 className="text-2xl font-bold border-b pb-2 mb-4">1. Initial Conditions</h2>
                <div className="space-y-4">
                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700">UST Price</label>
                            <input type="number" name="initialUstPrice" value={config.initialUstPrice} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm border p-2" />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">LUNA Price</label>
                            <input type="number" name="initialLunaPrice" value={config.initialLunaPrice} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm border p-2" />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">UST Supply</label>
                            <input type="number" name="initialUstSupply" value={config.initialUstSupply} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm border p-2" />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">LUNA Supply</label>
                            <input type="number" name="initialLunaSupply" value={config.initialLunaSupply} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm border p-2" />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">UST Pool (USD)</label>
                            <input type="number" name="ustPoolSizeUsd" value={config.ustPoolSizeUsd} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm border p-2" />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">LUNA Pool (USD)</label>
                            <input type="number" name="lunaPoolSizeUsd" value={config.lunaPoolSizeUsd} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm border p-2" />
                        </div>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Market Depth</label>
                        <select name="marketDepth" value={config.marketDepth} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm border p-2">
                            <option value="moderate">Moderate</option>
                            <option value="shallow">Shallow</option>
                            <option value="deep">Deep</option>
                        </select>
                    </div>
                    <div className="flex space-x-2">
                        <button onClick={onStart} disabled={isRunning} className={`w-full text-white font-semibold py-2 px-4 rounded-lg transition ${isRunning ? 'bg-gray-400' : 'bg-indigo-600 hover:bg-indigo-700'}`}>
                            {isRunning ? 'Running...' : 'Start Simulation'}
                        </button>
                        <button onClick={onReset} className="bg-gray-500 text-white font-semibold py-2 px-4 rounded-lg hover:bg-gray-600 transition">
                            Reset
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};
