
# Flask Project and Tutorial

Welcome to the Flask Project! This guide will walk you through the steps to set up and run the project on your local Windows machine.

## 🚀 Getting Started

### 1. Clone the Repository

Open your terminal (e.g. Command Prompt or PowerShell), then run:

```bash
git clone https://github.com/eyespywmlileye/FlaskTutorial.git
cd FlaskTutorial
````
---

### 2. Create a Virtual Environment (Windows)

Run the following command to create a virtual environment in the project folder:

```bash
python -m venv .venv
```

---

### 3. Activate the Virtual Environment

In **Command Prompt**:

```bash
.venv\Scripts\activate
```

In **PowerShell**:

```bash
.\.venv\Scripts\Activate.ps1
```

You should now see `(.venv)` at the beginning of your terminal line, showing that the environment is active.

---

### 4. Install the Required Packages

The `requirements.txt` file lists all the Python packages and versions your Flask project depends on. It's used to ensure consistent environments across different setups by letting others install the exact same dependencies.

Once the virtual environment is activated, install all dependencies:

```bash
pip install -r requirements.txt
```

---

### 5. Run the Application

Start the Flask app using:

```bash
python run.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

---

## ✅ Verify It Works

Open your web browser and go to:

```
http://127.0.0.1:5000/api/status
```

You should see a response like:

```json
{
    "status": "ok", 
    "message": "Inventory API is running"
}
```

---

# 📂 Project Structure 

Once you run your project, your file strucutre will look like this, with the `instance/` folder also being created. 

The `instance/` folder in a Flask project is used to store environment-specific or sensitive files that shouldn't be committed to version control. Common use cases include:

* SQLite database files
* Configuration files containing secrets (e.g., API keys, DB URIs)
* Uploads or runtime-generated content

```
FlaskTutorial/
│
├── run.py
├── requirements.txt
├── .gitignore
├── .venv/
└── app/
    ├── __init__.py
    ├── routes.py
    ├── config.py
    ├── extensions.py
    └── models.py
```

---

Happy coding! 💻🔥
