import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ message: "Error uploading file." });
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>OCR & Sentiment Analysis</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".pdf,.png,.jpg,.jpeg" onChange={handleFileChange} />
        <button type="submit" disabled={!file || loading} style={{ marginLeft: 10 }}>
          {loading ? "Processing..." : "Upload & Analyze"}
        </button>
      </form>
      {result && (
        <div style={{ marginTop: 30 }}>
          <h2>Result</h2>
          <p><strong>Message:</strong> {result.message}</p>
          <p><strong>Filename:</strong> {result.filename}</p>
          <p><strong>Extracted Text:</strong></p>
          <pre style={{ background: "#f0f0f0", padding: 10 }}>{result.extracted_text}</pre>
          <p><strong>Sentiment:</strong></p>
          <pre style={{ background: "#f0f0f0", padding: 10 }}>{JSON.stringify(result.sentiment, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
