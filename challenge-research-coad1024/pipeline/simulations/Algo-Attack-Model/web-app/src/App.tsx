import { useState, useEffect, useRef } from 'react';
import { StablecoinSystem } from './engine/StablecoinSystem';
import type { SimulationConfig, SimulationLogEntry } from './engine/types';
import { Controls } from './components/Controls';
import { Charts } from './components/Charts';
import { Activity, ShieldAlert, Play, RotateCcw, TrendingDown } from 'lucide-react';

const INITIAL_CONFIG: SimulationConfig = {
  initialUstPrice: 1.00,
  initialLunaPrice: 80.00,
  initialUstSupply: 18_700_000_000,
  initialLunaSupply: 350_000_000,
  ustPoolSizeUsd: 1_200_000_000, // Curve 3Pool Reality
  lunaPoolSizeUsd: 70_000_000,   // Virtual BasePool Reality
  marketDepth: 'moderate',       // Use raw values (moderate = 1.0 multiplier)
  attackSize: 500_000_000,
  shortSize: 160_000_000 
};

function App() {
  const [config, setConfig] = useState<SimulationConfig>(INITIAL_CONFIG);
  const [isRunning, setIsRunning] = useState(false);
  const [data, setData] = useState<SimulationLogEntry[]>([]);
  const systemRef = useRef<StablecoinSystem | null>(null);
  const intervalRef = useRef<number | null>(null);

  const toggleSimulation = () => {
    if (isRunning) {
        stopSimulation();
    } else {
        if (!systemRef.current) {
          systemRef.current = new StablecoinSystem(config);
          setData([systemRef.current.step()]);
        }
        setIsRunning(true);
    }
  };

  const stopSimulation = () => {
    setIsRunning(false);
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
  };

  const resetSimulation = () => {
    stopSimulation();
    systemRef.current = null;
    setData([]);
  };

  const executeAttack = () => {
    if (!systemRef.current) return;
    
    // 1. Open Short Position (Front-run the crash)
    if (config.shortSize > 0) {
        systemRef.current.openShort(config.shortSize);
    }
    
    // 2. Execute the Dump
    systemRef.current.executeAttack(config.attackSize);
    
    setData(prev => [...prev, { ...systemRef.current!.getState(), action: 'Attack' }]);
  };

  // useEffect(() => {
  //   // If config changes while a system exists, we must reset to apply new config
  //   if (systemRef.current) {
  //       resetSimulation();
  //   }
  // }, [config]);

  useEffect(() => {
    if (isRunning) {
      intervalRef.current = window.setInterval(() => {
        if (systemRef.current) {
          const newState = systemRef.current.step();
          setData(prev => {
            const newData = [...prev, newState];
            if (newData.length > 500) return newData.slice(-500);
            return newData;
          });
        }
      }, 100);
    } else {
      if (intervalRef.current) clearInterval(intervalRef.current);
    }
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
    };
  }, [isRunning]);

  const currentStatus = data.length > 0 ? data[data.length - 1].pegStatus : 'Stable';
  const getStatusColor = (status: string) => {
      switch(status) {
          case 'Stable': return 'text-emerald-400 bg-emerald-400/10 border-emerald-400/20';
          case 'De-pegged': return 'text-amber-400 bg-amber-400/10 border-amber-400/20';
          case 'Collapsed': return 'text-rose-500 bg-rose-500/10 border-rose-500/20';
          default: return 'text-slate-400';
      }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 font-sans selection:bg-indigo-500/30">
      
      {/* Navbar */}
      <nav className="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
        <div className="container mx-auto px-6 h-16 flex items-center justify-between">
            <div className="flex items-center gap-3">
                <div className="bg-indigo-500/20 p-2 rounded-lg">
                    <Activity className="w-6 h-6 text-indigo-400" />
                </div>
                <h1 className="text-xl font-bold tracking-tight text-white">
                    Algo<span className="text-indigo-400">Sim</span>
                </h1>
            </div>
            <div className="text-sm text-slate-500 hidden sm:block">
                Research Challenge / Attack Model
            </div>
        </div>
      </nav>

      <div className="container mx-auto p-4 md:p-6 lg:p-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          
          {/* LEFT COLUMN: Controls & Metrics */}
          <div className="lg:col-span-4 space-y-6">
            
            {/* Status Card */}
            <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl relative overflow-hidden">
                <div className="absolute top-0 right-0 p-4 opacity-10">
                    <ShieldAlert className="w-24 h-24" />
                </div>
                <h2 className="text-slate-400 text-sm font-semibold uppercase tracking-wider mb-2">System Status</h2>
                <div className={`inline-flex items-center gap-2 px-4 py-2 rounded-full border ${getStatusColor(currentStatus)} font-bold text-lg`}>
                    <div className={`w-2 h-2 rounded-full ${currentStatus === 'Stable' ? 'bg-emerald-400' : 'bg-rose-500'} animate-pulse`}></div>
                    {currentStatus}
                </div>

                <div className="mt-6 grid grid-cols-2 gap-4">
                     <div className="bg-slate-950/50 p-3 rounded-lg border border-slate-800/50">
                        <div className="text-slate-500 text-xs">Attacker Cash</div>
                        <div className="text-xl font-mono font-medium text-emerald-400">
                            {data.length > 0 ? `$${(data[data.length - 1].attackerCash / 1e6).toFixed(1)}M` : '$0.0M'}
                        </div>
                     </div>
                     <div className="bg-slate-950/50 p-3 rounded-lg border border-slate-800/50">
                        <div className="text-slate-500 text-xs">Current Debt</div>
                        <div className="text-xl font-mono font-medium text-rose-400">
                            {data.length > 0 ? `$${(data[data.length - 1].debtValue / 1e6).toFixed(1)}M` : '$0.0M'}
                        </div>
                     </div>
                </div>

                <div className="mt-4 grid grid-cols-2 gap-4">
                     <div className="bg-slate-950/50 p-3 rounded-lg border border-slate-800/50">
                        <div className="text-slate-500 text-xs">Net PnL</div>
                        <div className={`text-xl font-mono font-medium ${data.length > 0 && data[data.length-1].attackerPnl > 0 ? 'text-emerald-400' : 'text-slate-300'}`}>
                            {data.length > 0 ? `$${(data[data.length - 1].attackerPnl / 1e6).toFixed(1)}M` : '$0.0M'}
                        </div>
                     </div>
                     <div className="bg-slate-950/50 p-3 rounded-lg border border-slate-800/50">
                        <div className="text-slate-500 text-xs">Current Step</div>
                        <div className="text-xl font-mono font-medium text-slate-300">
                            {data.length > 0 ? data[data.length - 1].step : '0'}
                        </div>
                     </div>
                </div>

                {/* Technical Debug Section */}
                <div className="mt-6 bg-slate-950/30 border border-slate-800 p-4 rounded-xl">
                    <h3 className="text-slate-500 text-[10px] font-bold uppercase tracking-[0.2em] mb-3">Technical Debug</h3>
                    {data.length > 0 ? (
                        <div className="space-y-3 font-mono text-[10px]">
                            <div className="flex justify-between border-b border-slate-800 pb-1">
                                <span className="text-slate-600">UST POOL USD:</span>
                                <span className="text-slate-400">${(data[data.length-1].ustPool.usdReserve/1e6).toFixed(1)}M</span>
                            </div>
                            <div className="flex justify-between border-b border-slate-800 pb-1">
                                <span className="text-slate-600">UST POOL TOK:</span>
                                <span className="text-slate-400">{(data[data.length-1].ustPool.tokenReserve/1e6).toFixed(1)}M</span>
                            </div>
                            <div className="flex justify-between border-b border-slate-800 pb-1">
                                <span className="text-slate-600">UST PRICE:</span>
                                <span className="text-indigo-400">${data[data.length-1].ustPrice.toFixed(4)}</span>
                            </div>
                            <div className="flex justify-between border-b border-slate-800 pb-1">
                                <span className="text-slate-600">LUNA PRICE:</span>
                                <span className="text-pink-400">${data[data.length-1].lunaPrice.toFixed(4)}</span>
                            </div>
                        </div>
                    ) : <p className="text-slate-700 italic text-[10px]">No data</p>}
                </div>
            </div>

            {/* Config & Controls */}
            <div className="bg-slate-900 border border-slate-800 rounded-xl p-1 shadow-xl">
                 <Controls
                    config={config}
                    setConfig={setConfig}
                    onStart={toggleSimulation}
                    isRunning={isRunning}
                    onReset={resetSimulation}
                />
            </div>

            {/* Attack Module */}
            <div className="bg-slate-900 border border-rose-900/30 rounded-xl p-6 shadow-xl relative overflow-hidden group">
                <div className="absolute inset-0 bg-gradient-to-br from-rose-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <h2 className="text-rose-400 text-lg font-bold flex items-center gap-2 mb-4">
                    <TrendingDown className="w-5 h-5" />
                    Attack Vector
                </h2>
                <p className="text-slate-400 text-sm mb-6 leading-relaxed">
                    Strategy: Dump <span className="text-rose-300 font-semibold">${(config.attackSize * config.leverage / 1e6).toLocaleString()}M Stablecoin</span> and Short <span className="text-rose-300 font-semibold">${(config.shortSize * config.leverage / 1e6).toLocaleString()}M Collateral</span> (~{(config.initialLunaPrice > 0 ? ((config.shortSize * config.leverage) / config.initialLunaPrice / 1e6) : 0).toFixed(1)}M Tokens).
                </p>
                <button
                    onClick={executeAttack}
                    disabled={!isRunning}
                    className={`w-full py-4 px-4 rounded-lg font-bold text-white transition-all transform flex items-center justify-center gap-2
                        ${!isRunning 
                            ? 'bg-slate-800 text-slate-600 cursor-not-allowed' 
                            : 'bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 shadow-lg shadow-rose-900/20 hover:shadow-rose-900/40 active:scale-[0.98]'
                        }`}
                >
                    <ShieldAlert className="w-5 h-5" />
                    EXECUTE STRATEGY
                </button>
            </div>
          </div>

          {/* RIGHT COLUMN: Visualizations */}
          <div className="lg:col-span-8 space-y-6">
            <Charts data={data} />
          </div>

        </div>
      </div>
    </div>
  );
}

export default App;