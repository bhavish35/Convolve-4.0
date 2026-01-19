import { useState } from "react";
import { queryMemory } from "../api";
import { styles } from "../styles";

export default function QueryMemory() {
  const [patientId, setPatientId] = useState("");
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  async function search() {
    setLoading(true);
    try {
      const res = await queryMemory(patientId, query);
      setResults(res.evidence || []);
    } catch (error) {
      alert("Error searching records");
    }
    setLoading(false);
  }

  return (
    <div style={styles.card}>
      <div style={styles.cardHeader}>
        <div style={{...styles.cardIcon, ...styles.iconGreen}}>🔍</div>
        <h2 style={styles.cardTitle}>Search Patient History</h2>
      </div>

      <div style={styles.grid2}>
        <div style={styles.formGroup}>
          <label style={styles.label}>Patient ID</label>
          <input
            type="text"
            placeholder="Enter patient ID"
            value={patientId}
            onChange={(e) => setPatientId(e.target.value)}
            style={styles.input}
          />
        </div>

        <div style={styles.formGroup}>
          <label style={styles.label}>Search Query</label>
          <input
            type="text"
            placeholder="Search medical history..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={styles.input}
          />
        </div>
      </div>

      <button
        onClick={search}
        disabled={loading}
        style={{...styles.button, ...styles.btnGreen}}
      >
        {loading ? "Searching..." : "Search Records"}
      </button>

      {results.length > 0 && (
        <div style={styles.results}>
          <h3 style={styles.resultsTitle}>Search Results ({results.length})</h3>
          <div>
            {results.map((r, i) => (
              <div key={i} style={styles.resultItem}>
                <p>{r}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}