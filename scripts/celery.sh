#!/bin/sh

set -e

celery -A app beat -l INFO &