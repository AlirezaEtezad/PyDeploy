# 
FROM python

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
COPY ./TodoList.db /code/TodoList.db

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]