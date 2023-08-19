import logo from "./logo.svg";
import Player from "./Components/Player";
import "./App.css";

function App() {
  return (
    <div className="App">
      <div className="flex flex-col justify-center items-center font-bold text-3xl gap-2 my-8">
        Player's Turn
      </div>
      <div className="flex flex-col pl-10 my-[40px] text-[36px] gap-10">
        <div>Player's Card:</div>
        <div>
          <Player />
        </div>
      </div>
      <div className="flex flex-col pl-10 my-[2px] text-[36px] gap-10">
        <div>Dealer's Card:</div>
        <div>
          <Player />
        </div>
      </div>
    </div>
  );
}

export default App;
