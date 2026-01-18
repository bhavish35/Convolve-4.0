import AddMemory from "./components/AddMemory";
import QueryMemory from "./components/QueryMemory";
import Emergency from "./components/Emergency";

export default function App() {
  return (
    <div style={{ padding: 20 }}>
      <h1>VitaTrace Dashboard</h1>
      <AddMemory />
      <hr />
      <QueryMemory />
      <hr />
      <Emergency />
    </div>
  );
}
