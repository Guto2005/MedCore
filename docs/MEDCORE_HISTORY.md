# MEDCORE_HISTORY.md

## Função

Preservar toda a história do projeto MedCore — as batalhas técnicas, decisões e a evolução completa, do zero até o estado atual.

## Pergunta que este arquivo responde

**"Como chegamos até aqui?"**

> Este arquivo não deve ser enxugado. É a memória viva do projeto — cada erro resolvido, cada decisão tomada, fica registrado aqui na íntegra.

---

# MEDCORE - MEMÓRIA COMPLETA DO PROJETO

## PARTE 1 - ORIGEM, ARQUITETURA E FUNDAÇÃO

Autor: Gustavo

Projeto: MedCore

Objetivo: Registrar todo o contexto necessário para continuar o desenvolvimento do MedCore em qualquer conversa futura sem perder histórico.

---

# 1. O QUE É O MEDCORE

O MedCore nasceu como um sistema hospitalar desenvolvido por Gustavo utilizando Django.

O objetivo principal do sistema é permitir que clínicas, consultórios e médicos realizem:

* Cadastro de pacientes
* Cadastro de médicos
* Controle de atendimentos
* Controle de consultas
* Controle de exames
* Upload de exames DICOM
* Visualização médica dos exames
* Emissão de laudos
* Gerenciamento administrativo

A inspiração veio de sistemas utilizados na prática médica como:

* Sonic DICOM
* Sistemas PACS
* RIS
* Plataformas de radiologia

O foco sempre foi criar algo próximo de um software profissional utilizado em hospitais.

---

# 2. DECISÃO DE TECNOLOGIA

Após diversas conversas foi decidido utilizar:

Backend:

* Python
* Django

Banco:

* SQLite

Frontend:

* HTML
* CSS puro
* JavaScript puro

Visualização DICOM:

* Cornerstone

Processamento DICOM:

* pydicom

Pré-visualizações:

* Pillow

Versionamento:

* Git
* GitHub

IDE:

* VS Code

Sistema Operacional:

* Windows

---

# 3. ESTRUTURA DO PROJETO

Projeto principal:

MedCore

Aplicações Django criadas:

* usuarios
* medicos
* pacientes
* atendimentos
* consultas
* secretarias
* dashboard
* exames

Todas adicionadas ao INSTALLED_APPS.

---

# 4. FILOSOFIA DE DESENVOLVIMENTO

Uma decisão importante foi:

Não copiar sistemas prontos.

O objetivo é entender cada componente.

Mesmo quando algo demora mais para ser construído, a prioridade é aprender como funciona internamente.

Isso vem da experiência anterior de Gustavo durante o trainee Python, onde o professor Wilson incentivava entender a lógica e não apenas copiar código.

---

# 5. SISTEMA DE USUÁRIOS

Foi criado um modelo de usuários com papéis distintos.

Tipos previstos:

ADMIN

MEDICO

USUARIO

Campos principais:

* nome
* email
* tipo_usuario

O sistema foi preparado para diferenciar permissões futuramente.

---

# 6. SISTEMA DE MÉDICOS

Modelo Médico:

Relacionamento:

Medico
→ OneToOne
→ Usuario

Campos:

* CRM
* Especialidade
* Telefone

Objetivo:

Permitir que cada médico tenha seus próprios laudos e exames.

---

# 7. SISTEMA DE PACIENTES

Foi criada aplicação específica para pacientes.

Objetivo:

Separar claramente:

* médicos
* pacientes
* usuários administrativos

Essa separação foi considerada essencial desde o início.

---

# 8. SISTEMA DE EXAMES

O módulo de exames tornou-se o núcleo do projeto.

Estrutura inicial:

Exame
→ pertence a um paciente

Campos importantes:

* arquivo
* status
* datas
* observações

O campo arquivo passou a armazenar arquivos DICOM reais.

---

# 9. DECISÃO PELO DICOM

Foi decidido que o MedCore deveria trabalhar com exames médicos reais.

Não apenas imagens PNG.

Objetivo:

Suportar:

* RX
* TC
* RM
* Mamografia
* PET
* Medicina Nuclear

Formato escolhido:

DICOM (.dcm)

Motivo:

É o padrão mundial utilizado por hospitais.

---

# 10. PRIMEIROS TESTES COM DICOM

Inicialmente foram utilizados arquivos simples.

Os testes mostraram:

Modalidade:
CT

Resolução:
512 x 512

Pixel Array:
512 x 512

Verificado através de:

pydicom

Comandos executados:

import pydicom

ds = pydicom.dcmread(...)

print(ds.Modality)
print(ds.Rows)
print(ds.Columns)
print(ds.pixel_array.shape)

Resultado:

O DICOM estava íntegro.

---

# 11. SISTEMA DE PREVIEW

Foi criado um sistema para gerar miniaturas PNG.

Objetivo:

Mostrar prévias rápidas dos exames sem abrir o DICOM completo.

Fluxo:

DICOM
↓
Pydicom
↓
Pixel Array
↓
Pillow
↓
PNG

Essas imagens começaram a ser usadas no painel lateral.

---

# 12. WORKSPACE MÉDICO

Foi criada uma tela dedicada chamada:

workspace_laudo

Objetivo:

Imitar sistemas profissionais de radiologia.

Estrutura:

Esquerda:

* Séries
* Miniaturas

Centro:

* Visualizador

Direita:

* Laudo

Rodapé:

* Informações do exame

---

# 13. LAYOUT ESCOLHIDO

Estrutura final definida:

Toolbar superior

Painel lateral esquerdo

Viewer central

Painel de laudo direito

Barra de status inferior

Inspirado em:

* Sonic
* PACS hospitalares
* Workstations de radiologia

---

# 14. ESTADO AO FINAL DA PARTE 1

Funciona:

✔ Django

✔ Banco SQLite

✔ Cadastro de usuários

