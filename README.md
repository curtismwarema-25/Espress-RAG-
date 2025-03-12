# Espresso(RAG)

## 🚀 Retrieval-Augmented Generation (RAG) with GPT4All

Espresso(RAG) is a **local Retrieval-Augmented Generation (RAG) system** leveraging **GPT4All** and **FAISS** for efficient document retrieval and question answering. This project ensures privacy and cost efficiency by running **fully offline** with local embeddings and models.

---

## 🛠 Features
- **💾 Local Model** – Uses GPT4All instead of OpenAI API to avoid rate limits and enhance privacy.
- **🔍 Document Retrieval** – Indexes and retrieves documents using FAISS.
- **📄 Text Chunking** – Splits documents into smaller chunks for efficient retrieval.
- **🧠 Local Embeddings** – Utilizes Hugging Face models for vector embeddings.

---

## 📥 Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/Espresso-RAG.git
cd Espresso-RAG
```

### 2️⃣ **Set Up a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Download GPT4All Model**
Ensure you have a GPT4All-compatible model downloaded and placed in:
```sh
C:/Users/curtis mwarema/AppData/Local/nomic.ai/GPT4All/
```

Set the path in **.env**:
```env
GPT4ALL_MODEL_PATH=C:/Users/curtis mwarema/AppData/Local/nomic.ai/GPT4All/YourModel.gguf
```

---

## 🚀 Usage

### **Run the RAG System**
```sh
python rag_demo.py
```

### **Ask a Question**
Modify `rag_demo.py` to input custom questions:
```python
question = "What is Espresso(RAG)?"
```
---

## 📜 Project Structure
```
Espresso-RAG/
│── documents.txt        # Text file with source documents
│── rag_demo.py          # Main script for running RAG
│── .env                 # Stores environment variables (API keys, model paths)
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation (this file)
│── venv/                # Virtual environment
```
---

## 🛠 Technologies Used
- **LangChain** – Orchestrates retrieval and response generation
- **GPT4All** – Local LLM for answering questions
- **FAISS** – Efficient similarity search and document retrieval
- **Hugging Face Embeddings** – Converts text into vector representations
- **Python dotenv** – Loads environment variables

---

## 🎯 Future Improvements
- ✅ Support for larger document collections
- ✅ Improved UI for interactive querying
- ✅ Fine-tuned local models for better responses

---

## 📬 Contact
For inquiries, reach out via:
📧 Email: curtismwarema01@gmail.com

---

### 🔥 Ready for the Interview! 🎤

