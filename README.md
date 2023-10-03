# Finance App — Backend

Hello 👋
The frontend part for this project is provided here: https://annkurat.github.io/finance-app-frontend/. For the application to fully function, you first need to clone the backend repository

```bash
git clone https://github.com/annkurat/finance-app-backend
```

and then start the server on http://127.0.0.1:8000/.

## Installation

#### 1. Create virtualenv

```bash
pip install virtualenv
```

```bash
virtualenv venv
```

#### 2. Activate virtual environment:

For Windows:

```bash
venv\Scripts\activate
```

For macOS and Linus:

```bash
source venv/bin/activate
```

#### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 4. Apply migrations:

```bash
python manage.py migrate
```

#### 5. Start project

```bash
py manage.py runserver
```

## Create dependencies

Activate virtual environment and run:

```bash
pip freeze > requirements.txt
```

## Deactivate the virtual environment

```bash
deactivate
```
