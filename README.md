# Dockerized-ProcessTracker

**Dockerized-ProcessTracker** is a Python-based tool for monitoring running system processes.
It uses the `psutil` library to gather detailed process information and logs it into a file.
With Docker support, it can run consistently across different environments.

---

## 🚀 Features

* 📊 Logs system process details (PID, CPU, memory, I/O, threads, etc.)
* 🐍 Built with Python & psutil
* 🐳 Dockerized for easy deployment
* 📂 Automatic logging into `process_log.txt`
* 🔁 Continuous monitoring inside containers

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Dockerized-ProcessTracker.git
cd Dockerized-ProcessTracker
```

### 2️⃣ Build Docker image

```bash
sudo podman build -t process-tracker .
```

### 3️⃣ Run the container

```bash
sudo podman run --rm -v $(pwd):/app:Z process-tracker
```

This will log process details into:

```
~/ProcessTracker/process_log.txt
```

### 4️⃣ Run in background (optional)

```bash
sudo podman run -d --name proc-monitor -v $(pwd):/app:Z process-tracker
```

---





---

👉 Bas tum `your-username` ko apne GitHub username se replace karke use kar lena.

Kya chahte ho main tumhe **process_log.txt ka ek small real example output** bhi add karke README.md me daal dun (jaise Cardsafe-Encryptor me UI screenshot hoga)?
