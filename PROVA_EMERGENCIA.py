import pyautogui
pyautogui.sleep(5)


#FOGO DO MOTOR NO SOLO (PAGINA 01)
pyautogui.press('tab')
pyautogui.write('PROCEDIMENTO DE CORTE DO MOTOR EXECUTAR')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('CORTE DO OUTRO MOTOR EXECUTAR')
pyautogui.press('tab')
pyautogui.write('EVACUACAO DE EMERGENCIA INICIAR')
pyautogui.press('tab')
pyautogui.write('SOCORRO PELO RADIO SOLICITAR')
pyautogui.press('tab')
pyautogui.sleep(7)


#FALHA OU FOGO DO MOTOR NA DECOLAGEM (PAGINA 02)
pyautogui.press('tab')
pyautogui.write('MANETES DE POTENCIA REVERSO')
pyautogui.press('tab')
pyautogui.write('FREIOS APLICAR MAXIMO')
pyautogui.press('tab')
pyautogui.write('CONTROLE DIRECIONAL MANTER')
pyautogui.press('tab')
#AVIAO SEM PISTA SUFICIENTE PARA INICIAR PARADA
pyautogui.press('tab')
pyautogui.write('MANETE DE POTENCIA MINIMO')
pyautogui.press('tab')
pyautogui.write('MANETES DE COMBUSTIVEL CORTAR')
pyautogui.press('tab')
pyautogui.write('VALVULAS DE CORTE CORTAR')
pyautogui.press('tab')
pyautogui.write('INTERRUPTOR DE RECOLHIMENTO EM EMERGENCIA DO TREM EMERGENCIA')
pyautogui.press('tab')
pyautogui.write('TREM DE POUSO EM CIMA')
pyautogui.press('tab')
pyautogui.write('BATERIA DESLIGAR')
pyautogui.press('tab')
pyautogui.write('INTERRUPTOR MASTER DE AVIONICOS DESLIGAR')
pyautogui.press('tab')
#DECISAO DE CONTINUAR A DECOLAGEM
pyautogui.press('tab')
pyautogui.write('MANETE DE POTENCIA TORQUE MAXIMO PERMISSIVEL')
pyautogui.press('tab')
pyautogui.write('VELOCIDADE PARA DEIXAR O SOLO VR')
pyautogui.press('tab')
pyautogui.write('CONTROLE DIRECIONAL MANTER')
pyautogui.press('tab')
pyautogui.write('TREM DE POUSO EM CIMA')
pyautogui.press('tab')
pyautogui.write('VELOCIDADE ACELERAR PARA V2 (DEP FLAPE 0%) ou Vxse (DEP FLAPE 25%)')
pyautogui.press('tab')
#DEPOIS DE ATINGIR UMA CERTA ALTURA
pyautogui.press('tab')
pyautogui.write('FLAPE EM CIMA')
pyautogui.press('tab')
pyautogui.write('VELOCIDADE ACELERAR PARA VySE')
pyautogui.press('tab')
pyautogui.write('MOTOR AFETADO IDENTIFICAR E CORTAR')
pyautogui.press('tab')
pyautogui.write('EMBANDEIRAMENTO AUTOMATICO DESLIGAR')
pyautogui.press('tab')
pyautogui.write('BOMBA HIDRAULICA DE RECALQUE DESLIGAR')
pyautogui.press('tab')
pyautogui.sleep(7)


