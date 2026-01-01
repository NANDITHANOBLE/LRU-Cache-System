```md
# 🔄 Advanced LRU Cache Implementation  
**Python | Doubly Linked List | HashMap | Flask | HTML | CSS | JavaScript**

---

## 📌 Project Overview

This project implements an **Advanced LRU (Least Recently Used) Cache System** using a **Doubly Linked List** and a **Dictionary (HashMap)** to achieve **O(1)** time complexity for cache operations.

The project also includes a **Flask-based web interface** that allows users to interact with the cache using a browser.

---

## 🎯 Objectives

- Implement LRU Cache efficiently
- Demonstrate real-world use of Data Structures
- Provide a user-friendly web interface
- Persist cache data using JSON
- Make the project interview and resume ready

---

## 🧠 Core Concept

- **Doubly Linked List**
  - Maintains usage order
  - Most Recently Used (MRU) at head
  - Least Recently Used (LRU) at tail

- **Dictionary (HashMap)**
  - Stores key → node mapping
  - Enables constant time access

---

## ⚙️ Features

### Core Features
- PUT (Insert / Update)
- GET (Retrieve value)
- Automatic LRU eviction
- DELETE specific key
- Display cache order

### Advanced Features
- Cache hit & miss tracking
- TTL (Time-To-Live) support
- Dynamic cache resizing
- Persistent storage using JSON
- Web-based UI (HTML, CSS, JS)
- Automated test cases

---

## 🏗️ System Architecture

```

User Interface (HTML, CSS, JS)
↓
Flask API
↓
LRU Cache (DLL + HashMap)
↓
JSON Storage

```

---

## 📁 Folder Structure

```

LRU_Cache_Project/
│
├── app.py                 # Flask backend
├── lru_cache.py           # LRU Cache logic
├── node.py                # Doubly Linked List node
├── utility.py             # JSON save/load helpers
├── cache_data.json        # Persistent cache storage
├── test.py                # Test cases
│
├── templates/
│   └── index.html         # Frontend HTML
│
├── static/
│   ├── style.css          # Styling
│   └── script.js          # Client-side logic
│
└── README.md

````

---

## 📄 File Description

### `node.py`
Defines a doubly linked list node with:
- key
- value
- prev & next pointers
- timestamp (for TTL)

### `lru_cache.py`
- Implements LRU logic
- Handles GET, PUT, DELETE
- Manages eviction and statistics

### `utility.py`
- Saves cache to `cache_data.json`
- Loads cache data on restart

### `app.py`
- Flask server
- API endpoints for cache operations

### `index.html`
- User input form
- Cache display section

### `script.js`
- Sends requests using Fetch API
- Updates UI dynamically

### `style.css`
- Responsive and modern UI design

### `test.py`
- Tests all cache operations

---

## ▶️ How to Run the Project

### Step 1: Install Python
Ensure Python 3.8+ is installed.

```bash
python --version
````

---

### Step 2: Install Flask

```bash
pip install flask
```

---

### Step 3: Run the Application

```bash
python app.py
```

Open browser and visit:

```
http://127.0.0.1:5000
```

---

### Step 4: Run Tests

```bash
python test.py
```

---

## 🧪 Sample Inputs

| Operation | Key | Value |
| --------- | --- | ----- |
| PUT       | A   | 100   |
| PUT       | B   | 200   |
| PUT       | C   | 300   |
| GET       | A   | -     |
| PUT       | D   | 400   |

👉 Cache capacity exceeded → **B is evicted**

---

## ⏱️ Time Complexity

| Operation | Time |
| --------- | ---- |
| GET       | O(1) |
| PUT       | O(1) |
| DELETE    | O(1) |

Space Complexity: **O(N)**

---

## 🌍 Real-World Applications

* Web browser caching
* Database query caching
* Operating system memory management
* API response caching

---

## 🎓 Interview Explanation

> “This project uses a Doubly Linked List and HashMap to implement an LRU Cache with constant-time operations. It also includes a Flask-based web interface, persistence using JSON, and advanced features like TTL and cache statistics.”

---

## 🚀 Future Enhancements

* Authentication system
* Cache visualization graphs
* Redis-style REST API
* Cloud deployment
* Role-based access

---

## 🧑‍💻 Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* JSON

---

## ✅ Conclusion

This project demonstrates strong knowledge of:

* Data Structures
* Backend development
* Frontend integration
* System design concepts

```