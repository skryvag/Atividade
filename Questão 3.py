# python-questao3

 
nota1 = float(input('primeira nota: '))
 nota2= float(input('segunda nota: '))
  media = (nota1 + nota2 ) / 2; 
 
   print("tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média)) 
 
  if 7 > média >= 5:
  print('O aluno está em RECUPERAÇÃO.')
  elif média < 5:
  print('O aluno está REPROVADO.')
  elif média >= 7:
  print('O aluno está APROVADO.')
