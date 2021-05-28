FROM python:3.9

RUN useradd --create-home userapi
WORKDIR /Pycharm_flask_project

RUN pip install -U pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system
COPY / .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 5000
CMD ["gunicorn", "-b0.0.0.0:8000", "wsgi:app"]