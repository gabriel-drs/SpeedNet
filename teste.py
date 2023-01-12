#Importando speedtest
import speedtest

#Função de teste
def main():
    speed = speedtest.Speedtest()
    download = f"{'{:.1f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.1f}'.format(speed.upload()/1024/1024)}"
