# 🌿 Agriportance API

A simple Flask REST API for managing renewable energy plant data — including routes for plants, farms, and sensor readings.  
Built using **Flask**, **PostgreSQL**, and **Flask-RESTful**.

---

## 🚀 Features

- View all plants stored in the PostgreSQL database  
- Add and fetch farm records (in-memory demo)  
- Calculate average plant capacity by region  
- Create and retrieve sensor readings  
- Test connection and basic arithmetic endpoints

---

## 🧰 Tech Stack

- **Python 3**
- **Flask** + **Flask-RESTful**
- **PostgreSQL**
- **psycopg2**
- **dotenv** for environment variables

---

## ⚙️ Installation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/simple-flask-api.git
cd simple-flask-api
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set up your .env file
Create a file named .env in the root folder with the following variables:

bash
Copy code
DB_HOST=localhost
DB_NAME=agriportance
DB_USER=postgres
DB_PASS=your_postgres_password
🧮 Database Setup (PostgreSQL)
Start PostgreSQL and connect:

bash
Copy code
psql -U postgres
Create the database:

sql
Copy code
CREATE DATABASE agriportance;
Connect to it:

sql
Copy code
\c agriportance
Create the plants table:

sql
Copy code
CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL,
    capacity FLOAT
);
Optionally insert some sample data:

sql
Copy code
INSERT INTO plants (name, region, capacity) VALUES
('SolarOne', 'East', 120.5),
('WindyHill', 'West', 200.3),
('HydroFlow', 'North', 150.8),
('GeoTherma', 'South', 180.0);
🧩 Running the Server
bash
Copy code
python app.py
The app will run at:

cpp
Copy code
http://127.0.0.1:5000
🔗 API Endpoints
Method	Endpoint	Description
GET	/hello	Test connection
POST	/api/sum	Add two numbers (JSON body: {"a": 5, "b": 7})
GET	/api/plants	Fetch all plants
GET	/api/avg_capacity	Average capacity by region
GET	/api/farms	Get all in-memory farms
POST	/api/farms	Add a new in-memory farm
POST	/api/readings/setup	Create readings table (if not exists)
GET	/api/readings	Get latest average readings per plant

📦 Example: Test /api/sum
Using curl:

bash
Copy code
curl -X POST -H "Content-Type: application/json" \
-d "{\"a\": 10, \"b\": 20}" \
http://127.0.0.1:5000/api/sum
Output:

json
Copy code
{"sum": 30}
💡 Notes
The /api/farms routes use an in-memory list — data resets on restart.

Use Postman or Insomnia to test POST endpoints easily.

For production, replace the dev server with Gunicorn or Waitress.

🧑‍💻 Author
Sango Mabhuti Yapi
Frontend & Python Developer | Chemistry + Computer Science Graduate
📍 Johannesburg, South Africa