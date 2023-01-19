# RestAPI
First restAPI coded in python using FastAPI

## Requirements
- Have python in your device
- Have MySQL in your device

## Usage
- Create a virtual environment inside a folder
```terminal
python3 -m venv /path/to/new/virtual/environment
source /path/to/venv/bin/activate
```

- Run venv in Windows
```terminal
myenv\Scripts\activate.bat

```
- Run venv in MacOS
```terminal
source myenv/bin/activate
```

- Install all requirements from requirements.txt
```python
pip install -r requirements.txt
```

- Create a user in you MySQL workbench or through the terminal, click in the link for more instructions
[MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/)

- After downloading everything, run the following command to start the server
```python
uvicorn main:app --reload
```


