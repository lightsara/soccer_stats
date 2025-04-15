//"use client"    //must be client side because of the use of useeffect and usestate
//import React, { useEffect, useState } from "react";
import playerData from '../../data/players.json';
//import React from "react";

// Define a Typescript interface for our JSON data
interface UserData {
  name: string;
  age: number;
}

/
// Use the data with type safety
let user: UserData = userData;
console.log(`Name: ${user.name}, Age: ${user.age}`);