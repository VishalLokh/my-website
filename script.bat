@echo off
:: Navigate to the local Git repository directory
cd C:\Coding\Website

:: Ensure you're in a Git repository
git status
IF ERRORLEVEL 1 (
  echo Not a git repository. Please check the folder.
  pause
  exit /b
)

:: Add all changes to Git
git add .

:: Commit the changes with a message
git commit -m "Automated commit and sync from script"

:: Push the changes to GitHub
git push origin main

:: Sync the local files to the S3 bucket
aws s3 sync . s3://vishal-lokhande.com --delete

:: Confirm sync success
echo Sync completed successfully.
pause