✔ Cadastro de médicos

✔ Cadastro de pacientes

✔ Upload de DICOM

✔ Leitura DICOM com pydicom

✔ Geração de preview PNG

✔ Workspace médico criado

✔ Estrutura PACS definida

Próxima etapa:

Integração completa do Cornerstone.

(Fim da Parte 1)

# MEDCORE - MEMÓRIA COMPLETA DO PROJETO

## PARTE 2 - A GUERRA CONTRA O CORNERSTONE

Autor: Gustavo

Projeto: MedCore

Continuação da Parte 1

---

# 15. O OBJETIVO

Após concluir a estrutura principal do MedCore, surgiu a necessidade de transformar o sistema em algo próximo de um PACS real.

Até aquele momento:

✔ Upload DICOM funcionava

✔ Preview PNG funcionava

✔ Dados DICOM eram lidos

Mas ainda não existia:

✖ Visualização médica real

Foi então decidido integrar:

CORNERSTONE

---

# 16. O QUE É O CORNERSTONE

Cornerstone é uma biblioteca utilizada mundialmente para visualização de imagens médicas.

Ela é capaz de:

* Abrir DICOM
* Zoom
* Pan
* Window/Level
* Medidas
* Anotações
* Séries
* Scroll de slices

Basicamente é o coração dos visualizadores médicos modernos.

---

# 17. PRIMEIRA TENTATIVA

A ideia inicial foi simples:

Adicionar scripts CDN.

Exemplo:

cornerstone-core

cornerstone-tools

cornerstone-wado-image-loader

Mas os problemas começaram imediatamente.

---

# 18. PRIMEIRO ERRO

Erro:

cornerstoneWADOImageLoader is not defined

Significado:

O arquivo do WADO Loader não estava carregando.

Consequência:

O Cornerstone existia.

Mas o carregador DICOM não.

---

# 19. INVESTIGAÇÃO

Foi identificado que:

cornerstone-core carregava

cornerstone-tools carregava

Mas:

cornerstone-wado-image-loader não.

Isso impedia qualquer carregamento DICOM.

---

# 20. ERRO DE CDN

Tentativa:

Utilizar unpkg.

Erro:

404

Arquivo inexistente.

A versão que estava sendo buscada não possuía:

cornerstoneWADOImageLoader.js

---

# 21. DECISÃO PELO NODE

Foi então decidido instalar via npm.

Pacotes:

cornerstone-core

cornerstone-tools

cornerstone-wado-image-loader

dicom-parser

hammerjs

---

# 22. DESCOBERTA IMPORTANTE

Após instalação:

node_modules/cornerstone-wado-image-loader/dist

foi inspecionado.

Arquivos encontrados:

cornerstoneWADOImageLoader.bundle.min.js

cornerstoneWADOImageLoaderNoWebWorkers.bundle.min.js

index.worker.bundle.min.worker.js

Foi percebido que:

O arquivo esperado não existia.

O correto era utilizar:

cornerstoneWADOImageLoader.bundle.min.js

---

# 23. ERRO DE CAMINHO

Arquivo foi copiado.

Mas Django retornava:

404

Porque:

STATICFILES_DIRS não estava configurado.

---

# 24. DESCOBERTA DO STATIC

Foi identificado que:

Projeto possuía:

C:\Python3\Projetos\MedCore\static

Mas settings.py não possuía:

STATICFILES_DIRS

---

# 25. CORREÇÃO

Adicionado:

STATICFILES_DIRS = [
BASE_DIR / "static"
]

Após reiniciar:

Arquivo passou a carregar.

---

# 26. PRIMEIRO SINAL DE VIDA

Console:

CORNERSTONE: Module

WADO: Module

Pela primeira vez:

cornerstoneWADOImageLoader existia.

---

# 27. NOVO PROBLEMA

Mesmo carregando:

Imagem não aparecia.

Nenhum erro.

Nenhuma imagem.

Apenas tela preta.

---

# 28. INVESTIGAÇÃO DO DICOM

Foi necessário confirmar se:

O arquivo estava íntegro.

Executado:

import pydicom

ds = pydicom.dcmread(...)

Resultado:

Modality:
CT

Rows:
512

Columns:
512

Shape:
(512,512)

Conclusão:

Arquivo estava perfeito.

---

# 29. SUSPEITA

Hipótese:

Problema não era o DICOM.

Problema era o frontend.

---

# 30. NOVO TESTE

Adicionados:

console.log()

Em diversos pontos.

Objetivo:

Descobrir:

O script está rodando?

O elemento existe?

O imageId está correto?

---

# 31. DESCOBERTA CRÍTICA

O script estava sendo executado FORA do bloco correto.

No template:

workspace_laudo

Existia:

{% endblock %}

antes do script.

Resultado:

O JavaScript não estava entrando na página herdada corretamente.

---

# 32. MUDANÇA NA ARQUITETURA

Foi decidido criar:

{% block scripts %}

no workspace_base.

E colocar scripts específicos dentro dele.

---

# 33. ERRO DE TEMPLATE

Durante a alteração:

Erro:

TemplateSyntaxError

Unclosed block

---

# 34. CAUSA

Existiam:

dois endblock

ou

block aberto sem fechamento.

Foi necessário reorganizar:

workspace_base

workspace_laudo

---

# 35. CORREÇÃO

Estrutura final:

workspace_base:

{% block content %}
{% endblock %}

{% block scripts %}
{% endblock %}

workspace_laudo:

content separado

scripts separados

---

# 36. RESULTADO

Script voltou a executar.

Console passou a mostrar:

SCRIPT RODANDO

Elemento encontrado

ImageID encontrado

---

# 37. MOMENTO HISTÓRICO

Após múltiplos testes:

cornerstone.loadImage()

retornou imagem válida.

cornerstone.displayImage()

executou.

E finalmente:

A PRIMEIRA IMAGEM DICOM APARECEU NO MEDCORE.

