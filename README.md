# Finance app backend

## Installation

#### 1. Create virtualenv

```bash
pip install virtualenv
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
