# FastAPI CRUD with PostgreSQL 🚀

A simple **FastAPI** CRUD (Create, Read, Update, Delete) API with **PostgreSQL** as the database and SQLAlchemy for ORM. This project follows best practices for structuring a FastAPI application.

---

## 📁 Project Structure
```
fastapi_crud/
│── alembic/            # Alembic migration files
│── app/
│   ├── routes/        # API route handlers
│   ├── config.py      # Environment configuration
│   ├── crud.py        # CRUD operations
│   ├── database.py    # Database connection
│   ├── dependencies.py# FastAPI dependencies
│   ├── main.py        # Entry point of the FastAPI app
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas for validation
│── venv/              # Virtual environment
│── .env               # Environment variables file
│── alembic.ini        # Alembic configuration
│── requirements.txt   # Required dependencies
│── README.md          # Documentation (this file)
```

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/fastapi-crud.git
cd fastapi-crud
```

### **2️⃣ Create & Activate Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up PostgreSQL Database**
- **Make sure PostgreSQL is installed and running.**
- Create a new database manually:
```sql
CREATE DATABASE fastapi_db;
```
- Open `.env` file and update the database connection:
```ini
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/fastapi_db
```

### **5️⃣ Run Database Migrations (Alembic)**
```bash
alembic upgrade head
```

### **6️⃣ Start the FastAPI Server**
```bash
uvicorn app.main:app --reload
```
📌 The API is now running at: **`http://127.0.0.1:8000`**

---

## 📮 API Endpoints

### **1️⃣ Create a Hero**
**`POST /heroes/`**
- **Request Body:**
```json
{
    "name": "Superman",
    "power": "Flight"
}
```
- **Response:**
```json
{
    "id": 1,
    "name": "Superman",
    "power": "Flight"
}
```

### **2️⃣ Get All Heroes**
**`GET /heroes/`**
- **Response:**
```json
[
    {
        "id": 1,
        "name": "Superman",
        "power": "Flight"
    }
]
```

### **3️⃣ Get a Hero by ID**
**`GET /heroes/{hero_id}`**
- **Response:**
```json
{
    "id": 1,
    "name": "Superman",
    "power": "Flight"
}
```

### **4️⃣ Update a Hero**
**`PUT /heroes/{hero_id}`**
- **Request Body:**
```json
{
    "name": "Batman",
    "power": "Martial Arts"
}
```
- **Response:**
```json
{
    "id": 1,
    "name": "Batman",
    "power": "Martial Arts"
}
```

### **5️⃣ Delete a Hero**
**`DELETE /heroes/{hero_id}`**
- **Response:**
```json
{
    "message": "Hero deleted successfully"
}
```

---

## 🛠 Tools & Technologies Used
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **Alembic** - Database migrations
- **Pydantic** - Data validation
- **Uvicorn** - ASGI web server
- **Postman** - API testing

---

## 🛠 Testing with Postman
1. Open **Postman**.
2. Send requests to `http://127.0.0.1:8000`.
3. Use the JSON bodies provided in the **API Endpoints** section.

---

## 🎯 Next Steps
✅ Add authentication (JWT tokens).
✅ Implement pagination for large datasets.
✅ Add logging and error handling.

---

## ⚡ Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License
This project is licensed under the **MIT License**.

---

🚀 **Now, you can start building on FastAPI with PostgreSQL!** 🚀

