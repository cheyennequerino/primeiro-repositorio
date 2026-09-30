# ==============================================================================
# CADERNO DE DESAFIOS - AULA 3: GIT E EXPRESSÕES ARITMÉTICAS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# ==============================================================================

# ==============================================================================
# DESAFIO 1: O Onboarding com a Tech Lead (O Mundo do GIT)
# ==============================================================================
# Situação: No seu primeiro dia focado em código, a Patrícia (Líder Técnica) 
# avisa que não aceita código perdido. Antes de você programar a regra de 
# negócio do cliente, ela quer garantir que você entende de versionamento.
# Enunciado: Faça uma breve pesquisa e responda (usando a função print):
# A) Quem criou o Git e o GitHub?[cite: 2]
# B) Para qual empresa o GitHub foi vendido e por qual valor aproximado?[cite: 2]
# C) Cite o nome de pelo menos dois outros subversionadores (concorrentes do GitHub) 
#    usados no mercado.[cite: 2]

# Código:




# ==============================================================================
# DESAFIO 2: O Padrão da Empresa (Comandos GIT)
# ==============================================================================
# Situação: A Patrícia criou um manual de boas práticas da JWC. Todo desenvolvedor 
# precisa saber o fluxo básico para salvar o código na nuvem e evitar desastres. 
# Enunciado: Sem usar código Python, escreva dentro de prints quais são os 
# comandos do GIT responsáveis por:
# 1. Iniciar um novo repositório local na sua máquina.[cite: 2]
# 2. Verificar o estado atual dos arquivos (o que foi alterado).[cite: 2]
# 3. Adicionar arquivos para a "área de preparação" para serem salvos.[cite: 2]
# 4. Salvar as alterações criando um ponto na história (com uma mensagem).[cite: 2]

# Código:


# ==============================================================================
# DESAFIO 3: A Primeira Feature (Operador de Subtração -)
# ==============================================================================
# Situação: O Arthur (Product Owner) chegou com uma demanda de um cliente da 
# área de educação[cite: 2]. O sistema precisa mostrar no painel da diretoria 
# quantas vagas ainda estão disponíveis na escola.
# Enunciado: Como desenvolvedor, crie uma variável 'capacidade_total_escola' 
# valendo 850. Crie 'alunos_matriculados' valendo 523. O sistema deve calcular 
# a variável 'vagas_disponiveis' subtraindo os matriculados da capacidade total. 
# Imprima o resultado na tela.

# Código:


# ==============================================================================
# DESAFIO 4: Calculando o Faturamento (Operador de Multiplicação *)
# ==============================================================================
# Situação: O Arthur (PO) pediu para você criar a funcionalidade que projeta o 
# faturamento do mês seguinte, multiplicando o número de alunos pela mensalidade.
# Enunciado: Crie a variável 'mensalidade_padrao' valendo 850.50. Crie a variável 
# 'novas_matriculas' valendo 42. Crie a variável 'faturamento_projetado' que 
# multiplique os dois valores e exiba o resultado para o cliente.

# Código:
# mensalidade_padrao = 850.50
# novas_matriculas = 42
# faturamento_projetado = (mensalidade_padrao * novas_matriculas)

# print (faturamento_projetado)

# ==============================================================================
# DESAFIO 5: Divisão de Turmas (Operador de Divisão /)
# ==============================================================================
# Situação: O sistema precisa de um botão "Gerar Grupos de Estudo". O Arthur (PO) 
# definiu que a regra de negócio é dividir o total de alunos de uma turma pelo 
# tamanho ideal do grupo.
# Enunciado: Crie 'total_alunos_turma' valendo 45. Crie 'tamanho_grupo_ideal' 
# valendo 5. Calcule e imprima quantos grupos serão formados usando a divisão (/).
# (Note que no Python, a divisão normal sempre retorna um número quebrado - float).

# Código:
# total_alunos_turma = 45
# tamanho_grupo_ideal = 5
# resultado_divisao_dos_grupos = total_alunos_turma / tamanho_grupo_ideal

# print (f"O resultado é: {resultado_divisao_dos_grupos}")




# ==============================================================================
# DESAFIO 6: Lógica de Paginação (Divisão Inteira // e Resto %)
# ==============================================================================
# Situação: O cliente educacional comprou 100 tablets. O sistema precisa 
# distribuir esses tablets igualmente entre 3 salas, mas a Patrícia (Tech Lead) 
# avisa: "O sistema não pode quebrar um tablet no meio!".
# Enunciado: Você precisa usar a divisão inteira (//) para descobrir quantos 
# tablets inteiros vão para cada sala. Depois, use o resto da divisão (%) para 
# programar a variável 'tablets_sobra' e avisar quantos ficam na reserva da TI. 
# Imprima ambos os resultados.

# Código:
# total_tablets = 100
# divisao_tablets_sala = 3

# #DIVISÃO 
# tablets_divisao = total_tablets // divisao_tablets_sala
# print (f"O resultado da divisão é: {tablets_divisao}")

# #RESTO
# tablets_sobra = (total_tablets % divisao_tablets_sala)
# print (f"O resto da divisão é: {tablets_sobra}")

