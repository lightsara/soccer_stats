import React from 'react';
import Link from 'next/link';
import { Separator } from "./separator"

const Navbar: React.FC = () => {
  return (
    <nav className="flex justify-between bg-green-600 text-yellow-500 p-4 theme-secondary-colored theme-children-inherit">
      <ul className="flex items-center space-x-4">
        <li>
          <Link href="/" className="hover:underline">Players</Link>
        </li>
        <Separator orientation="vertical" />
        <li>
          <Link href="/teams" className="hover:underline">Teams</Link>
        </li>
        <Separator orientation="vertical" />
        <li>
          <Link href="/leagues" className="hover:underline">Leagues</Link>
        </li>
        <Separator orientation="vertical" />
        <li>
          <Link href="/extras" className="hover:underline">Extra special features</Link>
        </li>
      </ul>
      </nav>
  );
};

export default Navbar;