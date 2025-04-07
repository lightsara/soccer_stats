import { Suspense } from "react";

export default function Home() {
  return (
    <Suspense fallback={<p className="text-gray-300 text-center">Loading...</p>}>
      <div>Soccer</div>
    </Suspense>
  );
}