---

# 38. O "IRRAAAA"

Quando a imagem apareceu no viewer.

Gustavo comemorou:

"IRRAAAA, deu certo porra"

Esse foi oficialmente o momento em que:

MedCore deixou de ser apenas um CRUD hospitalar.

E virou um visualizador médico funcional.

---

# 39. ESTADO DO VIEWER APÓS A VITÓRIA

Funcionando:

✔ Cornerstone

✔ DICOM Viewer

✔ Renderização CT

✔ Arquivos locais

✔ Upload

✔ Preview PNG

✔ Layout PACS

Não funcionando ainda:

✖ Zoom

✖ Pan

✖ Window/Level

✖ Medidas

✖ Ângulos

✖ Texto

✖ Scroll entre slices

✖ Séries reais

---

# 40. NOVA DESCOBERTA

Durante testes:

Foi percebido que:

Os 6 arquivos DICOM disponíveis

eram apenas:

o mesmo crânio

em imagens repetidas.

Ou seja:

não eram estudos reais completos.

---

# 41. BUSCA POR EXAMES REAIS

Foi decidido procurar bases acadêmicas.

Opção escolhida:

TCIA

The Cancer Imaging Archive

---

# 42. OBJETIVO FUTURO

Utilizar:

* TC completos
* RM completas
* Estudos com centenas de slices

Para testar:

Viewer profissional

Scroll

Séries

MPR

Ferramentas médicas

---

# ESTADO AO FINAL DA PARTE 2

Funciona:

✔ Cornerstone integrado

✔ WADO Loader funcionando

✔ Arquivos estáticos configurados

✔ Viewer renderizando DICOM

✔ CT aparecendo na tela

✔ Estrutura PACS funcional

Próxima etapa:

Transformar o viewer em algo próximo do Sonic DICOM.

(Fim da Parte 2)

# MEDCORE - MEMÓRIA COMPLETA DO PROJETO

## PARTE 3 - O WORKSPACE MÉDICO E O FUTURO PACS

Autor: Gustavo

Projeto: MedCore

Continuação da Parte 2

---

# 43. O OBJETIVO APÓS O PRIMEIRO DICOM

Depois que o primeiro DICOM apareceu na tela.

O objetivo mudou.

A missão deixou de ser:

"fazer o Cornerstone funcionar"

e passou a ser:

"transformar o MedCore em um PACS de verdade"

---

# 44. ANÁLISE DO WORKSPACE

Workspace atual:

Esquerda:

* Séries
* Miniaturas

Centro:

* Viewer DICOM

Direita:

* Laudo

Rodapé:

* Informações do exame

Visual:

Muito próximo de:

* Sonic DICOM
* PACS hospitalares
* Workstations radiológicas

---

# 45. PROBLEMA DAS MINIATURAS

Foi percebido que:

As séries laterais eram falsas.

O código estava fixo:

Série Principal

Série Auxiliar

Reconstrução

Tudo escrito manualmente.

---

# 46. PROBLEMA DE ESCALABILIDADE

Se um exame tivesse:

3 imagens

Funcionaria.

Mas se tivesse:

20

100

500

1000

Slices

O sistema quebraria conceitualmente.

---

# 47. NOVA REGRA DEFINIDA

O painel esquerdo deve ser:

DINÂMICO.

Ou seja:

O sistema deve descobrir automaticamente:

quantos slices existem

e gerar os cards sozinho.

---

# 48. DESCOBERTA IMPORTANTE

Durante testes:

Foi executado:

import os

listagem da pasta media/exames

Resultado:

6 arquivos DICOM.

---

# 49. DESCOBERTA MAIS IMPORTANTE

Esses 6 arquivos não eram:

6 slices de um exame.

Eram:

6 cópias da mesma imagem.

Ou imagens praticamente iguais.

---

# 50. CONSEQUÊNCIA

Não era possível testar:

* Scroll
* Séries
* Navegação
* Slice Counter

Porque não existia um estudo real.

---

# 51. O PROBLEMA DO "SLICE 1/1"

No viewer existia:

Slice 1/1

Escrito diretamente no HTML.

Foi identificado que:

Isso é incorreto.

Em um sistema real:

Esse valor deve ser calculado.

---

# 52. COMO FUNCIONA EM PACS REAIS

Exemplo:

TC de crânio

300 imagens

O PACS mostra:

Slice 157/300

---

Exemplo:

RM de joelho

120 imagens

O PACS mostra:

Slice 58/120

---

Exemplo:

RX simples

1 imagem

O PACS mostra:

Slice 1/1

---

# 53. DECISÃO FUTURA

O contador deve vir:

Do conjunto de arquivos DICOM.

Nunca do HTML.

---

# 54. A IDEIA DE UM ESTUDO

Foi introduzido o conceito:

Estudo

Study

---

Um exame real não é:

1 arquivo DICOM.

Normalmente é:

Muitos arquivos DICOM.

---

Exemplo:

TC Crânio

↓

300 arquivos DICOM

↓

1 Estudo

---

# 55. CONSEQUÊNCIA PARA O BANCO

No futuro:

O modelo Exame provavelmente precisará suportar:

1 exame

↓

muitos DICOMs

---

Possivelmente:

Exame

↓

Serie

↓

Imagem DICOM

---

# 56. REFERÊNCIA SONIC

Durante o desenvolvimento:

Foi citado diversas vezes:

Sonic DICOM

Porque é uma das referências visuais.

---

Funcionalidades desejadas:

✔ Zoom

✔ Pan

✔ Window Level

✔ Medidas

✔ Texto

✔ Marcação de áreas

✔ Ferramentas radiológicas

✔ Navegação por slices

✔ Séries

---

# 57. MARCAÇÕES MÉDICAS

Foi discutido:

Médicos frequentemente desenham:

* círculos
* setas
* linhas
* medições

