FROM python:3.9-slim

WORKDIR /opt/app
COPY App App
COPY db db
COPY main.py main.py
COPY requirements.txt requirements.txt

EXPOSE 5000

RUN python -m pip install -U pip --trusted-host pypi.org --trusted-host files.pythonhosted.org
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]