#FALHA OU FOGO DO MOTOR EM VOO (PAGINA 03)
pyautogui.write('CONTROLE DIRECIONAL MANTER')
pyautogui.press('tab')
pyautogui.write('PILOTO AUTOMATICO DESACOPLAR')
pyautogui.press('tab')
pyautogui.write('VELOCIDADE ACIMA DA VMC')
pyautogui.press('tab')
pyautogui.write('MANETES DE POTENCIA TORQUE MAXIMO PERMISSIVEL')
pyautogui.press('tab')
pyautogui.write('TREM DE POUSO E FLAPES CONVENIENTES')
pyautogui.press('tab')
pyautogui.write('MOTOR AFETADO IDENTIFICAR E CORTAR')
pyautogui.press('tab')
pyautogui.write('AR CONDICIONADO VENTILACAO OU DESLIGADO')
pyautogui.press('tab')
pyautogui.write('COMPENSACAO EFETUAR')
pyautogui.press('tab')
pyautogui.write('MANETE DE POTENCIA E VELOCIDADE CONVENIENTES')
pyautogui.press('tab')
pyautogui.sleep(7)


#REACENDIMENTO IMEDIATO (PAGINA 04)
pyautogui.write('NG OBSERVAR ACIMA DE 50%')
pyautogui.press('tab')
pyautogui.write('IGNICAO IGNICAO EM VOO')
pyautogui.press('tab')
pyautogui.write('MANETE DE POTENCIA MINIMO')
pyautogui.press('tab')
pyautogui.write('MANETE DE COMBUSTIVEL ALTO')
pyautogui.press('tab')
pyautogui.write('MANETE DE POTENCIA CONVENIENTE DEPOIS DO REACENDIMENTO')
pyautogui.press('tab')
pyautogui.write('IGNICAO CONVENIENTE')
pyautogui.press('tab')
pyautogui.sleep(7)

#DESPRENDIMENTO DO CAPÔ EM VOO (PAGINA 7)
pyautogui.write('PILOTO AUTOMATICO DESACOPLAR')
pyautogui.press('tab')
pyautogui.write('VELOCIDADE VMC +10%')
pyautogui.press('tab')
pyautogui.write('DIRECAO CONVENIENTE')
pyautogui.press('tab')
pyautogui.write('TREM DE POUSO EM CIMA')
pyautogui.press('tab')
pyautogui.write('FLAPE CONVENIENTE')
pyautogui.press('tab')
pyautogui.write('SINCRO-HELICE DESLIGAR')
pyautogui.press('tab')
pyautogui.write('MANETES DE HELICE 100% Nh')
pyautogui.press('tab')
pyautogui.write('MANETES DE POTENCIA CONVENIENTES')
pyautogui.press('tab')
pyautogui.write('AR CONDICIONADO VENTILACAO OU DESLIGADO')
pyautogui.press('tab')
pyautogui.write('COMPENSACAO EFETUAR')
pyautogui.press('tab')
pyautogui.write('MOTOR AFETADO IDENTIFICAR CONDICOES DO CAPO E APLICAR POTENCIA NECESSARIA')
pyautogui.press('tab')
pyautogui.sleep(7)

#CORTE DO MOTOR (PAGINA 8)
pyautogui.write('ALARME SONORO DE FOGO SILENCIAR (se aplicavel)')
pyautogui.press('tab')
pyautogui.write('SINCRO-HELICE DESLIGAR ')
pyautogui.press('tab')
pyautogui.write('MANETE DE POTENCIA MINIMO ')
pyautogui.press('tab')
pyautogui.write('MANETE DE HELICE BANDEIRA')
pyautogui.press('tab')
pyautogui.write('MANETE DE COMBUSTIVEL CORTAR ')
pyautogui.press('tab')
pyautogui.write('VALVULA DE CORTE DO MOTOR AFETADO CORTAR')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('EXTINTOR DESCARREGAR (SE APLICAVEL)')
pyautogui.press('tab')
pyautogui.write('LUZ V OBSERVAR ACESA (SE APLICAVEL)')
pyautogui.press('tab')
pyautogui.write('GERADOR DESLIGAR')
pyautogui.press('tab')
pyautogui.write('CARGA NO OUTRO GERADOR VERIFICAR DENTRO DOS LIMITES')
pyautogui.press('tab')
pyautogui.write('BOMBAS DE COMBUSTIVEL DO MOTOR AFETADO DESLIGAR')
pyautogui.press('tab')

