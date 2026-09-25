# ==============================================================================
# CADERNO DE DESAFIOS - AULA 2: O PRIMEIRO DIA NA JWC
# ==============================================================================

# ==============================================================================
# DESAFIO 1: A Chegada ao Centro
# ==============================================================================
# Situação: Você finalmente chegou à sede da JWC, localizada no movimentado 
# centro do Rio de Janeiro. A Líder Técnica, Patrícia, 
# te recebe na porta com um sorriso e pede para você testar o terminal do saguão.
# Missão: Use a função print() para exibir a mensagem: "Cheguei na JWC!"

# print("Cheguei na JWC!")

# ==============================================================================
# DESAFIO 2: O Crachá de Visitante
# ==============================================================================
# Situação: A recepcionista precisa gerar o seu crachá temporário para o 
# processo seletivo da vaga de Programador Full Stack.
# Missão: Crie uma variável descritiva 'nome_candidato' e guarde o seu nome nela. 
# Depois, crie uma variável 'idade_candidato'. Imprima as duas variáveis na tela.

# Código:

nome_candidato = "Cheyenne Querino"
idade_candidato = 34

# print (nome_candidato)
# print (idade_candidato)

# ==============================================================================
# DESAFIO 3: Conhecendo a Estrutura
# ==============================================================================
# Situação: No elevador, Patrícia te conta que a empresa tem 30 colaboradores na 
# área administrativa e 20 na equipe de desenvolvimento. 
# Missão: Crie a variável 'total_colaboradores_administrativos' valendo 30 e a 
# variável 'total_colaboradores_desenvolvimento' valendo 20. Crie uma terceira 
# variável chamada 'total_geral_funcionarios' que some as duas e imprima o resultado!

# Código:
total_colaboradores_administrativos = 30
total_colaboradores_desenvolvimento = 20

total_geral_funcionarios = total_colaboradores_administrativos + total_colaboradores_desenvolvimento


# print (total_geral_funcionarios) 


# ==============================================================================
# DESAFIO 4: O Boom da Educação
# ==============================================================================
# Situação: Durante a pandemia, a JWC cresceu muito atendendo um setor específico: 
# o da educação. 
# Missão: Crie uma constante (tudo em maiúsculo) chamada 'SETOR_MERCADO_PRINCIPAL' 
# e guarde nela a palavra "Educação". Imprima uma frase usando essa constante.

# Código:
SETOR_MERCADO_PRINCIPAL = "Educação"
# print ("Um dos setores que recebe mais investimento é o da " + SETOR_MERCADO_PRINCIPAL)


# ==============================================================================
# DESAFIO 5: O Armário do RH
# ==============================================================================
# Situação: O pessoal do RH te explica que eles organizam os dados dos candidatos 
# como se fosse a "arrumação de um armário". As gavetas com cadeado são 
# as Constantes, e as caixas abertas são as Variáveis.
# Missão: Crie uma constante 'NOME_EMPRESA' valendo "JWC". Crie uma variável 
# 'status_atual_candidato' valendo "Em teste". Imprima ambas.

# Código:
NOME_EMPRESA = "JWC"
status_atual_candidato = "Em teste"

# print (NOME_EMPRESA)
# print (status_atual_candidato) 

# ==============================================================================
# DESAFIO 6: Conversa no Cafezinho
# ==============================================================================
# Situação: Na copa da empresa, um desenvolvedor sênior quer puxar assunto com você.
# Missão: Use a função input() para perguntar: "Qual é a sua linguagem de 
# programação favorita?". Guarde a resposta numa variável chamada 'linguagem_favorita' 
# e depois imprima essa resposta.

# Código:

# linguagem_favorita = input ("Qual é sua linguagem de programação favorita?") 

# print (linguagem_favorita)



# ==============================================================================
# DESAFIO 7: O Formulário de Transporte
# ==============================================================================
# Situação: O RH precisa saber como você vai se deslocar até o centro do Rio de Janeiro 
# todos os dias, caso seja contratado.
# Missão: Use o input() para perguntar qual meio de transporte você utiliza. 
# Salve na variável 'meio_transporte_utilizado' e exiba na tela formatado.

# Código:
# meio_transporte_utilizado = input ("Qual meio de transporte você utiliza?")
# print (meio_transporte_utilizado)


