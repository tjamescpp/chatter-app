Full-stack Social Media Web App

-   I created a mock social media web app using Python Django as a personal
    project.
-   It's a chatroom app that has posts for different subjects, a home feed that
    shows all of your posts, and other users posts in the chatrooms.
-   The app is deployed on Render. It may take a few minutes to load because
    it's using the free version.

Link: https://chatter-app-n87k.onrender.com/

The home page will ask you to login. I've created a default user to showcase the
app.

-   Username: tommy
-   Password: V7eW#y3AivcRQ@S

## Features

-   **User Authentication** - Secure login and registration system
-   **Real-time Chat** - Interactive chatrooms for different subjects
-   **Post Creation** - Share thoughts and content with the community
-   **Home Feed** - Personalized timeline showing your posts and followed users
-   **Subject-based Chatrooms** - Organized discussions by topic
-   **User Profiles** - Customizable user profiles and settings
-   **Responsive Design** - Mobile-friendly interface

## Getting Started

### Prerequisites

-   Python 3.8+
-   Django 4.0+
-   pip package manager

### Installation

1. Clone the repository

    ```bash
    git clone <repository-url>
    cd twtapp
    ```

2. Create a virtual environment

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations

    ```bash
    python manage.py migrate
    ```

5. Start the development server

    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://localhost:8000`
