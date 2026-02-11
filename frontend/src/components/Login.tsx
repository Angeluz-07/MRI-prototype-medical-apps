import { useState } from "react";

const Login = () => {
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

    // FastAPI espera los datos en este formato por defecto para OAuth2
    const body = new URLSearchParams();
    body.append("username", formData.username);
    body.append("password", formData.password);

    try {
      const response = await fetch("http://localhost:8080/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: body,
      });

      if (response.ok) {
        const data = await response.json();
        // Guardamos el token en localStorage
        localStorage.setItem("token", data.access_token);
        alert("¡Inicio de sesión exitoso!");
        window.location.href = "/dashboard"; // Redirigir
      } else {
        const errorData = await response.json();
        setError(errorData.detail || "Error al iniciar sesión");
      }
    } catch (err) {
      setError("Error de conexión con el servidor");
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
            value={formData.password}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <div className="row my-3 mx-auto">
          <button type="submit" className="btn btn-success">
            Entrar
          </button>
        </div>
      </form>
    </div>
  );
};

export default Login;
