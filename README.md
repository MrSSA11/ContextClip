# 🚀 ContextClip: The Smart Clipboard Bot

### 🏷️ Project Tagline
Transforming volatile mobile clipboards into a permanent, context-aware digital second brain using Graph RAG and AI memory networks.

### 📌 Problem Statement
Standard mobile clipboards are volatile, short-lived, and isolated. The moment a user copies a new piece of text, code snippet, or web URL, their previous clipboard history is completely overwritten and lost. Furthermore, standard historical search engines rely on strict keyword text matching. If a user cannot remember the exact words of an item they copied days ago, finding that historical context is nearly impossible.

### 💡 The Solution
**ContextClip** completely revolutionizes mobile knowledge management. By leveraging a private 1-on-1 Discord Direct Message room as an instant text gateway, users can continuously dump raw clipboard items directly into the cloud. 

Instead of treating text like a flat database list, ContextClip utilizes the advanced **Cognee AI Memory Framework** to automatically extract entities, synthesize context, and construct an evolving, localized relational knowledge graph database. Users can then query their clipboard graph using casual, multi-hop natural language to recall connected records instantly.

---

## 🛠️ Technical Architecture & Stack

* **User Interface Layer:** Handled entirely by the native Discord Mobile/Desktop client, optimizing for single-tap entry and clean markdown parsing.
* **Gateway Communication:** Asynchronous event loops driven by the `discord.py` library to intercept incoming text streams securely.
* **Cognitive Memory Engine:** Open-source **Cognee Framework**, mapping chaotic text chunks into explicit ontological categories.
* **Core AI Layer:** Google **Gemini 2.5 Flash** for high-speed intent processing and text reasoning.
* **Vector & Graph Layer:** Google **`gemini-embedding-001`** (768-dimension vectors) combined with localized graph data frames to perform semantic searches without strict word matching.
* **Hosting Environment:** Built and fully simulated inside GitHub Codespaces.

---

## 🌟 Key Engineering Features

### 1. Direct-Message Ingest Engine (`cognee.remember`)
Users paste standard quotes, code chunks, or links into the chat. The bot triggers a real-time ingestion worker pipeline that automatically segments data and anchors text concepts cleanly into long-term vector maps without freezing the message listener thread.

### 2. Multi-Hop Graph Traversal Queries (`cognee.recall`)
Using the prefix `?`, the user invokes semantic context matching. The system maps the query to vector clusters, leaps across relational graph edges, and extracts multi-layered insights (e.g., linking a user name to a specific project name, and that project name directly to its target completion date).

### 3. Dynamic Human-Readable Filter Layer
Raw Graph database formats output messy metadata clusters filled with system strings and token hashes. ContextClip features a dedicated parsing layer that strips away structural system values, delivering clean, perfectly structured answers straight back to the user chat window.

---

## 🛣️ What's Next for ContextClip
* **24/7 Persistent Server Containerization:** Migrating the active code footprint onto isolated cloud microservices (Render/Koyeb) to ensure execution availability without exhausting developmental environments.
* **Multi-Modal Clipping:** Extending the memory graph boundaries to ingest binary images, voice recordings, and files using Gemini's multimodal layout.
