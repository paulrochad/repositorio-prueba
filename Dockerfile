FROM       python:3
LABEL      maintainer="Paul Rocha"

RUN        pip install mysql.connector
RUN        pip install datetime

WORKDIR    /app
COPY       autentificador.py /app/
RUN        chmod a+x autentificador.py

ENTRYPOINT ["./autentificador.py"]