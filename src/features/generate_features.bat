echo off
title Generate features of tdwpDB
:: Runs all py files to generator features for analysis/inference.

echo Generating Features from ../../data/processed/..
echo ----------------------
echo Running Sales / Presales generator..
python generate_sales_features.py

echo ----------------------          
echo Running Stock generator..
python generate_stock_features.py

echo ----------------------
echo Running design generator..
python generate_design_features.py

echo ----------------------
echo ----------------------
echo Files in ../../data/processed/ ready to go!
pause