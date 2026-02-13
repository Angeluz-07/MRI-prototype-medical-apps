import { useState } from "react";
import axios from "axios"; // Importamos Axios
import { useAuth } from "./AuthContext";

const Login = () => {
  const { login } = useAuth(); // Usamos la función del contexto
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      // 1. Django + SimpleJWT espera un JSON, no URLSearchParams
      // 2. Axios convierte automáticamente el objeto a JSON
      const response = await axios.post("http://localhost:8000/api/login/", {
        username: formData.username,
        password: formData.password,
      });

      // 3. SimpleJWT responde con { access: "...", refresh: "..." }
      if (response.data.access) {
        login(response.data.access, response.data.refresh);
        
        alert("¡Inicio de sesión exitoso!");
      }
    } catch (err) {
      // 4. Axios maneja los errores en el bloque catch de forma más estructurada
      if (err.response) {
        // El servidor respondió con un error (400, 401, etc.)
        setError(err.response.data.detail || "Credenciales incorrectas");
      } else {
        // Error de red o el servidor está apagado
        console.log(err);
        setError("No se pudo conectar con el servidor (CORS o Red)");
      }
    }
  };

  return (
    <div className="container-fluid col-sm-12 col-md-4">
      <div className="row my-3 mx-auto">
        <h1>Log In</h1>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="row my-3 mx-auto">
          <input
            type="text"
            name="username"
            placeholder="username"
            value={formData.username}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        <div className="row my-3 mx-auto">
          <input
            type="password"
            name="password"
            placeholder="password"
            value={formData.password}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        {error && <div className="alert alert-danger my-2">{error}</div>}
        <div className="row my-3 mx-auto">
          <button type="submit" className="btn btn-success">
            Enter
          </button>
        </div>
      </form>
    </div>
  );
};

export default Login;