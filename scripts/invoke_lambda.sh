#!/bin/sh
aws lambda invoke --region=$(terraform output --raw region_name) --function-name=$(terraform output --raw function_name) response.json
