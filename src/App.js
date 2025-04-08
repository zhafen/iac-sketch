import * as d3 from "d3";
import logo from './logo.svg';
import './App.css';


function MyButton() {
  return (
    <button>I'm a button</button>
  );
}

const resources = await d3.json("/resources.json");
const workflow = await d3.json("/workflow.json");

export default function App() {
  return (

    <div className="App">
      <header className="App-header">
        <p>
          Working.
        </p>
      </header>
    </div>
  );
}
