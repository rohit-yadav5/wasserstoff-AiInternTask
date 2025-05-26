# 🐑 Sheep Bot

Sheep Bot is a friendly, sheep-themed chatbot that helps users interact with and explore documents like PDFs in a conversational, intuitive way. Designed for students, educators, and professionals, Sheep Bot makes document research, theme discovery, and semantic search both accessible and fun.

---

## 🌐 Live Demo & API

- 🔗 Live Website: [Sheep Bot Web App](https://wasserstoff-aiinterntask.vercel.app/)
- ⚙️ API Docs (Swagger): [Sheep Bot API](https://mahindra-bot.biup.ai/docs#/)

---
## 📺Demonstration Video

- 🔗Complete folder: [GDrive](https://drive.google.com/drive/folders/1wmRE1AhAQsZBopTXXE_s2dp81Hb5SBil?usp=share_link)

- 🔗 Google Drive: [Demo Videos](https://drive.google.com/drive/folders/1CFnADz2myb82HCp8jaEbTVe7i5I4aX61?usp=share_link)
- 🔗 Google Drive: [Demo Photos](https://drive.google.com/drive/folders/1VDaE7lynVCuuHKyXLB3pPKdwxJmS9qq9?usp=share_link)

---

## ✨ Features

- 📁 Document Upload – Add and manage your files through a simple sidebar.
- 💬 Conversational Q&A – Ask natural language questions about your documents.
- 🧠 Semantic Search – Find relevant document sections using AI-powered embeddings.
- 📌 Theme Identification – Discover main topics in your files using clustering.
- 💻 Chat-Style UI – Enjoy a sheep-themed interface with light/dark mode support.
- 🖼️ File Previews – Quickly view and select documents for analysis.
- 🛡️ Robust Error Handling – Get clear messages for unsupported files or system issues.

---

## 🏗️ System Architecture

- **Frontend**  
  Chat interface with a sidebar for uploads and previews, built using modern JavaScript frameworks (React/Next.js or similar).

- **Backend (FastAPI)**  
  Handles requests, document operations, and RESTful API endpoints.

- **Document Processor**  
  - Chunking: Splits files into smaller parts (like paragraphs).  
  - Embedding: Converts chunks to semantic vectors using Sentence Transformers.

- **Vector Database (ChromaDB)**  
  Stores embeddings for fast semantic search.

- **Clustering (KMeans)**  
  Groups similar content to identify themes in documents.

---

## 🧠 Methodologies

1. Document Chunking – Files are split into manageable sections.  
2. Semantic Embedding – Chunks are turned into meaningful vectors via Sentence Transformers.  
3. Semantic Search – User queries are compared with vectors to retrieve relevant text.  
4. Clustering – KMeans algorithm groups similar chunks to highlight key topics.  
5. Citation Support – Each result is traced back to its original section (not clickable).

---

## 🛠️ Technologies Used

- ⚙️ FastAPI – Backend API development.  
- 🔍 Sentence Transformers – Semantic vector generation.  
- 🧩 ChromaDB – Vector storage and semantic search.  
- 📊 scikit-learn – Clustering with KMeans.  
- 🌐 Frontend – React/Next.js (or similar).  
- 🐳 Docker – Consistent deployment environment.

---

## ⚙️ Deployment & Scalability

- **Current Deployment**  
  - ✅ Website hosted on Vercel  
  - ✅ API hosted on a custom domain with external help (due to limitations with platforms listed in the project PDF)

- **Scalability**  
  - Modular design enables horizontal scaling.  
  - Docker support allows easy migration to any modern cloud platform like Hugging Face Spaces, Render, or Railway.

---

## 💡 Design Choices & Challenges

- 🔄 Modular Codebase – Easier to manage, debug, and scale.  
- ⚡ Resource Optimization – Lightweight models for cloud compatibility.  
- 🧯 Error Handling – User-friendly backend and frontend messaging.  
- 🎨 Fun UI – Light/dark mode, sheep animations, playful responses.  
- 🚀 Flexible Deployment – Docker-ready, not tied to any single platform.

---

## 📝 Developer Notes

Building Sheep Bot was a challenging but rewarding experience. From integrating NLP and vector search to connecting the frontend and backend, each step came with its own learning curve. The biggest hurdle was deployment, as many of the suggested platforms weren’t suitable for my use case. With the help of an employee from my sister’s company, I finally hosted the project on a custom domain, ensuring reliable public access. This process taught me a lot about full-stack development, API integration, and cloud deployment.

---

## 🎯 Conclusion

Sheep Bot is more than just a chatbot — it’s a smart, interactive assistant that simplifies document research through AI. With features like semantic search, theme detection, and a creative UI, it brings both functionality and fun to users. Despite the initial deployment issues, the project is now live, stable, and production-ready. It’s a strong example of learning, growth, and creative problem-solving.

---

## 📚 References

- FastAPI Documentation  
- ChromaDB Documentation  
- Sentence Transformers  
- scikit-learn Documentation

---

## 📬 Contact

- Developer: Rohit Yadav  
- Email: rohityadav.0620@gmail.com  
- GitHub: [@rohit-yadav5](https://github.com/rohit-yadav5)  
- Portfolio: [rohit-yadav5.github.io](https://rohit-yadav5.github.io)
