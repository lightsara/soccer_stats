"use client"    //must be client side because of the use of useeffect and usestate
import React, { useEffect, useState } from "react";

interface ProlificGoalScorer {
    playerId: number;
    playername: string;
    goalcount: number;
}

import myData from './data.json';

const Players: React.FC = () => {

    const [players, setPlayers] = useState<ProlificGoalScorer[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchPlayers = async () => {
            try {
                const data = await getProlificGoalScorer();
                setPlayers(data.filter((player): player is ProlificGoalScorerer => 
                    typeof player.playername === 'number'));
            } catch {
                setError("Failed to fetch prolific goal scorers.");
            }
        };

        console.log(fetchPlayers)
        fetchPlayers();
    }, []);

    if (error) {
        return <div className="text-red-400">{error}</div>;
    }

}

export default Players
