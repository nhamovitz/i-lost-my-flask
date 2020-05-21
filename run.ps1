# Evidentally `&` is not the background-process indicator that it is on Linux; in Powershell, it's the "call operator" (https://stackoverflow.com/questions/2035193/how-to-run-a-powershell-script#comment14052749_2035209)
& (Join-Path $PSScriptPath "venv/Scripts/Activate.ps1")
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run