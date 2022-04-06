def ifood(kind, *arguments, **keywords):
  print("Ana: Olá, eu gostaria de pedir um", kind, "por favor?")
  print("Atendente virtual: OK! Só vou registrar o pedido do ", kind, "! Aguarde, por favor!", sep='')
  for arg in arguments:
    print(arg)
  print("-" * 40)
  keys = sorted(keywords.keys())
  for kw in keys:
    print(kw, ":", keywords[kw])
  print("-" * 40)

ifood("cachorro-quente", "Atendente virtual: Seu pedido está sendo processado...",
"Atendente virtual: Seu pedido está registrado, Ana!",
"Ana: Muito obrigada :) !!!",
Restaurante='Cachorrão do H8',
Cliente="Ana",
Tempo_para_entrega="2 horas",
Lugar_de_entrega="Prédio da COMP")