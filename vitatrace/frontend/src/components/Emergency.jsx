import { useState } from "react";
import { requestOTP, verifyOTP } from "../api";
import { styles } from "../styles";

export default function Emergency() {
  const [patientId, setPatientId] = useState("");
  const [otp, setOtp] = useState("");
  const [demoOtp, setDemoOtp] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleOTP() {
    setLoading(true);
    try {
      const data = await requestOTP(patientId);
      setDemoOtp(data.otp);
      setResult(null);
    } catch (error) {
      alert("Error generating OTP");
    }
    setLoading(false);
  }

  async function handleEmergency() {
    setLoading(true);
    try {
      const data = await verifyOTP(patientId, otp);
      setResult(data);
    } catch (error) {
      alert("Error verifying OTP");
    }
    setLoading(false);
  }

  return (
    <div style={styles.emergencyCard}>
      <div style={styles.cardHeader}>
        <div style={{...styles.cardIcon, ...styles.iconRed}}>🛡️</div>
        <h2 style={styles.cardTitle}>🚨 Emergency Access</h2>
      </div>

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

      <button
        onClick={handleOTP}
        disabled={loading}
        style={{...styles.button, ...styles.btnOrange}}
      >
        🔐 {loading ? "Generating..." : "Generate OTP"}
      </button>

      {demoOtp && (
        <div style={styles.otpDisplay}>
          <p style={styles.otpLabel}>🔐 Demo OTP:</p>
          <p style={styles.otpValue}>{demoOtp}</p>
        </div>
      )}

      <div style={styles.formGroup}>
        <label style={styles.label}>Enter OTP</label>
        <input
          type="text"
          placeholder="Enter 6-digit OTP"
          value={otp}
          onChange={(e) => setOtp(e.target.value)}
          style={{...styles.input, textAlign: 'center', fontSize: '18px', letterSpacing: '3px'}}
        />
      </div>

      <button
        onClick={handleEmergency}
        disabled={loading}
        style={{...styles.button, ...styles.btnRed}}
      >
        {loading ? "Verifying..." : "Emergency Access"}
      </button>

      {result?.error && (
        <div style={styles.alertError}>
          <p>❌ {result.error}</p>
        </div>
      )}

      {result?.critical_info && (
        <div style={styles.criticalInfo}>
          <h3 style={styles.resultsTitle}>Critical Information:</h3>
          <div>
            {result.critical_info.map((item, i) => (
              <div key={i} style={styles.criticalItem}>
                <p>{item}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {result?.warning && (
        <div style={styles.alertWarning}>
          <p>{result.warning}</p>
        </div>
      )}
    </div>
  );
}