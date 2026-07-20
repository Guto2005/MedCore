# MEDCORE_LAB.md

# Função

Laboratório oficial de pesquisa, experimentação e evolução do MedCore.

Este documento responde à pergunta:

> **"O que está sendo estudado, investigado ou planejado para o futuro do MedCore?"**

Nenhuma informação contida neste documento representa regra oficial do projeto até passar pelo processo de validação e promoção para o `MEDCORE_CORE_CONTEXT.md`.

---

# Fluxo Oficial de Evolução

```text
IDEIA
 ↓
LAB
 ↓
ANÁLISE
 ↓
VALIDAÇÃO TÉCNICA
 ↓
VALIDAÇÃO COM USUÁRIOS
 ↓
DECISÃO

      ↙          ↘

REPROVADO     APROVADO
     ↓             ↓
 Arquivado     CORE_CONTEXT
```

O objetivo desse fluxo é impedir que decisões arquiteturais sejam tomadas apenas porque parecem interessantes tecnicamente.

Toda evolução deve possuir justificativa operacional.

---

# Filosofia do LAB

O LAB existe para preservar ideias.

Nem toda boa ideia deve virar código.

Toda proposta registrada neste documento deve responder obrigatoriamente:

- Qual problema ela resolve?
- Quem sofre esse problema?
- Existe validação com usuário real?
- Ela reduz tempo?
- Ela reduz erros?
- Ela reduz retrabalho?
- Ela reduz troca de sistemas?
- Vale o custo de manutenção que adicionará ao projeto?

Caso essas perguntas não possam ser respondidas, a ideia permanece em estudo.

---

# Regra de Promoção LAB → CORE_CONTEXT

Sempre que uma ideia for promovida para o CORE_CONTEXT deverá ser registrado:

## Problema resolvido

Qual necessidade real motivou a implementação.

Nunca utilizar justificativas como:

> "Parecia interessante."

ou

> "Outros sistemas possuem."

---

## Origem da solicitação

Registrar quem motivou a implementação.

Exemplos:

- Gustavo
- Dr. Cristiano
- Secretária
- Diretor Hospitalar
- Usuário piloto
- Outro profissional

---

## Motivo da aprovação

Explicar por que aquela funcionalidade entrou exatamente naquele momento do roadmap.

Esse histórico preserva o raciocínio arquitetural do projeto.

---

# Filosofia de Evolução

O MedCore cresce resolvendo problemas reais.

Não cresce acumulando funcionalidades.

Toda implementação deve aumentar pelo menos um destes indicadores:

- produtividade;
- segurança;
- simplicidade;
- integração;
- qualidade da experiência do profissional.

Sempre que possível, validar com usuários reais antes da implementação.

---

# Visão Estratégica do Produto

O MedCore não pretende ser apenas um visualizador DICOM.

A visão de longo prazo é tornar-se uma plataforma hospitalar completa, capaz de integrar:

- PACS
- RIS
- Workspace Médico
- Gestão de Laudos
- Auditoria
- Indicadores Operacionais
- Financeiro
- Multi-Hospital
- Portal do Cliente

O objetivo é reduzir drasticamente a quantidade de softwares utilizados por clínicas e hospitais.

---

# Roadmap Estratégico

## Fase 1.5 — Workspace Médico (MVP Comercial)

### Objetivo

Entregar uma estação de trabalho de radiologia utilizável em ambiente real para validação com o Dr. Cristiano.

Nenhum novo módulo deve atrasar essa entrega.

---

## Visualização DICOM

Implementado

- Cornerstone
- Renderização DICOM
- Upload
- Preview PNG

Em evolução

- Zoom
- Pan
- Window / Level
- Scroll entre slices
- Ferramentas de medição
- Histórico do paciente
- Navegação segura

---

## Ferramentas previstas

Visualização

- Zoom
- Pan
- Window / Level
- Scroll
- Fullscreen

Medição

- Distância
- Ângulo
- Texto

Melhorias estudadas

- Reset View
- Fit to Screen
- Inverter cores
- Rotação
- Flip Horizontal
- Flip Vertical

Essas funcionalidades serão avaliadas conforme necessidade observada durante os testes clínicos.

---

## Navegação entre Slices

Objetivos

- Scroll do mouse
- Próximo slice
- Slice anterior
- Slider
- Navegação por teclado
- Contador real

Exemplo

```text
1 / 532
2 / 532
...
532 / 532
```

---

## Estudos DICOM

Arquitetura desejada

```text
Exame

↓

Estudo

↓

Axial
Coronal
Sagital
Reconstruções

↓

Centenas de slices
```

O usuário navega pelas séries.

Não por centenas de miniaturas.

---

## Painel de Séries

Inspirado em PACS comerciais.

Estrutura desejada

```text
┌────────────────────┐
│ TC Crânio          │
│ Preview            │
│ 300 imagens        │
└────────────────────┘
```

Cada série abre no Viewer principal.

---

## Ferramentas de Medição

Implementadas

