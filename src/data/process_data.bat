echo off
title Clean and Aggregate Data
:: Runs all py files to clean and organize data files in data/raw

echo Processing Data in ../../data/raw/
echo ----------------------
echo Cleaning Summaries..
python clean_summaries.py
          
echo Cleaning presales..
python clean_presales.py

echo Aggregating Summaries together into sales/1.0..
python process_summaries.py

echo ----------------------
echo Cleaning Sales Reports..
python clean_sales_reports.py

echo Aggregating Sales Reports together into stock/1.0..
python -W ignore process_sales_reports.py

echo ----------------------
echo Cleaning PWD Dailies..
echo !-- edit bat file to clean older dailies --!
python clean_daily-PWD.py

echo ----------------------
echo Cleaning WRAABB Dailies..
echo !-- edit bat file to clean older dailies --!
python clean_daily-WRAABB.py

echo Aggregating dailies together into design/1.0..
python -W ignore process_daily.py

echo ----------------------
echo Files in ../../data/processed/ up to date.
pause