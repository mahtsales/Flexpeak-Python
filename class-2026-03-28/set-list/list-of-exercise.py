#criem uma lista com 5 saldos de conta corrente e ordene: maior saldo, menor saldo, media dos saldos, e o total dos saldos.
saldos = [1000.50, 2500.75, 500.00, 1500.25, 3000.00]
maior_saldo = max(saldos) # retorna o maior valor
menor_saldo = min(saldos) # retorna o menor valor
media_saldos = sum(saldos) / len(saldos) # retorna a media dos valores existentes
total_saldos = sum(saldos) # retorna o total dos valores
print(f"Maior saldo: R${maior_saldo:.2f}")
print(f"Menor saldo: R${menor_saldo:.2f}")
print(f"Média dos saldos: R${media_saldos:.2f}")
print(f"Total dos saldos: R${total_saldos:.2f}")
#OBS.: o ':.2f' gera as duas casas decimais após o ponto.
