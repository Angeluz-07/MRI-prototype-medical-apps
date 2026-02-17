import {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
} from "react";
import axios from "axios"; // Importamos Axios

interface User {
  username: string;
  email: string;
  // add other fields like avatar, bio, etc.
}

interface AuthContextType {
  isAuthenticated: boolean;
  user: User | null; // New user state
  login: (access: string, refresh: string) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(
    !!localStorage.getItem("access_token"),
  );

  // Function to fetch user data using the token
  const fetchUserData = async () => {
    try {
      const API_URL = "http://127.0.0.1:8000/api/me";

      // 1. Get the token from storage
      const token = localStorage.getItem("access_token");

      const response = await axios.get(API_URL, {
        // 2. Add the headers object
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setUser(response.data);
      console.log(response.data)
    } catch (err) {
      logout(); // If fetching user fails, token might be invalid
    }
  };

  useEffect(() => {
    if (isAuthenticated) {
      fetchUserData();
    }
  }, [isAuthenticated]);

  const login = (access: string, refresh: string) => {
    localStorage.setItem("access_token", access);
    localStorage.setItem("refresh_token", refresh);
    setIsAuthenticated(true);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth debe usarse dentro de AuthProvider");
  return context;
};
