import { useState, useEffect, useRef } from 'react';
import { StablecoinSystem } from './engine/StablecoinSystem';
import { SimulationConfig, SimulationLogEntry } from './engine/types';
import { Controls } from './components/Controls';
import { Charts } from './components/Charts';
import { Play, RotateCcw, Activity } from 'lucide-react';

const INITIAL_CONFIG: SimulationConfig = {
  initialUstPrice: 1.00,
  initialLunaPrice: 50.00,
  initialUstSupply: 2_000_000_000,
  initialLunaSupply: 100_000_000,
  ustPoolSizeUsd: 500_000_000,
  lunaPoolSizeUsd: 500_000_000,
  marketDepth: 'moderate'
};

function App() {
  const [config, setConfig] = useState<SimulationConfig>(INITIAL_CONFIG);
  const [isRunning, setIsRunning] = useState(false);
  const [data, setData] = useState<SimulationLogEntry[]>([]);
  const systemRef = useRef<StablecoinSystem | null>(null);
  const intervalRef = useRef<number | null>(null);

  const startSimulation = () => {
    if (isRunning) return;

    // Initialize system if first run or after reset
    if (!systemRef.current) {
      systemRef.current = new StablecoinSystem(config);
      setData([systemRef.current.step()]); // Initial state
    }

    setIsRunning(true);
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
    // Attack size: 100M UST (hardcoded for demo, could be from config)
    systemRef.current.executeAttack(100_000_000);
    // Force update
    setData(prev => [...prev, { ...systemRef.current!.getState(), action: 'Attack' }]);
  };

  useEffect(() => {
    if (isRunning) {
      intervalRef.current = window.setInterval(() => {
        if (systemRef.current) {
          const newState = systemRef.current.step();
          setData(prev => {
            const newData = [...prev, newState];
            // Limit history for performance if needed
            if (newData.length > 500) return newData.slice(-500);
            return newData;
          });
        }
      }, 100); // 100ms step
    } else {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    }
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
    };
  }, [isRunning]);

  return (
    <div className="min-h-screen bg-gray-100 text-gray-800 font-sans">
      <div className="container mx-auto p-4 md:p-8">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 flex items-center justify-center gap-2">
            <Activity className="w-10 h-10 text-indigo-600" />
            Algorithmic Stablecoin Simulator
          </h1>
          <p className="text-lg text-gray-600 mt-2">Model and visualize Terra/LUNA-style de-pegging dynamics.</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left Column: Controls */}
          <div className="lg:col-span-1 space-y-6">
            <Controls
              config={config}
              setConfig={setConfig}
              onStart={startSimulation}
              isRunning={isRunning}
              onReset={resetSimulation}
            />

            {/* Attack Controls */}
            <div className="bg-white p-6 rounded-2xl shadow-lg">
              <h2 className="text-2xl font-bold border-b pb-2 mb-4 text-red-600">⚠ Launch Attack</h2>
              <p className="text-sm text-gray-600 mb-4">Simulate a $100M dump of UST on the open market.</p>
              <button
                onClick={executeAttack}
                disabled={!isRunning}
                className={`w-full text-white font-semibold py-3 px-4 rounded-lg transition ${!isRunning ? 'bg-gray-400' : 'bg-red-600 hover:bg-red-700 shadow-md transform hover:scale-105'}`}
              >
                Execute Attack ($100M Sell)
              </button>
            </div>

            <div className="bg-white p-6 rounded-2xl shadow-lg">
              <h2 className="text-2xl font-bold border-b pb-2 mb-4">Metrics</h2>
              {data.length > 0 ? (
                <div className="space-y-2">
                  <div className="flex justify-between">
                    <span>Peg Status:</span>
                    <span className={`font-bold ${data[data.length - 1].pegStatus === 'Stable' ? 'text-green-600' : 'text-red-600'}`}>{data[data.length - 1].pegStatus}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Attacker PnL:</span>
                    <span className="font-mono">${data[data.length - 1].attackerPnl.toLocaleString(undefined, { maximumFractionDigits: 0 })}</span>
                  </div>
                </div>
              ) : <p className="text-gray-400 italic">Start simulation to see metrics.</p>}
            </div>
          </div>

          {/* Right Column: Charts */}
          <div className="lg:col-span-2 bg-white p-6 rounded-2xl shadow-lg">
            <Charts data={data} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
