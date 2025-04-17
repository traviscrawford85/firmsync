from invoke import task
import subprocess
import os

@task
def auth_servers(c):
    subprocess.Popen("start cmd /k python -m firm_clio.auth.oauth_server", shell=True)
    subprocess.Popen("start cmd /k python -m firm_qbo.auth.oauth_server", shell=True)

@task
def clio_server(c):
    subprocess.Popen("powershell", "-NoExit", "-Command", "python -m firm_clio.auth.oauth_server")

@task
def qbo_server(c):
    subprocess.Popen("powershell", "-NoExit", "-Command", "python -m firm_qbo.auth.oauth_server")

@task  
def kill_servers(c):
    print("🛑 Killing Clio (5000) and QBO (3000) OAuth servers...")

    kill_ports = [5000, 3000]
    for port in kill_ports:
        cmd = f'''
        for /f "tokens=5" %%a in ('netstat -aon ^| findstr :{port}') do taskkill /F /PID %%a
        '''
        subprocess.call(cmd, shell=True)