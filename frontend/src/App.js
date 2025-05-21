import React, { useState, useEffect } from "react";
import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [documents, setDocuments] = useState([]);
  const [file, setFile] = useState(null);
  const [uploadMsg, setUploadMsg] = useState("");
  const [selectedDoc, setSelectedDoc] = useState(null);
  const [docDetails, setDocDetails] = useState(null);

  useEffect(() => {
    fetchDocuments();
  }, []);

  const fetchDocuments = async () => {
    const res = await axios.get(`${API_BASE}/documents/`);
    setDocuments(res.data);
  };

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    try {
      const res = await axios.post(`${API_BASE}/upload/`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setUploadMsg(res.data.message || "Uploaded!");
      setFile(null);
      fetchDocuments();
    } catch (err) {
      setUploadMsg("Upload failed.");
    }
  };

  const handleDownload = (id) => {
    window.open(`${API_BASE}/documents/${id}/download`, "_blank");
  };

  const handleDelete = async (id) => {
    await axios.delete(`${API_BASE}/documents/${id}`);
    fetchDocuments();
    if (selectedDoc === id) {
      setDocDetails(null);
      setSelectedDoc(null);
    }
  };

  const handleShowDetails = async (id) => {
    setSelectedDoc(id);
    const res = await axios.get(`${API_BASE}/documents/${id}`);
    setDocDetails(res.data);
  };

  return (
    <div style={{ maxWidth: 600, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h2>Document Uploader</h2>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={handleFileChange} accept=".pdf,.png,.jpg,.jpeg" />
        <button type="submit" disabled={!file}>Upload</button>
      </form>
      <div style={{ color: "green", margin: "10px 0" }}>{uploadMsg}</div>
      <h3>Uploaded Documents</h3>
      <ul>
        {documents.map((doc) => (
          <li key={doc.id} style={{ marginBottom: 10 }}>
            <b>{doc.filename}</b> ({doc.filetype}){" "}
            <button onClick={() => handleDownload(doc.id)}>Download</button>{" "}
            <button onClick={() => handleDelete(doc.id)}>Delete</button>{" "}
            <button onClick={() => handleShowDetails(doc.id)}>Details</button>
          </li>
        ))}
      </ul>
      {docDetails && (
        <div style={{ border: "1px solid #ccc", padding: 16, marginTop: 24 }}>
          <h4>Details for: {docDetails.filename}</h4>
          <strong>Extracted Text:</strong>
          <pre style={{ background: "#f9f9f9", padding: 8, maxHeight: 200, overflow: "auto" }}>
            {docDetails.extracted_text}
          </pre>
          <strong>Sentiment:</strong>
          <pre>{JSON.stringify(docDetails.sentiment, null, 2)}</pre>
          <button onClick={() => { setDocDetails(null); setSelectedDoc(null); }}>Close</button>
        </div>
      )}
    </div>
  );
}

export default App;