# ==============================================================================
# DESAFIO 8: Mudança de Planos
# ==============================================================================
# Situação: Você estava concorrendo para uma posição inicial, mas o diretor viu seu 
# potencial e te alocou para a vaga de "Programador Full Stack"!
# Missão: Crie a variável 'cargo_pretendido_candidato' valendo "Estágio". Imprima. 
# Na linha de baixo, atualize o valor da MESMA variável para "Full Stack" e imprima novamente.

# Código:

# cargo_pretendido_candidato = "Estágio"
# print (cargo_pretendido_candidato)
# cargo_pretendido_candidato = "Full Stack"
# print (cargo_pretendido_candidato)

# ==============================================================================
# DESAFIO 9: Avaliação de Perfil
# ==============================================================================
# Situação: A JWC busca pessoas "curiosas, ágeis e inovadoras". 
# Missão: Crie três variáveis descritivas do tipo booleano (True ou False): 
# 'possui_perfil_curioso', 'possui_perfil_agil' e 'possui_perfil_inovador'. 
# Atribua True para todas e imprima-as.

# Código:
# possui_perfil_curioso = True
# possui_perfil_agil = True
# possui_perfil_inovador = True

# print (possui_perfil_agil, possui_perfil_agil, possui_perfil_inovador)

# ==============================================================================
# DESAFIO 10: O Grito do Diretor
# ==============================================================================
# Situação: O diretor da JWC adora avisos em letras MAIÚSCULAS no mural da empresa.
# Missão: Crie uma variável 'mensagem_aviso_mural' com o texto "bem-vindos novos talentos". 
# Use o método .upper() no print para exibir a frase toda em letras maiúsculas.

# Código:
mensagem_aviso_mural = "Bem-vindo novos talentos!"
print (mensagem_aviso_mural.upper())

# ==============================================================================
# DESAFIO 11: A Senha de Acesso
# ==============================================================================
# Situação: Você pediu a senha temporária de rede, mas a equipe de segurança 
# informou que senhas seguras precisam ser medidas em tamanho.
# Missão: Crie a variável 'senha_temporaria_rede' com um valor de texto. Use a 
# função len() dentro do print para contar e exibir quantos caracteres essa senha possui.

# Código:
# senha_temporaria_rede = "senha123"
# print (len (senha_temporaria_rede))

# ==============================================================================
# DESAFIO 12: Juntando os Pedaços
# ==============================================================================
# Situação: O banco de dados da empresa separa o primeiro nome do sobrenome.
# Missão: Crie a variável 'primeiro_nome' e a variável 'sobrenome_candidato'. 
# Depois, crie uma terceira variável chamada 'nome_completo_formatado' que junte 
# as duas com um espaço no meio. Imprima o resultado.

# Código:
# primeiro_nome = "Cheyenne"
# sobrenome_candidato = "Querino"
# nome_completo_formatado = (primeiro_nome  + " " + sobrenome_candidato)
# print (nome_completo_formatado) 

# ==============================================================================
# DESAFIO 13: Cálculo do Benefício
# ==============================================================================
# Situação: Todo novo funcionário ganha um auxílio inicial para ferramentas de estudo.
# Missão: Crie uma variável 'valor_salario_base' valendo 2000 e uma variável 
# 'valor_auxilio_ferramentas' valendo 150. Imprima a soma das duas variáveis usando 
# uma variável de resultado chamada 'total_remuneracao_inicial'.

# Código:
# valor_salario_base = 2000
# valor_auxilio_ferramentas = 150
# total_remuneracao_inicial = (valor_salario_base + valor_auxilio_ferramentas)

# print (total_remuneracao_inicial)

# ==============================================================================
# DESAFIO 14: O Bug do Código
# ==============================================================================
# Situação: Um colega da equipe de desenvolvimento tentou criar uma mensagem, mas 
# esqueceu de estruturar o texto corretamente e o código quebrou!
# Missão: Conserte o código abaixo para que ele funcione sem erros de sintaxe.
# texto_informativo = Alerta do sistema interno da JWC
# print(texto_informativo)

# Código (escreva a versão corrigida aqui):
# texto_informativo = "Alerta do sistema interno da JWC"
# print  (texto_informativo)

