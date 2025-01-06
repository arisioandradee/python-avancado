# Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar #sem parenteses retorna o espaco na memoria


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')
print(falar_bom_dia('Arisio'))
print(falar_boa_noite('Arisio'))