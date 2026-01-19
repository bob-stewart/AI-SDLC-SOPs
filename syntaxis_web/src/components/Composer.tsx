import React, { useState } from 'react';
import { Plus, X } from 'lucide-react';
import useStore, { type BlockType, type EffectVector } from '../store';
import { v4 as uuidv4 } from 'uuid';

const Composer = () => {
    const [isOpen, setIsOpen] = useState(false);
    const addNode = useStore((state) => state.addNode);

    const [title, setTitle] = useState('');
    const [type, setType] = useState<BlockType>('QUESTION');
    const [content, setContent] = useState('');
    const [effects, setEffects] = useState<EffectVector>({
        risk: 0.1,
        fairness: 0.5,
        novelty: 0.5,
        privacy: 0.1,
    });

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const newNodeId = uuidv4();
        const newNode = {
            id: newNodeId,
            type: type === 'AMENDMENT' ? 'amendmentNode' : 'thoughtNode',
            position: { x: Math.random() * 500, y: Math.random() * 500 },
            data: {
                id: newNodeId,
                title,
                type,
                content,
                status: 'DRAFT' as const,
                effects,
                author: 'User',
                timestamp: Date.now(),
            },
        };
        addNode(newNode);
        setIsOpen(false);
        resetForm();
    };

    const resetForm = () => {
        setTitle('');
        setType('QUESTION');
        setContent('');
        setEffects({ risk: 0.1, fairness: 0.5, novelty: 0.5, privacy: 0.1 });
    };

    if (!isOpen) {
        return (
            <button
                onClick={() => setIsOpen(true)}
                className="absolute bottom-8 right-8 bg-primary hover:bg-blue-600 text-white p-4 rounded-full shadow-lg transition-all hover:scale-110 z-50"
            >
                <Plus size={24} />
            </button>
        );
    }

    return (
        <div className="absolute bottom-8 right-8 w-96 glass rounded-xl p-6 shadow-2xl z-50 animate-in slide-in-from-bottom-10 fade-in duration-200">
            <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold text-white">New Thought Block</h3>
                <button onClick={() => setIsOpen(false)} className="text-secondary hover:text-white">
                    <X size={20} />
                </button>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block text-xs font-mono text-secondary mb-1">Type</label>
                    <select
                        value={type}
                        onChange={(e) => setType(e.target.value as BlockType)}
                        className="w-full bg-surface border border-white/10 rounded-md p-2 text-sm text-white focus:ring-2 focus:ring-primary outline-none"
                    >
                        <option value="QUESTION">Question</option>
                        <option value="CLAIM">Claim</option>
                        <option value="EVIDENCE">Evidence</option>
                        <option value="PROTOCOL">Protocol</option>
                        <option value="RISK">Risk</option>
                        <option value="AMENDMENT">Amendment</option>
                    </select>
                </div>

                <div>
                    <label className="block text-xs font-mono text-secondary mb-1">Title</label>
                    <input
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        className="w-full bg-surface border border-white/10 rounded-md p-2 text-sm text-white focus:ring-2 focus:ring-primary outline-none"
                        placeholder="Enter a concise title..."
                        required
                    />
                </div>

                <div>
                    <label className="block text-xs font-mono text-secondary mb-1">Content</label>
                    <textarea
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                        className="w-full bg-surface border border-white/10 rounded-md p-2 text-sm text-white focus:ring-2 focus:ring-primary outline-none h-24 resize-none"
                        placeholder="Describe your thought..."
                    />
                </div>

                <div className="space-y-3 pt-2 border-t border-white/10">
                    <label className="block text-xs font-mono text-secondary">Effect Vector</label>

                    <div className="grid grid-cols-2 gap-4">
                        {Object.entries(effects).map(([key, value]) => (
                            <div key={key}>
                                <div className="flex justify-between text-xs mb-1">
                                    <span className="capitalize text-secondary">{key}</span>
                                    <span className="text-white font-mono">{value.toFixed(1)}</span>
                                </div>
                                <input
                                    type="range"
                                    min="0"
                                    max="1"
                                    step="0.1"
                                    value={value}
                                    onChange={(e) => setEffects({ ...effects, [key]: parseFloat(e.target.value) })}
                                    className="w-full h-1 bg-surface rounded-lg appearance-none cursor-pointer accent-primary"
                                />
                            </div>
                        ))}
                    </div>
                </div>

                <button
                    type="submit"
                    className="w-full bg-primary hover:bg-blue-600 text-white py-2 rounded-md font-medium transition-colors mt-4"
                >
                    Create Block
                </button>
            </form>
        </div>
    );
};

export default Composer;
