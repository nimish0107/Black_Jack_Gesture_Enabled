import React from "react";
import Card from "./Card";
import axios from "axios";

const Player = () => {
  const playerArray = [];

  axios.get("http://localhost:5000/").then((res) => {
    playerArray.push(res.data);
  });

  return (
    <div className="flex flex-row gap-5 items-center justify-center">
      {playerArray.map((card, index) => (
        <Card key={index} value={card} />
      ))}
    </div>
  );
};

export default Player;
