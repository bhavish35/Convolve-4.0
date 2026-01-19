import AddMemory from "./components/AddMemory";
import QueryMemory from "./components/QueryMemory";
import Emergency from "./components/Emergency";
import { styles } from "./styles";

export default function App() {
  return (
    <div style={styles.body}>
      <div style={styles.container}>
        <div style={styles.header}>
          <div style={styles.headerTitle}>
            <div style={styles.logo}>💊</div>
            <h1 style={styles.h1}>VitaTrace</h1>
          </div>
          <p style={styles.subtitle}>Advanced Patient Memory Management System</p>
        </div>

        <div style={styles.cardContainer}>
          <AddMemory />
          <QueryMemory />
          <Emergency />
        </div>

        <footer style={styles.footer}>
          <p>© 2026 VitaTrace. Secure medical data management.</p>
        </footer>
      </div>
    </div>
  );
}
