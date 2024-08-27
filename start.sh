#!/bin/sh
# Start the Uvicorn server
exec uvicorn index:app --reload --host 0.0.0.0 --port ${PORT:-8080}
# exec python index.py