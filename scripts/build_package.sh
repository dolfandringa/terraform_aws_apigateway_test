#!/bin/sh
cd hello-world
ls
rm "dist/*"
rm "package/*" -r
set -e
poetry build
poetry run pip install --upgrade -t package dist/*.whl
cd package ; zip -r ../artifact.zip . -x '*.pyc'
cd ..
cd ..
