# API Hit Tracking and Analytics Dashboard

## Project Overview
This project is a web application that tracks API hits, stores them in a PostgreSQL database, and presents insightful visualizations on a separate dashboard. It provides valuable insights into API usage patterns and trends, facilitating informed decision-making.

## Features
- Tracks API hits and stores them in a PostgresSQL database.
- Displays API hit analytics in a user-friendly dashboard.
- Visualizes data using pie charts and bar charts.
- Supports filtering and detailed views of API hit data.

## Tech Stack
- Backend: Flask, SQLAlchemy, Flask-Migrate, PostgresSQL
- Frontend: React.js, Bootstrap, Chart.js
- Database: PostgresSQL

## Prerequisites
- Python 3.x
- Node.js and npm
- PostgresSQL

## Setup Instructions

### Backend

1. **Clone the repository:**
    ```sh
    git clone <https://github.com/kartikgupta09/API_COUNT_ENEGMA.git>
    cd APICount
    cd flask_app
    ```

2. **Set up a virtual environment:**
    ```sh
    python -m venv .venv
    source venv/bin/activate   # On Windows, use `.venv\Scripts\activate`
    ```

3. **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database:**
    - Create a PostgreSQL database.
    - Update the `config.py` file in the `flask_app` folder with your database URI:
        ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/api_hits'
        ```

5. **Run the database migrations:**
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the Flask application:**
    ```sh
    flask run
    ```

### Frontend

1. **Navigate to the frontend directory:**
    ```sh
    cd api-dashboard
    ```

2. **Install the required npm packages:**
    ```sh
    npm install
    ```

3. **Start the React application:**
    ```sh
    npm start
    ```
# API Hit Tracking and Analytics Dashboard

![Dashboard](image/api_image.png)
![Dashboard](image/api_image_2.png)

## Project Overview
This project is a web application that tracks API hits, stores them in a PostgreSQL database, and presents insightful visualizations on a separate dashboard. It provides valuable insights into API usage patterns and trends, facilitating informed decision-making.


## Folder Structure
```plaintext

── flask_app
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── migrations
│   └── ...
├── api-dashboard
│   ├── public
│   ├── src
│   │   ├── Dashboard.js
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── Dashboard.css
│   │   └── ...
│   ├── package.json
│   └── ...
├── requirements.txt
└── README.md

