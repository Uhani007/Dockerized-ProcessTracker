# Dockerized-ProcessTracker  🐳

**Dockerized-ProcessTracker** is a Python-based tool for monitoring running system processes.
It uses the `psutil` library to gather detailed process information.
With Docker support, it can run consistently across different environments.

---

## 🚀 Features

*  Logs system process details (PID, CPU, memory, I/O, threads, etc.)
*  Built with Python & psutil
*  Dockerized for easy deployment
*  Continuous monitoring inside containers

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Dockerized-ProcessTracker.git
cd Dockerized-ProcessTracker
```

### 2️⃣ Build Docker image

```bash
sudo docker build -t process-tracker .
```

### 3️⃣ Run the container

```bash
sudo docker run --rm process-tracker
```

```

### 4️⃣ Run in background (optional)

```bash
sudo docker run -d --name proc-monitor process-tracker

```
