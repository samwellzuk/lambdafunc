python -m compileall ./awsfrwk
python -m compileall lambda_function.py
py-lambda-packer
aws s3 cp py-lambda-package.zip s3://cloudspider/
rm py-lambda-package.zip -f
python update_function_code.py
