import { Suspense } from "react";
import * as playerData from '../data/players_cleaned_0414.json';

interface Player {
  player_id: number;
  name: string;
}
console.log('Player data type:', typeof playerData);
console.log('Keys available:', Object.keys(playerData));  
export default function Home() {
  // Cast the imported data to Player[] type
  // Debug the structure
  //console.log('Player data type:', typeof playerData);
  //console.log('Is array:', Array.isArray(playerData));
  //console.log('Structure:', JSON.stringify(playerData).substring(0, 100) + '...');
  
  // Access the data correctly
  //const players = Array.isArray(playerData) 
  //  ? playerData 
  //  : playerData.default;
    
  //for key in Object.keys(playerData):
  //  console.log('Key:', key); 
  //  console.log('Value:', playerData[key]);

  // Option 1: Using for...of loop (recommended)
  for (const key of Object.keys(playerData)) {
      console.log('Key:', key);
      console.log('Value:', playerData[key as keyof typeof playerData]);
      break;
    } 

  const counter = 0;
  return (
        <div className="container mx-auto p-4">
          <h1 className="text-2xl font-bold mb-6">Soccer Players</h1>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
               {/* Map over player data properly */}
          {Object.entries(playerData).map(([name, info], index) => (
      
            <div key={index} className="border rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow">
              console.log(index)
              <h2 className="text-lg font-semibold">{name}</h2>
              {/* Access player info if needed */}
              <p>Appearances: {typeof info === 'object' && 'appearances' in info ? info.appearances : 'N/A'}</p>
            </div>
))}
          </div>
      </div>
  );
}
