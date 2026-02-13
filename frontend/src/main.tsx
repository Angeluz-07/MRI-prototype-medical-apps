import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
//import './index.css'
import Home from "./components/home";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import { AuthProvider } from "./components/AuthContext";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    {/* <--App />*/}
    <AuthProvider>
      <Home />
    </AuthProvider>
  </StrictMode>,
);
