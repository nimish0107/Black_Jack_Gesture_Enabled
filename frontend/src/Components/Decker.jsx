import React, { useState, useEffect } from "react";
import Card from "./Card";
import axios from "axios";

const Decker = () => {
  const [playerArray, setPlayerCards] = useState([]); // Initialize with an empty array

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/deck")
      .then((res) => {
        const { dealer_cards } = res.data;
        setPlayerCards((prevCards) => [...prevCards, ...dealer_cards]); // Update the state with received cards
        console.log(dealer_cards);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <div className="flex flex-row gap-5 items-center justify-center">
      {playerArray.map((card, index) => (
        <Card key={index} value={card} />
      ))}
    </div>
  );
};

export default Decker;
