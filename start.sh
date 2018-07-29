#!/usr/bin/env bash

if [[ $PATH != *":/venv/bin:"* ]]
then
    echo "Activating the virtual environment"
    virtualenv venv
    . venv/bin/activate
fi

export FLASK_APP=lift_api
export DATABASE_URL="postgresql://$(whoami)@localhost/lift_api"
export FLASK_DEBUG=1

echo "Starting server <${FLASK_APP}>"

python3 flask run