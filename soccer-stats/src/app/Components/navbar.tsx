import React from 'react';

<nav>
<ul style={{ display: 'flex', listStyle: 'none', padding: 0 }}>
  <li style={{ margin: '0 10px' }}>
    <button onClick={() => document.getElementById('barcelona')?.scrollIntoView({ behavior: 'smooth' })}>
      Barcelona
    </button>
  </li>
  <li style={{ margin: '0 10px' }}>
    <button onClick={() => document.getElementById('brazil')?.scrollIntoView({ behavior: 'smooth' })}>
      Brazil
    </button>
  </li>
  <li style={{ margin: '0 10px' }}>
    <button onClick={() => document.getElementById('players')?.scrollIntoView({ behavior: 'smooth' })}>
      Players
    </button>
  </li>
  <li style={{ margin: '0 10px' }}>
    <button onClick={() => document.getElementById('teams')?.scrollIntoView({ behavior: 'smooth' })}>
      Teams
    </button>
  </li>
</ul>
</nav>