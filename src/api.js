const BASE_URL = "http://127.0.0.1:8000";

export async function addMemory(data) {
  const res = await fetch(`${BASE_URL}/add_memory`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function queryMemory(patient_id, query) {
  const res = await fetch(
    `${BASE_URL}/query?patient_id=${patient_id}&query=${query}`
  );
  return res.json();
}

const BASE = "http://127.0.0.1:8000";

export async function requestOTP(patient_id) {
  const res = await fetch(
    `${BASE}/emergency/request-otp?patient_id=${patient_id}`,
    { method: "POST" }
  );
  return res.json();
}

export async function verifyOTP(patient_id, otp) {
  const res = await fetch(
    `${BASE}/emergency/verify?patient_id=${patient_id}&otp=${otp}`,
    { method: "POST" }
  );
  return res.json();
}

  
