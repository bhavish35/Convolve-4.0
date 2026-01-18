import { useState } from "react";
import { addMemory } from "../api";
import { styles } from "../styles";

export default function AddMemory() {
  const [form, setForm] = useState({
    patient_id: "",
    text: "",
    category: "",
    critical: false,
  });
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    try {
      await addMemory(form);
      alert("Memory stored successfully");
      setForm({ patient_id: "", text: "", category: "", critical: false });
    } catch (error) {
      alert("Error storing memory");
    }
    setLoading(false);
  }

  return (
    <div style={styles.card}>
      <div style={styles.cardHeader}>
        <div style={{...styles.cardIcon, ...styles.iconBlue}}>➕</div>
        <h2 style={styles.cardTitle}>Add Patient Memory</h2>
      </div>

      <div style={styles.formGroup}>
        <label style={styles.label}>Patient ID</label>
        <input
          type="text"
          placeholder="Enter patient ID"
          value={form.patient_id}
          onChange={(e) => setForm({ ...form, patient_id: e.target.value })}
          style={styles.input}
        />
      </div>

      <div style={styles.formGroup}>
        <label style={styles.label}>Medical Note</label>
        <textarea
          placeholder="Enter detailed medical note..."
          value={form.text}
          onChange={(e) => setForm({ ...form, text: e.target.value })}
          rows="4"
          style={{...styles.input, ...styles.textarea}}
        />
      </div>

      <div style={styles.formGroup}>
        <label style={styles.label}>Category</label>
        <input
          type="text"
          placeholder="e.g., Diagnosis, Prescription, Lab Results"
          value={form.category}
          onChange={(e) => setForm({ ...form, category: e.target.value })}
          style={styles.input}
        />
      </div>

      <div style={styles.checkboxGroup}>
        <input
          type="checkbox"
          id="critical"
          checked={form.critical}
          onChange={(e) => setForm({ ...form, critical: e.target.checked })}
          style={styles.checkbox}
        />
        <label htmlFor="critical" style={styles.checkboxLabel}>
          ⚠️ Mark as Critical Information
        </label>
      </div>

      <button
        onClick={submit}
        disabled={loading}
        style={{...styles.button, ...styles.btnBlue}}
      >
        {loading ? "Saving..." : "Save Memory"}
      </button>
    </div>
  );
}
