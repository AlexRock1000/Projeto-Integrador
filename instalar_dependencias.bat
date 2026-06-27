@echo off
REM Desabilitar aliases de Python do Windows para este script
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths\python.exe" /v "Alias" /t REG_SZ /d "" /f >nul 2>&1

REM Procurar por Python instalado
python3.14 -m venv .venv
if errorlevel 1 (
    python3 -m venv .venv
)
if errorlevel 1 (
    echo Erro: Python nao encontrado!
    pause
    exit /b 1
)

REM Ativar o venv
call .venv\Scripts\activate.bat

REM Instalar dependências
pip install --upgrade pip setuptools wheel
pip install mysql-connector-python python-dotenv

echo.
echo Instalacao concluida!
echo Ativando o venv e testando a conexao...
call .venv\Scripts\activate.bat
python conexao.py

pause