- Distância
- Ângulo
- Texto

Em estudo

- ROI Circular
- ROI Retangular
- ROI Livre
- Área
- Estatísticas
- Densidade (HU)

Essas ferramentas somente entram após validação da necessidade clínica.

---

## Presets Radiológicos

Estudo futuro.

Botões rápidos.

Exemplos

- Pulmão
- Osso
- Cérebro
- Abdome
- Tecido Mole

Objetivo

Aplicar automaticamente Window/Level apropriado.

---

## Produtividade Médica

Ideias atualmente em avaliação

### HUD Inteligente

Exibir continuamente

- Zoom
- Slice
- Window
- Level

Objetivo

Dar feedback visual imediato ao médico.

---

### Atalhos

Exemplos

Ctrl + Scroll → Zoom

Scroll → Navegação entre slices

Ctrl + S → Salvar

Ctrl + Enter → Finalizar

Objetivo

Reduzir quantidade de cliques.

---

### Navegação Segura

Estudos atuais

- Botão Voltar
- Botão Cancelar
- Confirmação de saída
- beforeunload
- Detecção de alterações não salvas

Objetivo

Eliminar perda acidental de laudos.

---

### Auto Save

Em estudo.

Salvar automaticamente:

- por tempo
- troca de série
- troca de exame

Objetivo

Evitar perda de trabalho.

---

### Comparação de Exames

Fluxo desejado

Histórico

↓

Selecionar exame anterior

↓

Abrir nova guia

↓

Comparação lado a lado

Objetivo

Permitir avaliação da evolução clínica.

Esse diferencial nasceu da necessidade observada durante o desenho do Workspace Médico e deverá ser validado com o Dr. Cristiano antes de se tornar comportamento definitivo.

---

## Testes de Estresse

Meta mínima

- 500 slices
- 1000 slices
- 2000 slices

Objetivo

Garantir estabilidade antes da comercialização.

---

# Fase 1.6 — Produtividade Médica

Objetivo

Reduzir tempo de laudagem.

Possíveis funcionalidades

- Templates de laudo
- Histórico de versões
- Adendos
- Workspace em modo Consulta/Edição
- Auditoria inicial
- Anotações persistentes
- Cine Mode
- Atalhos de teclado
- Salvamento inteligente

Todas essas funcionalidades permanecem em avaliação e somente entrarão após conclusão da versão 1.5.

# Fase 1.7 — Auditoria e Conformidade

## Objetivo

Garantir rastreabilidade completa das ações realizadas dentro do sistema.

Nenhuma alteração clínica importante deve ocorrer sem possibilidade de auditoria.

---

## Auditoria

Registrar automaticamente:

- quem criou;
- quem editou;
- quem visualizou;
- quem finalizou.

Informações mínimas:

- usuário;
- data;
- horário;
- endereço IP (quando aplicável);
- estação de trabalho (quando aplicável).

---

## Histórico de Eventos

Exemplo:

```text
08:12 Exame recebido

08:25 Médico abriu exame

08:41 Laudo salvo

08:47 Laudo finalizado

08:49 Impressão realizada

08:55 Download realizado
```

Objetivo:

Permitir rastreabilidade completa do exame.

---

## Controle de Permissões

Perfis previstos

- Administrador
- Diretor
- Médico
- Secretária
- Financeiro

O modelo definitivo permanece em estudo.

---

# Fase 1.8 — Gestão Operacional

## Objetivo

Transformar o MedCore em uma ferramenta de gestão para coordenadores e diretores.

---

## Dashboard Operacional

Indicadores previstos

- Exames do dia
- Pendentes
- Em laudagem
- Finalizados
- Urgentes

---

## Indicadores

Exemplos

- Tempo médio de laudo
- Tempo médio de espera
- Produção por médico
- Produção por unidade
- SLA
- Exames críticos

---

## Fila Operacional

Estados previstos

Recebido

↓

Distribuído

↓

Em análise

↓

Em laudagem

↓

Finalizado

↓

Entregue

---

# Fase 2.0 — Plataforma Comercial

## Objetivo

Transformar o MedCore em um produto comercial completo.

---

## Financeiro

Objetivo

Eliminar sistemas paralelos para gestão financeira.

Relacionamentos previstos

Exame

↓

Laudo

↓

Médico

↓

Pagamento

↓

Repasse

Indicadores

- Produção médica
- Valor por laudo
- Faturamento
- Custos
- Receita líquida

---

## Multi-Hospital

Estrutura prevista

Hospital A

Hospital B

Hospital C

Cada instituição deve possuir isolamento completo dos próprios dados.

---

## Portal do Cliente

Estudos futuros

Permitir

- download de laudos;
- consulta de exames;
- histórico do paciente.

---

## Assinatura Digital

Integração futura com

- ICP-Brasil
- Certificados médicos

---

# Fase 2.5 — PACS Avançado

## Comparação de Exames

Visualização simultânea

```text
Exame Atual

|

Exame Anterior
```

Objetivo

Facilitar avaliação da evolução clínica.

