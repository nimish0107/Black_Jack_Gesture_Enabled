import React from "react";
import Card from "./Card";

const Player = () => {
  const playerArray = ["2C", "3D", "4D", "5D", "6D", "7D", "8D", "9D"];

  return (
    <div className="flex flex-row gap-5 items-center justify-center">
      {playerArray.map((card, index) => (
        <Card key={index} value={card} />
      ))}
    </div>
  );
};

export default Player;
