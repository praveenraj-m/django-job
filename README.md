# Job Portal

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/downloads/release)

## Overview

This is a job portal web application allowing users to browse the latest Job listings on the website.
## Features

- **Job Listings:** Browse and search for jobs based on various criteria.
- **Subscription:** Users can subscribe to receive job updates.
- **Admin Panel:** Customize the built-in admin panel for efficient management.

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.0+

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/praveenraj-m/job-portal.git
    cd job-portal
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at [http://localhost:8000](http://localhost:8000)

## Usage

1. Log in as an admin using the superuser credentials created.
2. Manage job listings and user subscriptions via the admin panel.
3. Users can browse available jobs.
4. Users can subscribe to receive job updates by providing their name, mobile number, email, and choosing between weekly and monthly updates.


## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