# ==============================================================================
# DESAFIO 15: O Relatório de Fim de Dia (Projeto Final da Aula)
# ==============================================================================
# Situação: O seu primeiro dia de testes práticos na JWC chegou ao fim! Para registrar 
# seu progresso, você precisa gerar um relatório automatizado.
# Missão: Use 'inputs' para coletar: 'nome_colaborador_input', 'idade_colaborador_input' 
# e 'pontuacao_teste_pratico'. Depois, exiba um print formatado (f-string) unindo 
# todas essas informações em uma frase clara para o recrutador.

# Código:

# nome_colaborador_input = input ("Qual o nome do colaborador?")
# idade_colaborador_input =  input ("Qual idade do colaborador?")
# pontuacao_teste_pratico = input ("Qual é pontuação do teste prático?")

# print (f"Nome: {nome_colaborador_input}, Idade: {idade_colaborador_input}, Pontuação: {pontuacao_teste_pratico}")


# ==============================================================================
# CADERNO DE DESAFIOS - AULA 2: O PRIMEIRO DIA NA JWC - revisão
# ==============================================================================
# CONCEITO GERAL: Nesta aula, vamos aprender os fundamentos da comunicação com o 
# computador. Vamos ensiná-lo a falar (print), a escutar (input) e a guardar 
# informações na memória usando caixinhas chamadas "variáveis".

# ==============================================================================
# DESAFIO 1: A Chegada ao Centro
# ==============================================================================
# CONCEITO: A função 'print()' é a "boca" do computador. É como mandamos ele 
# escrever algo na tela. Tudo que for TEXTO deve estar sempre entre aspas ("").

# EXPLICAÇÃO: O computador vai ler isso e mostrar exatamente a frase na tela.

# ==============================================================================
# DESAFIO 2: O Crachá de Visitante
# ==============================================================================
# CONCEITO: Uma "variável" é como uma caixa organizadora com uma etiqueta.
# Nós damos um nome a ela (a etiqueta) e guardamos uma informação lá dentro.

# Criamos a caixa 'nome_candidato' e guardamos o texto "Caio Barbosa".

# Criamos a caixa 'idade_candidato' e guardamos o número 50 (números não usam aspas!).

# Agora pedimos para o computador mostrar o que tem DENTRO das caixas.


# ==============================================================================
# DESAFIO 3: Conhecendo a Estrutura
# ==============================================================================
# CONCEITO: O computador é ótimo com matemática. Podemos fazer contas usando as 
# nossas caixas (variáveis) em vez de usar os números diretamente.



# Aqui criamos uma terceira caixa que vai guardar o resultado da SOMA (+) das outras duas.


# ==============================================================================
# DESAFIO 4: O Boom da Educação
# ==============================================================================
# CONCEITO: Quando queremos criar uma caixa cujo valor NUNCA deve ser alterado, 
# nós a chamamos de "Constante". Por convenção (um acordo entre programadores),
# escrevemos o nome dela todo em MAIÚSCULAS para avisar: "Não mexa aqui!".

# PI = 3.14
# print (PI)

# O sinal de mais (+) quando usado com textos serve para "colar" (concatenar) um no outro.

# ==============================================================================
# DESAFIO 5: O Armário do RH
# ==============================================================================
# CONCEITO: Fixando a diferença visual. MAIÚSCULAS para coisas fixas (Constantes),
# minúsculas para coisas que podem mudar ao longo do tempo (Variáveis).




# ==============================================================================
# DESAFIO 6: Conversa no Cafezinho
# ==============================================================================
# CONCEITO: A função 'input()' é o "ouvido" do computador. Ela faz o programa pausar,
# faz uma pergunta na tela e espera o usuário digitar uma resposta no teclado.

# A resposta que o usuário digitar será guardada na caixa 'linguagem_favorita'.

# Depois, o computador mostra o que ele acabou de escutar e guardar.
# linguagem_favorita = input ("Qual sua linguagem favorita?")
# print (linguagem_favorita)

# ==============================================================================
# DESAFIO 7: O Formulário de Transporte
# ==============================================================================
# CONCEITO: Praticando a coleta de dados (input). Todo sistema precisa receber 
# dados de alguém (do teclado, do mouse, da tela do celular).

# nome_do_usuário = input ("Qual seu nome?")
# meio_de_transporte = input ("Qual meio de transporte utiliza?") 
# numero_de_passagens_dia = input ("Quantas passagens usa ao todo no dia?") 

