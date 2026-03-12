# Employee Management System 🧑‍💼

A simple Python + Tkinter application for managing employee records with a MySQL database.  
Features include **Add, Update, Delete, Refresh and View** employee records.

---

## 📦 Requirements

- Python 3.8+
- MySQL Server
- Pip (Python package manager)

Dependencies are listed in `requirements.txt`:
- `mysql-connector-python`
- `python-dotenv`

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/RamCharan-88/employee-management-system.git
cd employee-management-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
This project uses a `.env` file to store database credentials securely.

1. Copy the sample file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and update with your own database details:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password_here
   DB_NAME=abc_123
   ```

⚠️ **Important:** Never commit your real `.env` file. It is already ignored via `.gitignore`.

---

## 🗄️ Database Setup

Run the following SQL in MySQL:

```sql
CREATE DATABASE abc_123;
USE abc_123;

CREATE TABLE registration (
    id INT PRIMARY KEY,
    empname VARCHAR(100),
    mobile VARCHAR(20),
    salary DECIMAL(10,2)
);
```

---

## ▶️ Running the Application

```bash
python employee_management_sys.py
```

The Tkinter GUI will open, allowing you to:
- **Add** new employees
- **Update** existing records
- **Delete** employees
- **Refresh** all Records
- **View** all records in a table

---

## 🔐 Security Notes

- Database credentials are stored in `.env` (not in code).
- `.env` is ignored by Git, so your secrets remain private.
- `.env.example` is provided so others know what variables to set.

---

## 📂 Project Structure

```
employee-management-system/
│
├── employee_management_sys.py   # Main application
├── requirements.txt             # Python dependencies
├── .env.example                 # Sample environment variables
├── .gitignore                   # Ignore sensitive files
└── README.md                    # Project documentation
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit (`git commit -m "Add new feature"`)
5. Push (`git push origin feature-branch`)
6. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.
