#!/bin/bash
# turn on bash's job control
set -m

airflow initdb &
airflow scheduler -D &
airflow webserver --port 8080