sobre o exame.

---

Exemplo:

Nódulo pulmonar

↓

círculo desenhado

↓

comentário no laudo

---

# 58. OBJETIVO FUTURO

Permitir:

Anotações diretamente no viewer.

Sem precisar editar a imagem.

---

# 59. FERRAMENTAS PREVISTAS

Toolbar atual:

Zoom

Pan

Window

Medir

Ângulo

Texto

Histórico

Fullscreen

---

Situação:

Visualmente presentes.

Funcionalmente ainda não.

---

# 60. ORDEM DEFINIDA DE IMPLEMENTAÇÃO

Prioridade:

1. Séries reais

2. Slice Counter real

3. Scroll do mouse

4. Zoom

5. Pan

6. Window/Level

7. Medidas

8. Anotações

9. Ferramentas avançadas

---

# 61. NOVA NECESSIDADE

Foi percebido:

Os testes atuais são limitados.

Motivo:

Não existem exames complexos.

---

# 62. DECISÃO DE BUSCAR CASOS REAIS

Foi escolhida:

TCIA

The Cancer Imaging Archive

---

Objetivo:

Baixar:

* TC
* RM
* PET
* Mamografia

Reais.

---

# 63. PRIMEIRO CASO ENCONTRADO

Foi encontrado:

Caso relacionado à leucemia.

Através do TCIA.

---

# 64. PROBLEMA DO TCIA

O TCIA não fornece:

DICOM diretamente.

Inicialmente.

Ele fornece:

Manifest

arquivo .tcia

---

# 65. DESCOBERTA

O arquivo:

manifest-xxxxxxxx.tcia

não contém imagens.

Ele é apenas:

uma lista de download.

---

# 66. SOLUÇÃO FUTURA

Utilizar:

NBIA Data Retriever

ou

Download Query

para baixar os DICOMs reais.

---

# 67. VISÃO DE LONGO PRAZO

O objetivo final do MedCore é:

Não ser apenas um CRUD.

Não ser apenas um sistema de cadastro.

Mas um:

Sistema hospitalar completo.

Com visualização médica profissional.

---

# ESTADO AO FINAL DA PARTE 3

Funciona:

✔ Viewer DICOM

✔ Cornerstone

✔ Upload

✔ Preview PNG

✔ Workspace

✔ Laudo

✔ Estrutura PACS

Ainda falta:

✖ Estudos reais

✖ Séries reais

✖ Slice Counter real

✖ Scroll

✖ Ferramentas médicas

✖ Anotações

✖ Zoom

✖ Pan

✖ Window/Level

Próxima parte:

Estado atual do MedCore, arquitetura completa do banco, problemas conhecidos, dívidas técnicas e roadmap detalhado para transformar o projeto em um sistema hospitalar profissional.

(Fim da Parte 3)

# MEDCORE - MEMÓRIA COMPLETA DO PROJETO

## PARTE 4 - ESTADO ATUAL, DÍVIDAS TÉCNICAS E ROADMAP PROFISSIONAL

Autor: Gustavo

Projeto: MedCore

Continuação da Parte 3

---

# 68. O QUE O MEDCORE É HOJE

Neste momento da conversa.

O MedCore deixou de ser apenas um projeto acadêmico.

Ele já possui:

✔ Backend funcional

✔ Banco funcional

✔ Estrutura hospitalar funcional

✔ Upload de DICOM

✔ Geração de Preview

✔ Viewer DICOM funcionando

✔ Workspace Médico

✔ Sistema de Laudo

Ou seja.

O projeto já ultrapassou a fase de "CRUD simples".

---

# 69. O MAIOR MARCO DO PROJETO

Até aqui.

O maior marco foi:

Renderizar um DICOM real no navegador.

Isso foi importante porque:

Muita gente faz CRUD.

Pouca gente consegue:

* Processar DICOM
* Gerar Preview
* Exibir usando Cornerstone

---

# 70. ARQUITETURA ATUAL

Aplicações existentes:

usuarios

medicos

pacientes

atendimentos

consultas

secretarias

dashboard

exames

---

# 71. FLUXO ATUAL

Paciente

↓

Exame

↓

Upload DICOM

↓

Preview PNG

↓

Workspace

↓

Laudo

---

# 72. O QUE ESTÁ FUNCIONANDO

Usuários

✔ Cadastro

✔ Persistência

---

Médicos

✔ Cadastro

✔ CRM

✔ Especialidade

---

Pacientes

✔ Cadastro

✔ Associação

---

Exames

✔ Upload

✔ Armazenamento

✔ Leitura

---

Workspace

✔ Viewer

✔ Preview

✔ Painel de laudo

---

Cornerstone

✔ Carregamento

✔ Exibição

---

# 73. DÍVIDA TÉCNICA Nº1

ESTUDOS REAIS

Hoje:

1 Exame

↓

1 Arquivo DICOM

---

Realidade hospitalar:

1 Exame

↓

Múltiplas Séries

↓

Centenas de DICOMs

---

Essa é provavelmente a maior limitação atual.

---

# 74. DÍVIDA TÉCNICA Nº2

PAINEL DE SÉRIES

Atualmente:

Fake.

Hardcoded.

---

Exemplo:

Série Principal

Série Auxiliar

Reconstrução

---

Essas séries não existem.

São apenas cartões visuais.

---

# 75. DÍVIDA TÉCNICA Nº3

SLICE COUNTER

Hoje:

1/1

fixo.

---

Correto:

157/300

89/120

1/1

dependendo do estudo.

---

# 76. DÍVIDA TÉCNICA Nº4

SCROLL ENTRE IMAGENS

Hoje:

Inexistente.

---

Em PACS reais:

Scroll do mouse

↓

Próximo slice

↓

Anterior slice

---

Essencial para TC e RM.

---

# 77. DÍVIDA TÉCNICA Nº5

WINDOW LEVEL

Hoje:

