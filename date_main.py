import date_dif as dt

tipo_de_envio = input("como você quer enviar as datas? [console/arquivo]")

if tipo_de_envio == "console":
    dt.diferenca_date_console()
    print(dt.diferenca_date_console())

elif tipo_de_envio == "arquivo":
    dt.diferenca_date_arquivo()
    print(dt.diferenca_date_arquivo())



