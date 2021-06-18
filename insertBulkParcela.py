#!/usr/bin/env python
import pandas as pd
import sqlalchemy
import csv
import os

def using_pandas(csv_file,table_name, uri):
    df = pd.read_csv(csv_file,sep = ';')
    df.to_sql(table_name, con=uri, if_exists='append', index=False)



uri = 'mysql+pymysql://root:fiap2021@ec2-3-15-69-11.us-east-2.compute.amazonaws.com:3306/Cyrela'

#print("Posicao financeira")
#using_pandas('Dados_Tabela_PosicaoFinanceira.csv','PosicaoFinanceira', uri)

#print("Log Navegacao")
#using_pandas('Dados_Tabela_LogNavegacao.csv','log_navegacao', uri)


#print("Controle sessao")
#using_pandas('Dados_Tabela_Controlesessao.csv','ControleSessao', uri)


#print("Clientes")
#using_pandas('Dados_Tabela_Clientes.csv','Coobrigado', uri)


#print("Parcela")
#using_pandas('Dados_Tabela_Parcelas.csv','Parcela', uri)

print("DIM_Empreendimento")
using_pandas('dim_empreendimento.csv','DIM_Empreendimento',uri)
print("Fim")
