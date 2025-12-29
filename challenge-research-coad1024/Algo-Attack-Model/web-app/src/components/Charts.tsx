import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { SimulationLogEntry } from '../engine/types';

interface ChartsProps {
    data: SimulationLogEntry[];
}

export const Charts: React.FC<ChartsProps> = ({ data }) => {
    return (
        <div className="space-y-6">
            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
                <div className="bg-gray-50 p-4 rounded-lg h-80">
                    <h3 className="text-lg font-semibold text-center mb-2">UST Price Peg</h3>
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data}>
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="step" />
                            <YAxis domain={[0.5, 1.2]} />
                            <Tooltip />
                            <Legend />
                            <Line type="monotone" dataKey="ustPrice" stroke="#8884d8" name="UST Price" dot={false} />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
                <div className="bg-gray-50 p-4 rounded-lg h-80">
                    <h3 className="text-lg font-semibold text-center mb-2">LUNA Price</h3>
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data}>
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="step" />
                            <YAxis />
                            <Tooltip />
                            <Legend />
                            <Line type="monotone" dataKey="lunaPrice" stroke="#82ca9d" name="LUNA Price" dot={false} />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg h-80">
                <h3 className="text-lg font-semibold text-center mb-2">Supply (Log Scale)</h3>
                <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={data}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="step" />
                        <YAxis scale="log" domain={['auto', 'auto']} />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="ustSupply" stroke="#8884d8" name="UST Supply" dot={false} />
                        <Line type="monotone" dataKey="lunaSupply" stroke="#82ca9d" name="LUNA Supply" dot={false} />
                    </LineChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
};
