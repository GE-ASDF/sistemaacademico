from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as p
from time import sleep
import interface
import wmi
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
from connection import connection
from notify import notify

def reOpen():
    f = wmi.WMI()
    flag = 0
    for process in f.Win32_Process():
        if "sistemaAcademico.exe" == process.Name:
            print("Application is Running")
            flag = 1
            break
    if flag == 0:
        pathProgram = str(os.getcwd())+"sistemaAcademicoGrupoAnderson.exe"
        print(pathProgram)
        os.system(pathProgram)
        print("Application is not Running")


class Logar:

    def logar():
        user = ui.login.text()
        senha = ui.senha.text()
        found = connection.selectUser(CodigoContrato=user)
        notificar= notify()
        notificar.notificar(app_id="Sistema acadêmico", 
        title="Informação importante!", 
        msg="Aguarde enquanto buscamos suas informações no banco de dados.", 
        icon=os.getcwd()+"\\prepara-marca.png", duration="long").show()
        if(found):
            notificar.notificar(app_id="Sistema acadêmico", 
            title="Informação importante!", 
            msg="Parabéns! O processo de autenticação começará em alguns instantes. Aguarde...", 
            icon=os.getcwd()+"\\prepara-marca.png", duration="long").show()
            reOpen()
            Logar.logon(user, senha)
        else:
            p.alert("O usuário não foi encontrado. Tente novamente!", "Usuário não encontrado!")

    def logon(user, pwd):

        if user == user+"@prepara.com":
            user = user
        else:
            user = user+"@prepara.com"
        if user and pwd:
            MainWindow.close()
            chrome_service = ChromeService('chromedriver')
            chrome_service.creationflags = CREATE_NO_WINDOW
            navegador = webdriver.Chrome(service=chrome_service)
            navegador.get("https://portaldoaluno.prepara.com.br/login")
            navegador.maximize_window()
            while len(navegador.find_elements(By.ID, 'login')) < 1:
                sleep(1)
            login = navegador.find_element(By.ID, "login")
            login.click()
            login.send_keys(user)
            sleep(1)
            senha = navegador.find_element(By.ID, "senha")
            senha.click()
            senha.send_keys(pwd.capitalize())
            sleep(1)
            btnAcessar = navegador.find_element(By.ID, "btnAcessar")
            btnAcessar.click()
            while len(navegador.find_elements(By.ID, 'header')) < 1:
                sleep(1)
            while len(navegador.find_elements(By.ID, 'header')) >= 1:
                sleep(1)
            navegador.quit()
        else:
            p.alert("Não foi possível validar os dados")



if __name__ == "__main__":
        import sys
        app = interface.QtWidgets.QApplication(sys.argv)
        MainWindow = interface.QtWidgets.QMainWindow()
        ui = interface.Ui_Login()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.pushButton.clicked.connect(Logar.logar)
        ui.senha.returnPressed.connect(Logar.logar)
        sys.exit(app.exec_())

# reOpen()
