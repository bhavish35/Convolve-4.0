import { useState } from "react";
import { requestOTP, verifyOTP } from "../api";

export default function EmergencyAccess() {
  const [patientId, setPatientId] = useState("");
  const [otp, setOtp] = useState("");
  const [demoOtp, setDemoOtp] = useState(null);
  const [result, setResult] = useState(null);

  async function handleOTP() {
    const data = await requestOTP(patientId);
    setDemoOtp(data.otp);
    setResult(null);
  }

  async function handleEmergency() {
    const data = await verifyOTP(patientId, otp);
    setResult(data);
  }

  return (
    <div>
      <h3>🚑 Emergency Access</h3>

      <input
        placeholder="Patient ID"
        value={patientId}
        onChange={(e) => setPatientId(e.target.value)}
      />

      <button onClick={handleOTP}>Generate OTP</button>

      {demoOtp && (
        <p style={{ color: "yellow" }}>
          🔐 Demo OTP: <b>{demoOtp}</b>
        </p>
      )}

      <input
        placeholder="Enter OTP"
        value={otp}
        onChange={(e) => setOtp(e.target.value)}
      />

      <button onClick={handleEmergency}>Emergency Access</button>

      {result?.error && (
        <p style={{ color: "red" }}>❌ {result.error}</p>
      )}

      {result?.critical_info && (
        <ul>
          {result.critical_info.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      )}

      {result?.warning && (
        <p style={{ color: "orange" }}>{result.warning}</p>
      )}
    </div>
  );
}
