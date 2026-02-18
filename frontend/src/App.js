import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    Age: "",
    Severity: "",
    Gender: "Male",
    Diagnosis: "Cancer",
    Procedure: "Surgery"
  });

  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/predict", {
        Age: Number(formData.Age),
        Severity: Number(formData.Severity),
        Gender: formData.Gender,
        Diagnosis: formData.Diagnosis,
        Procedure: formData.Procedure
      });

      setPrediction(response.data.predicted_treatment_cost);
    } catch (error) {
      console.error("Error:", error);
      alert("Error connecting to backend.");
    }
  };

  return (
    <div className="container">
      <h1>AI Treatment Cost Prediction</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="Age"
          placeholder="Age"
          onChange={handleChange}
          required
        />

        <input
          type="number"
          name="Severity"
          placeholder="Severity (1-5)"
          onChange={handleChange}
          required
        />

        <select name="Gender" onChange={handleChange}>
          <option>Male</option>
          <option>Female</option>
        </select>

        <select name="Diagnosis" onChange={handleChange}>
          <option>Cancer</option>
          <option>Diabetes</option>
          <option>Heart Disease</option>
          <option>Infection</option>
        </select>

        <select name="Procedure" onChange={handleChange}>
          <option>Surgery</option>
          <option>Medication</option>
          <option>Therapy</option>
        </select>

        <button type="submit">Predict Cost</button>
      </form>

      {prediction && (
        <h2>Predicted Cost: ₹ {prediction.toFixed(2)}</h2>
      )}
    </div>
  );
}

export default App;
