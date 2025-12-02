Calisthenics Progress Tracker

A lightweight full-stack project for tracking calisthenics workout data.
Built with Python + Flask on the backend and a minimal HTML/JavaScript UI on the frontend.



- Features

Add workout entries (exercise, weight, reps)

Retrieve all entries for any user

REST API built with Flask

Simple browser-based UI using Fetch API



- Tech Stack

Backend: Python, Flask
Frontend: HTML, JavaScript
Tools: Virtual environment



- How to Run (on Linux)

1. Clone this repository:
```bash
git clone https://github.com/richardkapsh/Calisthenics-tracker

2. Change to its directory
```bash
cd Calisthenics-tracker

3. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

4. Install dependencies
```bash
pip install -r requirements.txt

5. Start the server
```bash
python3 server.py

6. Open the frontend
Just open frontend.html in your browser or go the website listed at this step


- API Endpoints

POST /progress?userId=<id>

Add a new workout entry.

GET /progress?userId=<id>

Fetch all workout entries for a user.


- Project Structure
project/
├── server.py
├── requirements.txt
└── frontend.html


- Why I Built This

To practice backend development, routing, API design, data handling, and connecting a frontend client to an HTTP server.