# ==============================================================================
# DESAFIO 7: Escalabilidade de Servidor (Exponenciação **)
# ==============================================================================
# Situação: A Patrícia (Tech Lead) precisa configurar os servidores da AWS para 
# suportar o novo sistema educacional. Ela sabe que a base de dados dobra de 
# tamanho a cada ano.
# Enunciado: Crie a variável 'armazenamento_atual_tb' valendo 3. Como o volume 
# dobra anualmente, calcule o tamanho necessário para daqui a 4 anos elevando 
# 2 à 4ª potência (**). Multiplique o resultado pelo armazenamento atual e imprima.

# Código:
# armazenamento_atual_tb = 3
# resultado = 2**4
# print (resultado*armazenamento_atual_tb)




# ==============================================================================
# DESAFIO 8: O MVP do Boletim Digital (Projeto Final da Aula 3)
# ==============================================================================
# Situação: Sprint final! O Arthur (PO) precisa apresentar o Produto Mínimo 
# Viável (MVP) funcionando. A funcionalidade principal é o cálculo da média 
# do aluno pelo professor[cite: 2].
# Regra da Patrícia: "O sistema não pode ter valores fixos. O usuário (professor) 
# é quem deve digitar os dados no terminal."
# Enunciado: 
# 1. Use input() para capturar o nome do aluno.
# 2. Use input() para capturar as notas do 1º, 2º e 3º trimestre (lembre-se 
#    de aplicar a conversão float() para que o Python entenda como matemática).
# 3. Calcule a média somando as 3 notas e dividindo por 3. (Cuidado com a 
#    ordem de precedência matemática: use parênteses!).
# 4. Exiba o resultado formatado (f-string) na tela para o professor: 
#    "Sistema JWC: O aluno [nome] fechou o ano com média [media]".

# nome_aluno = input("Qual o nome do Aluno(a)? ")
# primeira_nota = float(input("Qual a primeira nota? "))
# segunda_nota = float(input("Qual a segunda nota? "))
# terceira_nota = float(input("Qual a terceira nota? "))

# media_das_notas = (primeira_nota + segunda_nota + terceira_nota) / 3
# print (media_das_notas)



# Código:

# ==============================================================================
# CADERNO DE DESAFIOS - AULA 3: GIT E EXPRESSÕES ARITMÉTICAS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# ==============================================================================
# CONCEITO GERAL: Nesta aula, o foco é entender a diferença entre Git e GitHub,
# aprender os comandos básicos de versionamento no próprio computador e, por fim, 
# usar o Python como uma calculadora poderosa para resolver problemas do dia a dia.

# ==============================================================================
# DESAFIO 1: O Onboarding com a Tech Lead (O Mundo do GIT)
# ==============================================================================
# CONCEITO: Existe uma grande confusão entre "Git" e "GitHub". 
# - O Git é o "programa" que você instala no seu computador. Ele gerencia as 
#   versões do seu projeto (como uma máquina do tempo dos seus arquivos).
# - O GitHub é o "site" (a nuvem) onde você publica e compartilha esses arquivos
#   para trabalhar em equipe (como se fosse uma rede social para programadores).

# print("A) O Git foi criado por Linus Torvalds. O GitHub foi criado por Tom Preston-Werner, Chris Wanstrath e P. J. Hyett, com Scott Chacon também entre os primeiros integrantes.")
# print("B) O GitHub foi vendido para a Microsoft em 2018 por aproximadamente US$ 7,5 bilhões.")
# print("C) Dois concorrentes do GitHub são GitLab e Bitbucket.")
# EXPLICAÇÃO: GitLab e Bitbucket são como "canais de TV diferentes". Eles fazem
# o mesmo serviço que o GitHub (guardar código na internet), mas são de outras empresas.

# ==============================================================================
# DESAFIO 2: O Padrão da Empresa (Comandos GIT)
# ==============================================================================
# CONCEITO: Como a gente salva o nosso trabalho usando o Git no nosso computador?
# Imagine que você está empacotando coisas para uma mudança.

# print("1. Iniciar um novo repositório local: git init")
# # EXPLICAÇÃO: 'init' (iniciar). É como pegar uma caixa de papelão vazia e dizer: 
# # "Vou começar a guardar meu projeto aqui dentro".

# print("2. Verificar o estado atual dos arquivos: git status")
# # EXPLICAÇÃO: 'status'. É olhar para a caixa e ver o que está dentro, o que foi 
# # modificado e o que ainda está fora da caixa.

# print("3. Adicionar arquivos à área de preparação: git add .")
# # EXPLICAÇÃO: 'add .' (o ponto significa 'tudo'). É você pegar todos os arquivos 
# # novos ou modificados e colocá-los dentro da caixa.

# print("4. Salvar as alterações com uma mensagem: git commit -m 'mensagem'")
# # EXPLICAÇÃO: 'commit'. É você passar a fita adesiva na caixa, fechar e colar uma 
# # etiqueta (a mensagem) dizendo: "Aqui dentro estão as alterações do dia 21".