---

## MPR

Reconstruções

- Axial
- Coronal
- Sagital

Geradas dinamicamente.

---

## Reconstrução 3D

Visualização volumétrica.

---

## Sincronização de Viewers

Mover vários exames simultaneamente.

---

## Estudos Históricos

Permitir comparação da evolução clínica durante anos.

---

# LAB #009 — Campos Estruturados do Exame

Status

A avaliar.

Proposta

Adicionar ao Exame

- região anatômica;
- prioridade;
- modalidade estruturada.

Adicionar ao Laudo

- médico responsável.

Objetivo

Melhorar filtros, indicadores e histórico clínico.

---

# LAB #010 — Auditoria e Reedição de Laudos

Status

A avaliar.

Objetivo

Permitir reedição controlada de laudos finalizados.

Fluxo proposto

Workspace

↓

Modo Consulta

↓

Solicitação de edição

↓

Nova versão

↓

Registro de auditoria

Toda alteração deverá registrar

- usuário;
- data;
- motivo;
- versão anterior;
- versão nova.

---

## Decisão Temporária da Versão 1.5

Enquanto o fluxo definitivo não existir

Workspace de exames FINALIZADOS abre em modo consulta.

Viewer permanece totalmente funcional.

Campos de edição permanecem bloqueados.

Essa decisão deverá ser removida quando o fluxo definitivo de auditoria for implementado.

---

# Ideias em Investigação

As ideias abaixo ainda não possuem prioridade oficial.

Permanecem em estudo.

## Inteligência Artificial

Possibilidades

- auxílio à escrita do laudo;
- organização automática de exames;
- identificação de inconsistências;
- apoio ao preenchimento de templates.

Nenhuma decisão de implementação foi tomada.

---

## Workspace Inteligente

Possíveis funcionalidades

- lembrar ferramentas favoritas;
- restaurar sessão anterior;
- layouts personalizáveis;
- presets por modalidade.

---

## Produtividade

Ideias futuras

- comandos rápidos;
- pesquisa universal;
- favoritos;
- abertura dos exames mais recentes.

---

## Dashboard Médico

Possibilidades

- exames concluídos;
- tempo médio;
- produtividade diária;
- histórico pessoal.

---

# Estrutura Multi-Hospital

Em estudo.

Objetivos

Cada hospital poderá possuir

- médicos;
- usuários;
- configurações;
- integrações;
- indicadores.

Um médico poderá atuar em múltiplos hospitais.

Sempre respeitando permissões individuais.

---

# Sistema Financeiro

Em estudo.

Objetivos

Calcular automaticamente

- produção;
- valores;
- impostos;
- repasses;
- participação do sistema.

Sem necessidade de preenchimento manual.

---

# Segurança

Princípios futuros

- RBAC completo;
- menor privilégio;
- isolamento por hospital;
- auditoria obrigatória;
- rastreabilidade completa.

---

# Perguntas para Validação com Usuários

Estas perguntas deverão ser respondidas durante entrevistas com médicos e gestores.

## Fluxo Médico

- Quantas séries normalmente existem em uma TC?
- O scroll é realmente o método mais utilizado?
- Quais ferramentas são usadas diariamente?
- O que mais incomoda no sistema atual?
- Quais funcionalidades nunca são utilizadas?

---

## Fluxo Operacional

- Como os exames chegam hoje?
- Quem distribui exames?
- Existe fila automática?
- Existe SLA?
- Como a produtividade é medida?

---

## Fluxo Financeiro

- O pagamento é por exame?
- Por laudo?
- Por modalidade?
- Existe repasse automático?
- Existem regras diferentes por hospital?

---

# Filosofia de Crescimento

O MedCore deve crescer por evolução incremental.

Antes de criar qualquer novo módulo deve-se perguntar:

- este problema pode ser resolvido evoluindo algo que já existe?
- existe código reaproveitável?
- existe validação com usuário real?
- esta funcionalidade reduz trabalho?
- vale o custo de manutenção?

Se a resposta for "não", a funcionalidade permanece no LAB.

---

# Critério para Comercialização

Antes da primeira demonstração comercial, o Workspace Médico deverá ser capaz de substituir o fluxo principal realizado em sistemas de radiologia tradicionais.

Como referência mínima, o sistema deve oferecer:

- navegação entre slices;
- múltiplas séries reais;
- histórico clínico integrado;
- proteção contra perda de laudo;
- ferramentas básicas de visualização e medição;
- estabilidade em estudos grandes;
- fluxo completo de laudagem.

A partir desse ponto, o MedCore deixa de ser apenas um projeto de desenvolvimento e passa a ser um produto validável em ambiente hospitalar.

---

# Regra de Atualização

Este documento registra:

- ideias;
- pesquisas;
- hipóteses;
- backlog;
- experimentos;
- arquitetura futura;
- funcionalidades em estudo.

Nada aqui representa comportamento oficial do sistema até ser promovido formalmente para o MEDCORE_CORE_CONTEXT.