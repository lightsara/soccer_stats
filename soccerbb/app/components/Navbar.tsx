import React from 'react';
import Link from 'next/link';
import { Separator } from "./separator"

const Navbar: React.FC = () => {
  return (
    <nav className="flex bg-green-700 text-yellow-500 p-6 theme-secondary-colored theme-children-inherit">
      <ul className="mx-auto flex items-center space-x-20">
        <li>
          <Link href="/" className="text-2xl font-semibold hover:underline">Players</Link>
        </li>
        <Separator orientation="vertical" />
        <li>
          <Link href="/teams" className="text-2xl font-semibold 2hover:underline">Clubs</Link>
        </li>
        <Separator orientation="vertical" />
        <li>
          <Link href="/leagues" className="text-2xl font-semibold hover:underline">Competitions</Link>
        </li>
        <Separator orientation="vertical" />
        <li>
          <Link href="/extras" className="text-2xl font-semibold hover:underline"> Player by Country </Link>
        </li>
      </ul>
      </nav>
  );
};

export default Navbar;