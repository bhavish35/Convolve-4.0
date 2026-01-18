import { useState } from "react";
import { queryMemory } from "../api";

export default function QueryMemory() {
  const [patientId, setPatientId] = useState("");
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  async function search() {
    const res = await queryMemory(patientId, query);
    setResults(res.evidence || []);
  }

  return (
    <div>
      <h2>Search Patient History</h2>

      <input placeholder="Patient ID"
        onChange={(e) => setPatientId(e.target.value)} />

      <input placeholder="Query"
        onChange={(e) => setQuery(e.target.value)} />

      <button onClick={search}>Search</button>

      <ul>
        {results.map((r, i) => <li key={i}>{r}</li>)}
      </ul>
    </div>
  );
}
