from arquivo import*
tv= Televisor('Sony','Sony-123')

controle= ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)
