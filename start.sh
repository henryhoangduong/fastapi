#!/bin/sh
# Start the Uvicorn server
exec uvicorn app.index:app --host 0.0.0.0 --port $PORT