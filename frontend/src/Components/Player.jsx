import React from "react";
import Card from "./Card";
import { useEffect } from "react";
import axios from "axios";

const Player = () => {
    const [playerArray, setPlayerCards] = React.useState([]);

    useEffect(() => {
      // Fetch card data from the server when the component mounts
      axios.get("http://127.0.0.1:5000/deck")
        .then((res) => {
          const { player_cards } = res.data;
          setPlayerCards(...Card,  player_cards);
          console.log(playerArray) // Update state with player cards
        })
        .catch((err) => {
          console.log(err);
        });
    }, []); //


  return (
    <div className="flex flex-row gap-5 items-center justify-center">
      {playerArray.map((card, index) => (
        <Card key={index} value={card} />
      ))}
    </div>
  );
};

export default Player;
