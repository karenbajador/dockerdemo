FROM python:3.6.3
                      
ENV AIRFLOW_HOME=/app/airflow

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY /dags $AIRFLOW_HOME/dags/
COPY default_airflow.cfg $AIRFLOW_HOME/airflow.cfg
COPY run_airflow.sh run_airflow.sh

CMD ["./run_airflow.sh"]


