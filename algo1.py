def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): 
  
 taxa_juros_diaria = taxa_juros_anual / 365 / 100 
  
 juros = valor_principal * taxa_juros_diaria * dias_atraso 
  
 valor_total = valor_principal + juros 
 return valor_total, juros 
valor_principal = 1000.00  
taxa_juros_anual = 5.0  
dias_atraso = 30  
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) 
print(f"Valor total a ser pago: R${valor_total}") 
print(f"Valor dos juros: R${juros:.2f}")