Não implementado.

---

É uma das ferramentas mais usadas por radiologistas.

Permite:

* Clarear
* Escurecer
* Destacar tecidos

---

Sem isso.

Um CT fica praticamente "cego".

---

# 78. DÍVIDA TÉCNICA Nº6

ZOOM

Botão existe.

Função não.

---

# 79. DÍVIDA TÉCNICA Nº7

PAN

Botão existe.

Função não.

---

# 80. DÍVIDA TÉCNICA Nº8

MEDIDAS

Botão existe.

Função não.

---

Futuro:

Medir:

* Tumores
* Distâncias
* Fraturas

---

# 81. DÍVIDA TÉCNICA Nº9

ANOTAÇÕES

Hoje:

Inexistentes.

---

Futuro:

Médico desenha:

○ círculo

→ seta

✎ texto

---

Sem alterar o DICOM original.

---

# 82. DÍVIDA TÉCNICA Nº10

FULLSCREEN

Botão visual.

Sem implementação.

---

# 83. DÍVIDA TÉCNICA Nº11

HISTÓRICO

Botão visual.

Sem backend.

---

Futuro:

Histórico de:

* Laudos
* Alterações
* Revisões

---

# 84. ROADMAP IMEDIATO

Próximos passos ideais:

PASSO 1

Conseguir estudo real.

TCIA.

---

PASSO 2

Importar estudo completo.

---

PASSO 3

Criar navegação entre slices.

---

PASSO 4

Corrigir contador.

---

PASSO 5

Gerar painel de séries dinâmico.

---

# 85. ROADMAP MÉDIO PRAZO

Adicionar:

Zoom

Pan

Window Level

Length Tool

Angle Tool

Text Tool

---

Transformar viewer em algo próximo ao Sonic.

---

# 86. ROADMAP LONGO PRAZO

Sistema PACS completo.

---

Estrutura:

Paciente

↓

Estudo

↓

Série

↓

DICOM

---

Sem hacks.

Sem gambiarra.

---

# 87. POSSÍVEL FUTURO COM IA

Já foi discutido algumas vezes.

Possibilidade futura:

IA auxiliar.

---

Não para substituir médicos.

Mas para:

* Destacar áreas suspeitas
* Auxiliar triagem
* Organizar exames

---

Muito distante ainda.

Mas possível.

---

# 88. SITUAÇÃO REAL DO PROJETO

Se fosse dar uma nota hoje.

CRUD Hospitalar:

9/10

---

Visualização Médica:

4/10

---

Infraestrutura:

7/10

---

Potencial:

Muito alto.

---

# 89. O QUE MAIS IMPRESSIONA

Até aqui.

O projeto foi feito praticamente por:

* Gustavo
* Conversas técnicas
* Tentativa e erro

Sem equipe.

Sem financiamento.

Sem framework hospitalar pronto.

---

# 90. CONCLUSÃO DA FASE ATUAL

O MedCore já provou que consegue:

✔ Armazenar exames

✔ Processar DICOM

✔ Renderizar DICOM

✔ Criar Workspace Médico

Agora começa a fase mais interessante:

Transformar o Viewer em uma ferramenta que um médico realmente conseguiria utilizar no dia a dia.

(Fim da Parte 4)

# MEDCORE - MEMÓRIA COMPLETA DO PROJETO

## PARTE 5 - INFRAESTRUTURA, AMBIENTE E PROBLEMAS TÉCNICOS

Autor: Gustavo

Projeto: MedCore

Continuação da Parte 4

---

# 91. AMBIENTE PRINCIPAL

Sistema Operacional:

Windows 10

---

Projeto localizado em:

C:\Python3\Projetos\MedCore

---

Estrutura principal:

MedCore/

├── usuarios/

├── medicos/

├── pacientes/

├── atendimentos/

├── consultas/

├── secretarias/

├── dashboard/

├── exames/

├── media/

├── static/

├── venv/

├── manage.py

└── db.sqlite3

---

# 92. PYTHON UTILIZADO

Versão utilizada:

Python 3.13.2

---

Verificado diversas vezes durante:

* shell
* migrações
* testes

---

# 93. DJANGO UTILIZADO

Versão:

Django 6.0.5

---

Inicialmente houve confusão porque o projeto havia começado com referências ao Django 4.2.

Posteriormente foi confirmado:

Django 6.0.5

---

# 94. BANCO DE DADOS

Banco atual:

SQLite

Arquivo:

db.sqlite3

---

Motivos:

* Simples
* Leve
* Exigência acadêmica
* Não exige servidor separado

---

Futuro:

PostgreSQL

---

# 95. VIRTUALENV

Ambiente virtual:

venv

---

Ativação:

venv\Scripts\Activate.ps1

---

Problemas comuns:

ExecutionPolicy do PowerShell.

Resolução:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

---

# 96. FERRAMENTAS UTILIZADAS

Editor principal:

Visual Studio Code

---

Terminal:

PowerShell

---

Git:

Git Bash

---

Versionamento:

GitHub

---

# 97. PRIMEIRA GRANDE DIFICULDADE

Buildozer

---

Projeto anterior:

Tabuada APK

---

Problemas:

Python 3.14

Kivy

Pyjnius

Buildozer

Android SDK

Android NDK

---

Foram dias tentando resolver.

---

# 98. APRENDIZADO IMPORTANTE

Foi nessa fase que surgiu o hábito de:

* ler logs
* investigar erros
* analisar stack traces

---

Isso ajudou diretamente no MedCore.

---

# 99. PRIMEIRO CONTATO COM NODE.JS

Motivo:

Cornerstone

---

Necessidade:

npm

node_modules

bibliotecas modernas

---

Foi a primeira vez que o projeto exigiu frontend mais avançado.

---

# 100. CORNERSTONE

Objetivo:

Visualização DICOM

---

Motivo:

Simular softwares reais:

