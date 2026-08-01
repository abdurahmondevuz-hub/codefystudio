#!/bin/bash
set -e

echo '=== Staticfiles yig'ilmoqda ==='
python manage.py collectstatic --noinput

echo '=== Bot ishga tushmoqda ==='
python bot/bot.py &
BOT_PID=$!
echo "Bot PID: $BOT_PID"

echo '=== Gunicorn ishga tushmoqda ==='
exec gunicorn scr.wsgi:application --bind 0.0.0.0:${PORT:-8000}
