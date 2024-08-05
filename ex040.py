n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print ('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1,n2,m))
if m < 5:
    print('REPROVADO.')
    print('Na próxima, estude mais.')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO.')
    print('Você tem mais uma tentativa, estude mais um pouco.')
elif m >= 7:
    print('APROVADO!')
    print ('Parabéns! Você passou!')