* Sonic DICOM
* PACS hospitalares
* Visualizadores médicos

---

# 101. PRIMEIRA TENTATIVA

Uso via CDN.

Scripts:

cornerstone-core

cornerstone-tools

cornerstone-wado-image-loader

---

Resultado:

Erro.

---

# 102. PRIMEIRO ERRO IMPORTANTE

Mensagem:

cornerstoneWADOImageLoader is not defined

---

Motivo:

Biblioteca não carregava.

---

# 103. INVESTIGAÇÃO

Foi descoberto que:

O CDN utilizado não possuía o arquivo esperado.

---

O script retornava:

404

---

# 104. SOLUÇÃO

Instalação local.

npm install cornerstone-wado-image-loader

---

# 105. DESCOBERTA IMPORTANTE

Dentro de:

node_modules/cornerstone-wado-image-loader/dist

existia:

cornerstoneWADOImageLoader.bundle.min.js

---

Esse foi o arquivo correto.

---

# 106. ERRO DE STATIC FILES

Após copiar o arquivo.

Novo erro:

404

---

Django não encontrava:

static/libs/cornerstone/cornerstoneWADOImageLoader.bundle.min.js

---

# 107. CAUSA

STATICFILES_DIRS não configurado.

---

Django não sabia onde procurar.

---

# 108. SOLUÇÃO

Adicionar:

STATICFILES_DIRS = [
BASE_DIR / "static",
]

---

Depois reiniciar servidor.

---

# 109. PRIMEIRO SINAL DE VIDA

Console:

CORNERSTONE: Module

WADO: Module

---

Foi o primeiro momento em que o loader apareceu funcionando.

---

# 110. SEGUNDO PROBLEMA

DICOM não aparecia.

---

Mesmo carregando bibliotecas.

---

Tela continuava preta.

---

# 111. INVESTIGAÇÃO

Testes feitos:

console.log

imageId

element

loadImage

displayImage

---

# 112. DESCOBERTA

O script estava fora do bloco correto do template.

---

O JavaScript sequer executava.

---

# 113. CORREÇÃO

Criação do bloco:

scripts

---

workspace_base:

{% block scripts %}
{% endblock %}

---

workspace_laudo:

{% block scripts %}

script

{% endblock %}

---

# 114. TERCEIRO PROBLEMA

Erro:

Unclosed block tag

---

Motivo:

Blocos Django mal fechados.

---

Foram corrigidos:

endblock

content

scripts

---

# 115. PRIMEIRO DICOM RENDERIZADO

Momento histórico.

---

Após todas as correções.

O Cornerstone finalmente exibiu:

imagem real de TC.

---

# 116. CONFIRMAÇÃO

Python:

pydicom

---

Resultado:

Modality:
CT

Rows:
512

Columns:
512

pixel_array:
(512,512)

---

Confirmando:

Arquivo válido.

---

# 117. PREVIEWS

Preview PNG:

funcionando.

---

Gerado pelo backend.

---

Exibido na lateral.

---

# 118. WORKSPACE

Estrutura atual:

Toolbar

↓

Series Panel

↓

Viewer

↓

Laudo

---

Muito próximo visualmente de sistemas médicos reais.

---

# 119. SITUAÇÃO DO NODE

Hoje:

Node instalado.

npm funcional.

Cornerstone instalado.

---

Dependências já existentes.

---

# 120. SITUAÇÃO DA INFRAESTRUTURA

Backend:

Estável

---

Banco:

Estável

---

Upload:

Estável

---

Preview:

Estável

---

Viewer:

Funcional

---

Cornerstone:

Funcional

---

# 121. PRINCIPAL LIÇÃO TÉCNICA

Até aqui.

O maior aprendizado foi:

"Quase nunca o erro está onde parece."

---

Exemplos reais:

* CDN errado
* Static errado
* Script fora do bloco
* Template quebrado
* Configuração Django

---

Todos pareciam problemas do Cornerstone.

Mas vários eram problemas de estrutura.

---

# 122. CONCLUSÃO

Ao final desta fase.

O MedCore possui infraestrutura suficiente para:

✔ Upload

✔ Processamento

✔ Leitura DICOM

✔ Renderização DICOM

✔ Expansão futura

Sem necessidade de refatorações gigantes.

(Fim da Parte 5)

# MEDCORE - MEMÓRIA COMPLETA DO PROJETO

## PARTE 6 - DECISÕES ARQUITETURAIS E FILOSOFIA DO SISTEMA

Autor: Gustavo

Projeto: MedCore

Continuação da Parte 5

---

# 123. O OBJETIVO ORIGINAL

O MedCore nunca nasceu como:

* CRUD de Django
* Trabalho de faculdade
* Projeto de tutorial

---

O objetivo sempre foi:

Construir um sistema hospitalar real.

---

Mesmo que inicialmente simplificado.

---

# 124. FILOSOFIA PRINCIPAL

A regra adotada desde o início:

"Fazer simples agora para crescer depois."

---

Evitar:

* Engenharia excessiva
* Microserviços
* Complexidade prematura

---

# 125. ESCOLHA DO DJANGO

Motivos:

* Produtividade
* ORM robusto
* Painel Admin
* Segurança
* Rapidez para prototipar

---

Alternativas consideradas:

Flask

FastAPI

---

Decisão:

Django.

---

# 126. ESCOLHA DO SQLITE

Não foi por ser o melhor.

---

Foi escolhido porque:

* Funciona imediatamente
* Não exige servidor
* Facilita desenvolvimento
* Compatível com exigência acadêmica

---

Plano futuro:

PostgreSQL.

---

# 127. SEPARAÇÃO POR APPS

Decisão importante.

---

Ao invés de um sistema gigante.

Separação em:

usuarios

medicos

pacientes

consultas

atendimentos

secretarias

dashboard

exames

---

Motivo:

Facilidade de manutenção.

---

