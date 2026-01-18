import { useState } from "react";
import { addMemory } from "../api";

export default function AddMemory() {
  const [form, setForm] = useState({
    patient_id: "",
    text: "",
    category: "",
    critical: false,
  });

  async function submit() {
    await addMemory(form);
    alert("Memory stored successfully");
  }

  return (
    <div>
      <h2>Add Patient Memory</h2>

      <input placeholder="Patient ID"
        onChange={(e) => setForm({ ...form, patient_id: e.target.value })} />

      <textarea placeholder="Medical note"
        onChange={(e) => setForm({ ...form, text: e.target.value })} />

      <input placeholder="Category"
        onChange={(e) => setForm({ ...form, category: e.target.value })} />

      <label>
        <input type="checkbox"
          onChange={(e) => setForm({ ...form, critical: e.target.checked })} />
        Critical
      </label>

      <button onClick={submit}>Save</button>
    </div>
  );
}
