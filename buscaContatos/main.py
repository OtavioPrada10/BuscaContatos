import PySimpleGUI as sg
import webbrowser
from buscaContatos import BuscaContatos

"""
Site de consulta cpf https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp
"""

sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Facilitador de pesquisa de Contas', size = 30)],
            [sg.Text('nome da empresa', size = 14), sg.InputText(key='nomeEmpresa')],
            [sg.Text('Cargo',           size = 14), sg.InputText(key='cargo')],
            [sg.Text('Cidade' ,         size = 14), sg.InputText(key='cidade')],
            [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Facilitador', layout)
inicio = 0
while True:
    if inicio == 0:
        inicio = 1
        Contato = BuscaContatos()
        Contato.abrirSite()

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if(event == 'Ok'):
       sNomeEmpresa = values['nomeEmpresa']
       sCargo = values['cargo']
       sCidade = values['cidade']

       if sNomeEmpresa != False and sNomeEmpresa != '':
            Contato.buscaEmpresa(sNomeEmpresa, sCargo, sCidade)
            break

        

window.close()