# print ("Nome: " + nome_do_usuário) 
# print ("Meio de Transporte: " + meio_de_transporte)
# print ("Número de Passagens por Dia: " + numero_de_passagens_dia) 

# ==============================================================================
# DESAFIO 8: Mudança de Planos
# ==============================================================================
# CONCEITO: Por que se chama "Variável"? Porque o valor pode VARIAR! 
# Se você colocar algo novo em uma caixa que já estava cheia, o conteúdo antigo 
# é jogado fora e substituído pelo novo.

# A caixa recebe o valor "Estágio".
# nome = "Cheyenne"
# print (nome)
# nome = "Christine"
# print (nome)

# A MESMA caixa agora recebe o valor "Full Stack". O "Estágio" sumiu para sempre.


# ==============================================================================
# DESAFIO 9: Avaliação de Perfil
# ==============================================================================
# CONCEITO: "Booleanos" (True ou False) são como interruptores de luz: Ligado ou Desligado,
# Sim ou Não, Verdadeiro ou Falso. 
# Importante: Em Python, eles PRECISAM começar com letra maiúscula (True / False) e não usam aspas.

# amanda_is_admin = True



# ==============================================================================
# DESAFIO 10: O Grito do Diretor
# ==============================================================================
# CONCEITO: Textos em Python possuem "ferramentas" embutidas chamadas de "métodos".
# O método '.upper()' (do inglês "upper case" = letra maiúscula) pega qualquer 
# texto minúsculo e transforma em maiúsculo na hora de exibir.

# senha  = "123"
# print (len (senha))



# ''==============================================================================
# DESAFIO 11: A Senha de Acesso
# ==============================================================================
# CONCEITO: A função 'len()' vem da palavra "length" (comprimento/tamanho em inglês).
# Ela serve para o computador contar quantos caracteres (letras, números, espaços) 
# existem dentro de um texto.



# A senha tem a palavra "senha" (5 letras) + "123" (3 números) = 8 caracteres.

# conta = 5 + 5 #somar
# print (conta)
# letras = "5" + "5" #concatenar
# print (letras)


# ==============================================================================
# DESAFIO 12: Juntando os Pedaços
# ==============================================================================
# CONCEITO: Ao "colar" (concatenar) variáveis de texto usando o sinal de mais (+), 
# o computador junta tudo exatamente do jeito que está. Se você não colocar um 
# espaço manualmente (" "), as palavras ficarão grudadas ("ArthurSilva").


# Juntando: "Arthur" + " " (espaço vazio) + "Silva" = "Arthur Silva"

# print ("Cheyenne" +" "+ "Christine")


# ==============================================================================
# DESAFIO 13: Cálculo do Benefício
# ==============================================================================
# CONCEITO: O sinal de mais (+) é inteligente. 
# - Se as variáveis forem TEXTOS (com aspas), ele junta as palavras.
# - Se as variáveis forem NÚMEROS (sem aspas), ele faz a conta de matemática (soma).


# Aqui ele entende que é matemática, então 2000 + 150 vira 2150.


# ==============================================================================
# DESAFIO 14: O Bug do Código
# ==============================================================================
# CONCEITO: O computador é burro e obedece regras estritas. Texto SEMPRE precisa 
# de aspas (duplas "" ou simples ''). Se você não colocar, o computador acha que as 
# palavras são comandos ou variáveis que não existem, causando um "Erro de Sintaxe".

# CORREÇÃO: O texto informativo precisa estar envolto em aspas.


# ==============================================================================
# DESAFIO 15: O Relatório de Fim de Dia (Projeto Final da Aula)
# ==============================================================================
# CONCEITO: Aqui juntamos tudo o que aprendemos e introduzimos a 'f-string'.
# Colocar um 'f' minúsculo antes das aspas de um print (f"...") permite "injetar" 
# as nossas caixinhas (variáveis) diretamente no meio do texto, apenas colocando-as 
# entre chaves { }. É muito mais fácil do que usar o símbolo de mais (+).



# EXPLICAÇÃO: Em vez de fazer print("Nome: " + nome + ", Idade: " + idade...), 
# usamos a formatação 'f-string' para deixar o código limpo e elegante!

# nome = "Cheyenne"
# idade = "34"
# print (f"O nome é {nome} e a idade é {idade}")

