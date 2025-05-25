🐑 Sheep Bot

Sheep Bot is a friendly, sheep-themed chatbot that helps users interact with and explore documents like PDFs in a conversational, intuitive way. Designed for students, educators, and professionals, Sheep Bot makes document research, theme discovery, and semantic search accessible and fun.
🌐 Live Demo & API
Web App: https://wasserstoff-aiinterntask.vercel.app/
API Docs (Swagger): https://mahindra-bot.biup.ai/docs#/
✨ Features
Document Upload: Add and manage your files through a simple sidebar.
Conversational Q&A: Ask natural language questions about your documents.
Semantic Search: Find relevant document sections using AI-powered embeddings.
Theme Identification: Discover main topics in your files via clustering.
Chat-Style UI: Enjoy a playful, sheep-themed chat interface with light/dark mode.
File Previews: Quickly view and select documents for analysis.
Robust Error Handling: Get clear feedback for unsupported files or system issues.
🏗️ System Architecture
Frontend:
Sheep-themed chat interface for uploads and Q&A.
Sidebar for file management and previews.
Backend (FastAPI):
Handles user requests and document operations.
Exposes RESTful endpoints for document management and chat.
Document Processor:
Chunking: Splits documents into smaller parts (e.g., paragraphs).
Embedding: Uses Sentence Transformers to turn text into semantic vectors.
Vector Database (ChromaDB):
Stores embeddings for fast, similarity-based search.
Clustering (KMeans):
Groups similar content to help users see document themes.
🧠 Methodologies
Document Chunking:
Files are split into smaller sections for precise analysis.
Semantic Embedding:
Each chunk is converted into a vector using Sentence Transformers, capturing its meaning.
Semantic Search:
User queries are embedded and compared to document vectors to find the most relevant content.
Clustering:
KMeans groups similar chunks to reveal key topics and themes.
Citation Support:
Each answer identifies the relevant chunk or section, helping users trace information (but does not provide direct clickable links).
🛠️ Technologies Used
FastAPI: For backend API development.
Sentence Transformers: For semantic text embeddings.
ChromaDB: For storing and searching embeddings.
scikit-learn: For clustering (KMeans).
Frontend: Modern JavaScript (React/Next.js or similar).
Docker: For consistent deployment across environments.
⚙️ Deployment & Scalability
Current Deployment:
Web: Hosted on Vercel (see site)
API: Hosted on a custom domain (see docs)
Scalability:
Modular architecture allows for horizontal scaling.
Docker support enables easy migration to any cloud provider.
💡 Design Choices & Challenges
Modular Codebase:
Separates concerns for easier scaling and maintenance.
Resource Optimization:
Uses lightweight models and efficient chunking for cloud compatibility.
Error Handling:
Provides user-friendly messages and robust backend logic.
Fun, Accessible UI:
Sheep personality, animations, and a welcoming chat experience.
Deployment Flexibility:
Not tied to any single provider; Docker-ready for future moves.
📚 References
FastAPI Docs
ChromaDB Docs
Sentence Transformers
scikit-learn
📝 Developer Notes
Building Sheep Bot was a journey of learning and problem-solving—from integrating NLP and vector search to overcoming deployment hurdles. After trying several hosting options, the project was successfully launched with help from an external expert, ensuring reliable public access. This process strengthened my skills in full-stack AI applications and cloud deployment.
🎯 Conclusion
Sheep Bot combines practical AI with a delightful user experience. Even with deployment and integration challenges, the project is now live, stable, and ready for real-world use. Sheep Bot stands as a testament to creative problem-solving and technical growth, making document research smarter and more enjoyable.
Questions or feedback?
Contact: [Your Name] — [your.email@example.com]
Sheep Bot: Your woolly smart assistant for document exploration!