# ==============================================================================
# DESAFIO 3: A Primeira Feature (Operador de Subtração -)
# ==============================================================================
# CONCEITO: O Python funciona como uma calculadora. Aqui usamos o símbolo de 
# menos (-) para fazer contas de subtração.

# capacidade_total_escola = 850
# alunos_matriculados = 523

# # O computador pega o número 850, subtrai 523, e guarda o resultado (327) 
# # dentro de uma nova caixa (variável) chamada 'vagas_disponiveis'.
# vagas_disponiveis = capacidade_total_escola - alunos_matriculados

# print("Vagas disponíveis:", vagas_disponiveis)

# ==============================================================================
# DESAFIO 4: Calculando o Faturamento (Operador de Multiplicação *)
# ==============================================================================
# CONCEITO: No mundo da programação, não usamos o "x" para multiplicar, 
# usamos o asterisco (*).

# mensalidade_padrao = 850.50 # Números quebrados (decimais) usam ponto, não vírgula!
# novas_matriculas = 42

# faturamento_projetado = mensalidade_padrao * novas_matriculas

# print("Faturamento projetado:", faturamento_projetado)

# ==============================================================================
# # DESAFIO 5: Divisão de Turmas (Operador de Divisão /)
# # ==============================================================================
# # CONCEITO: Para dividir, usamos a barra (/). 
# # Um detalhe: a divisão normal (/) sempre entrega um número decimal (mesmo que 
# # a divisão seja exata, como 10 / 2, o computador mostra 5.0).

# total_alunos_turma = 45
# tamanho_grupo_ideal = 5

# grupos_formados = total_alunos_turma / tamanho_grupo_ideal

# print("Grupos formados:", grupos_formados)

# # ==============================================================================
# # DESAFIO 6: Lógica de Paginação (Divisão Inteira // e Resto %)
# # ==============================================================================
# # CONCEITO: E se precisarmos dividir coisas que não podem ser cortadas ao meio?
# # Não podemos ter "33.3 tablets" em uma sala. Precisamos de números inteiros!

# total_tablets = 100
# total_salas = 3

# # O operador // (duas barras) faz a "Divisão Inteira". 
# # Ele ignora os decimais. Ele responde: "Quantos grupos inteiros cabem?" (Neste caso, 33).
# tablets_por_sala = total_tablets // total_salas

# # O operador % (sinal de porcentagem) não significa porcentagem aqui! 
# # Na programação, ele é o "Módulo" ou "Resto da divisão". 
# # Ele responde: "Se eu dividir 100 por 3 e der 33 pra cada, quantos sobram?" (Sobra 1).
# tablets_sobra = total_tablets % total_salas

# print("Tablets inteiros por sala:", tablets_por_sala)
# print("Tablets que ficarão na reserva da TI:", tablets_sobra)

# # ==============================================================================
# # DESAFIO 7: Escalabilidade de Servidor (Exponenciação **)
# # ==============================================================================
# # CONCEITO: Como fazemos contas de "elevado a" (potência)? Usamos dois asteriscos (**).
# # E assim como na matemática da escola, o que está entre parênteses () é resolvido primeiro.

# armazenamento_atual_tb = 3

# # Aqui o computador resolve (2 ** 4) primeiro, ou seja, 2 elevado à 4ª potência (2*2*2*2 = 16).
# # Depois, ele multiplica o resultado por 3 (16 * 3 = 48).
# armazenamento_futuro_tb = armazenamento_atual_tb * (2 ** 4)

# print("Armazenamento necessário daqui a 4 anos:", armazenamento_futuro_tb, "TB")

# # ==============================================================================
# # DESAFIO 8: O MVP do Boletim Digital (Projeto Final da Aula 3)
# # ==============================================================================
# # CONCEITO: Aqui juntamos tudo e deixamos o programa interativo!

# # 'input()' faz o computador parar e esperar o usuário digitar alguma coisa.
# # O que o usuário digitar será guardado na caixa 'nome_aluno'.
# nome_aluno = input("Digite o nome do aluno: ")

# # O comando 'float()' transforma o texto que o usuário digitou em um "Número Decimal".
# # Se não fizermos isso, o computador acha que o número é só um texto e não consegue somar.
# nota1 = float(input("Digite a nota do 1º trimestre: "))
# nota2 = float(input("Digite a nota do 2º trimestre: "))
# nota3 = float(input("Digite a nota do 3º trimestre: "))

# # Primeiro ele soma as notas (porque estão entre parênteses) e depois divide por 3.
# media = (nota1 + nota2 + nota3) / 3

# # EXPLICAÇÃO FINAL: O 'f' antes das aspas (f"Sistema...") significa "Formatação".
# # Ele permite que a gente coloque as caixinhas (variáveis) no meio do texto,
# # apenas colocando elas entre chaves {}. 
# # O código ':.2f' dentro da chave da média serve para arredondar o número, 
# # dizendo para o computador mostrar apenas 2 (dois) números após o ponto (f).
# print(f"Sistema JWC: O aluno {nome_aluno} fechou o ano com média {media:.2f}")
