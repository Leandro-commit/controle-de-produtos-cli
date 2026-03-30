# 1. Configuramos os dados fixos
original_leite = 3.40
padarias = [
    "Maffile",
    "Minaslandia debaixo",
    "Minaslandia de cima",
    "Flor de maio",
    "Padaria Pão do dia",
    "Padaria Laura",
    "Padaria Monteiros",
    "Padaria do Moreira",
    "Padaria monalisa",
    "Padaria do Jaja",
    "Padaria General",
    "República dos pães",
    "Padaria alberto",
    "Chinelão",
]

lucro_total_dia = 0

# 2. Usamos um loop para repetir a lógica automaticamente
for nome in padarias:
    print(f"\n--- {nome} ---")

    # Entrada de dados com tratamento simples de vírgula
    litros = int(input(f"Quantos litros para {nome}? "))
    valor_venda = float(input("Valor de venda? ").replace(",", "."))

    # Cálculos
    lucro_por_litro = valor_venda - original_leite
    lucro_padaria = lucro_por_litro * litros
    lucro_total_dia += lucro_padaria  # Vai somando o total do dia

    # Exibição formatada
    print(f"Lucro nesta padaria: R$ {lucro_padaria:.2f}".replace(".", ","))

print("\n" + "=" * 30)
print(f"LUCRO TOTAL DO DIA: R$ {lucro_total_dia:.2f}".replace(".", ","))
print("=" * 30)