# 128. SISTEMA DE USUÁRIOS

Decisão:

Usuário centralizado.

---

Todos passam por:

Usuario

---

Especializações:

Admin

Médico

Secretária

Usuário comum

---

Permite expansão futura.

---

# 129. MÉDICOS SEPARADOS

Decisão:

Médico não é apenas usuário.

---

Médico possui:

CRM

Especialidade

Telefone

---

Por isso:

OneToOne com Usuario.

---

# 130. PACIENTES SEPARADOS

Paciente não depende de login.

---

Motivo:

Hospitais possuem milhares de pacientes.

---

Nem todos acessam sistema.

---

# 131. CONSULTAS SEPARADAS DE ATENDIMENTOS

Decisão estratégica.

---

Consulta:

Agendamento.

---

Atendimento:

Execução.

---

Isso aproxima do fluxo real hospitalar.

---

# 132. EXAMES COMO MÓDULO PRÓPRIO

Decisão extremamente importante.

---

Motivo:

O futuro PACS.

---

Exames seriam:

* independentes
* escaláveis
* preparados para DICOM

---

# 133. NÃO UTILIZAR BOOTSTRAP

Decisão consciente.

---

Motivo:

Visual genérico.

---

Objetivo:

Sistema com identidade própria.

---

# 134. TEMA ESCURO

Decisão obrigatória.

---

Motivos:

Menos fadiga visual.

Ambiente hospitalar.

Visual moderno.

---

# 135. INSPIRAÇÃO VISUAL

Referências:

Sonic DICOM

PACS hospitalares

Sistemas radiológicos

Softwares médicos reais

---

# 136. SIDEBAR

Decisão:

Navegação permanente.

---

Motivo:

Usuário precisa acessar:

Pacientes

Consultas

Médicos

Exames

---

Sem voltar telas.

---

# 137. TOPBAR

Decisão:

Sempre mostrar contexto.

---

Exemplo:

Usuário logado.

Função.

Atalhos.

---

# 138. DASHBOARD

Objetivo:

Visão executiva.

---

Mostrar:

Pacientes

Consultas

Exames

Indicadores

---

# 139. DICOM COMO PRIORIDADE

Grande decisão.

---

Muitos sistemas acadêmicos:

Param no CRUD.

---

MedCore:

Entrou em DICOM.

---

Isso elevou muito a complexidade.

---

# 140. ESCOLHA DO CORNERSTONE

Motivo:

Padrão de mercado.

---

Capaz de:

Zoom

Pan

Window Level

Anotações

Medições

Ferramentas radiológicas

---

# 141. NÃO USAR IMAGENS PNG COMO VISUALIZADOR FINAL

Importante.

---

PNG serve:

Preview.

---

Mas o diagnóstico real deve ocorrer no DICOM.

---

# 142. SEPARAÇÃO PREVIEW / VISUALIZADOR

Decisão:

Preview lateral.

---

Visualização principal:

Cornerstone.

---

Mesmo padrão usado em PACS.

---

# 143. LAUDO AO LADO DA IMAGEM

Decisão inspirada em sistemas reais.

---

Radiologista:

Visualiza imagem.

Escreve laudo.

---

Sem trocar de tela.

---

# 144. SISTEMA PREPARADO PARA TELELAUDO

Objetivo futuro.

---

Médico poderá:

Abrir exame.

Visualizar.

Laudar.

Salvar.

Finalizar.

---

Tudo remotamente.

---

# 145. RASCUNHO E FINALIZAÇÃO

Decisão importante.

---

Nem todo laudo nasce pronto.

---

Estados:

Rascunho

Finalizado

---

# 146. EVITAR REFAZER CÓDIGO

Filosofia adotada:

Sempre construir pensando na próxima etapa.

---

Exemplo:

Preview.

Mesmo simples.

Já preparado para múltiplas séries.

---

# 147. PENSAMENTO DE LONGO PRAZO

Meta atual:

Sistema funcional.

---

Meta futura:

Software hospitalar real.

---

# 148. DIFERENCIAL DO PROJETO

O MedCore começou como:

Projeto de aprendizado.

---

Mas a arquitetura já aponta para:

* PACS
* Telelaudo
* Radiologia
* Gestão clínica

---

# 149. MAIOR DECISÃO TOMADA

Não abandonar.

---

Mesmo após:

* erros
* bugs
* bibliotecas quebradas
* problemas do Cornerstone
* problemas do Django

---

O projeto continuou evoluindo.

---

# 150. CONCLUSÃO

Nesta fase.

O MedCore deixou de ser apenas um projeto Django.

Passou a ter uma arquitetura pensada para crescer como uma plataforma médica real.

(Fim da Parte 6)

# MEDCORE - MEMÓRIA COMPLETA DO PROJETO

## PARTE 7 - PENDÊNCIAS REAIS, ESTADO EXATO E PRÓXIMAS IMPLEMENTAÇÕES

Autor: Gustavo

Projeto: MedCore

Continuação da Parte 6

---

# 151. SITUAÇÃO REAL DO PROJETO

Ao final desta conversa.

O MedCore NÃO está finalizado.

Mas também já passou muito da fase inicial.

---

Hoje ele está em um estado que pode ser descrito como:

Protótipo funcional de sistema hospitalar com visualização DICOM.

---

# 152. O QUE FUNCIONA DE VERDADE

Usuários

✔ Cadastro

✔ Banco

✔ Login

✔ Permissões básicas

---

Médicos

✔ Cadastro

✔ CRM

✔ Especialidade

---

Pacientes

✔ Cadastro

✔ Consulta

✔ Relacionamento

---

Exames

✔ Cadastro

✔ Upload

✔ Armazenamento

---

DICOM

✔ Leitura

✔ Processamento

✔ Preview PNG

✔ Renderização no navegador

---

Cornerstone

✔ Carregado

✔ Funcionando

✔ Exibindo exame real

---

Workspace

