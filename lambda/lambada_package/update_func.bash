#!/bin/bash

# Define variables
VENV_DIR="venv"
PACKAGE_DIR="lambda_package"
ZIP_FILE="lambda_package.zip"

# Create and activate virtual environment
python -m venv $VENV_DIR
source $VENV_DIR/bin/activate

# Install dependencies
pip install -r requirements.txt -t $PACKAGE_DIR

# Copy your Lambda function code to the package directory
cp lambda_function.py $PACKAGE_DIR/

# Create a ZIP file with the Lambda function and dependencies
cd $PACKAGE_DIR
zip -r ../$ZIP_FILE .
cd ..

# Update the Lambda function code
aws lambda update-function-code --function-name authentication --zip-file fileb://$ZIP_FILE

# Clean up
rm -rf $VENV_DIR $PACKAGE_DIR $ZIP_FILE
