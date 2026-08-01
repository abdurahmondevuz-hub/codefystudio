#!/bin/bash
set -e

echo "🤖 Bot ishga tushmoqda..."
python bot/bot.py &

echo "🌐 Gunicorn ishga tushmoqda..."
exec gunicorn scr.wsgi:application --bind 0.0.0.0:${PORT:-8000}
