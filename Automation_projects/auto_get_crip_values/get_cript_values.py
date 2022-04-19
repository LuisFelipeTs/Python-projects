arq_cr_names = open('criptos_names.txt')
arq_cr_names_ap = arq_cr_names.readlines()

for i in range(len(arq_cr_names_ap)):
    arq_cr_names_ap[i] = str(arq_cr_names_ap[i]).replace('\n', '')
print(arq_cr_names_ap)

