distribuidora = [67836.43,36678.66,29229.88,27165.48,19849.53];

SOMA = sum(distribuidora);

for i in range(len(distribuidora)):
    valor = (distribuidora[i]*100) / SOMA;
    print(round(valor),"%");