✔ Estrutura pronta

✔ Layout funcional

✔ Viewer funcionando

✔ Painel de laudo funcionando

---

# 153. O QUE ESTÁ FALSO (PLACEHOLDER)

Várias partes do sistema hoje existem apenas visualmente.

---

Painel de séries

Hoje:

```text
Série Principal
Série Auxiliar
Reconstrução
```

---

Essas séries não são reais.

Foram escritas manualmente.

---

# 154. O QUE PRECISA SER FEITO NO PAINEL DE SÉRIES

Transformar:

```html
<div class="series-card">
```

em algo gerado automaticamente.

---

Objetivo:

Se existirem:

3 séries

↓

mostrar 3.

---

Se existirem:

25 séries

↓

mostrar 25.

---

Sem limite fixo.

---

# 155. O PROBLEMA DOS SLICES

Hoje:

```text
Slice 1/1
```

está escrito diretamente no HTML.

---

Isso é temporário.

---

O correto será:

```text
Slice 157/300
```

ou

```text
Slice 45/120
```

dependendo do exame.

---

# 156. O MAIOR BLOQUEIO ATUAL

Não possuímos um estudo real.

---

Os arquivos existentes:

6 DICOMs

---

Mas esses 6 DICOMs são praticamente:

o mesmo exame

a mesma região

o mesmo ângulo

---

Isso impede:

* scroll
* navegação
* slices reais

---

# 157. TCIA

Foi iniciada a busca por exames reais.

---

Fonte escolhida:

TCIA

The Cancer Imaging Archive

---

Objetivo:

Conseguir estudos completos.

---

# 158. PROBLEMA ENCONTRADO

O TCIA não entrega os arquivos diretamente.

---

Primeiro download:

manifest.tcia

---

Resultado:

não era o exame.

---

Era apenas uma lista de download.

---

# 159. SITUAÇÃO ATUAL DO TCIA

Ainda não foi concluída.

---

Nenhum estudo completo foi baixado.

---

Portanto:

Ainda não temos material suficiente para testar:

* centenas de slices
* múltiplas séries
* navegação

---

# 160. BOTÃO ZOOM

Existe visualmente.

---

Hoje:

não faz nada.

---

Precisa ser ligado ao:

Cornerstone Zoom Tool.

---

# 161. BOTÃO PAN

Existe visualmente.

---

Hoje:

não faz nada.

---

Precisa ser ligado ao:

Pan Tool.

---

# 162. BOTÃO WINDOW

Existe visualmente.

---

Hoje:

não faz nada.

---

É uma das ferramentas mais importantes para radiologia.

---

# 163. BOTÃO MEDIR

Existe visualmente.

---

Hoje:

não mede nada.

---

Objetivo:

Permitir:

* medir tumores
* medir lesões
* medir distâncias

---

# 164. BOTÃO ÂNGULO

Existe visualmente.

---

Hoje:

não funciona.

---

Objetivo:

Medição angular.

---

# 165. BOTÃO TEXTO

Existe visualmente.

---

Hoje:

não funciona.

---

Objetivo:

Anotar observações diretamente sobre a imagem.

---

# 166. HISTÓRICO

Existe botão.

---

Hoje:

sem backend.

---

Objetivo futuro:

Mostrar:

* revisões
* alterações
* versões do laudo

---

# 167. FULLSCREEN

Existe botão.

---

Hoje:

sem implementação.

---

Objetivo:

Expandir viewer para tela inteira.

---

# 168. ANOTAÇÕES MÉDICAS

Ainda inexistentes.

---

Objetivo:

Permitir:

○ círculos

□ caixas

→ setas

✎ textos

---

Igual sistemas profissionais.

---

# 169. MEDCORE AINDA NÃO POSSUI

❌ Scroll entre slices

❌ Navegação por série

❌ Window Presets

❌ Medidas

❌ Anotações

❌ PACS

❌ Worklist

❌ Query/Retrieve

❌ IA

---

# 170. O QUE DEVE SER FEITO PRIMEIRO

Ordem ideal:

1. Conseguir estudo real

2. Importar estudo

3. Gerar slices reais

4. Corrigir contador

5. Criar painel de séries dinâmico

6. Implementar scroll

7. Implementar zoom

8. Implementar pan

9. Implementar window level

10. Implementar medidas

---

# 171. O QUE NÃO DEVE SER FEITO AGORA

Não vale a pena:

* IA
* PACS completo
* PostgreSQL
* Telelaudo avançado

---

Antes de resolver:

visualização.

---

# 172. A MAIOR VITÓRIA DESTA CONVERSA

O DICOM apareceu.

---

Isso parece simples.

Mas foi o momento que provou que:

* Django funciona
* Upload funciona
* Preview funciona
* Cornerstone funciona
* Viewer funciona

---

Foi a validação mais importante do projeto até agora.

---

# 173. ESTIMATIVA DE MATURIDADE

CRUD Hospitalar:

9/10

---

Gestão de usuários:

8/10

---

Gestão de pacientes:

8/10

---

Exames:

7/10

---

Visualizador DICOM:

5/10

---

PACS profissional:

2/10

---

# 174. ESTADO FINAL AO ENCERRAR ESTA CONVERSA

O MedCore já é capaz de:

✔ Cadastrar

✔ Armazenar

✔ Processar

✔ Exibir exames DICOM

✔ Produzir laudos

---

Mas ainda precisa evoluir para se tornar:

✔ uma estação radiológica completa

✔ um PACS

✔ um ambiente profissional de diagnóstico

---

# FIM DA DOCUMENTAÇÃO ATUAL

Partes concluídas:

✔ Parte 1

✔ Parte 2

✔ Parte 3

✔ Parte 4

✔ Parte 5

✔ Parte 6

✔ Parte 7

Esta documentação representa o estado completo do MedCore até o encerramento desta conversa.

(Fim da Parte 7)

