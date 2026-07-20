# MEDCORE_CORE_CONTEXT.md

# Função

Representar a base oficial de conhecimento do MedCore.

Este documento responde à pergunta:

> **"Como o MedCore funciona hoje e quais decisões já foram oficialmente aprovadas?"**

Tudo que está registrado aqui é considerado parte oficial do projeto.

Ideias, pesquisas, hipóteses, backlog, roadmap e funcionalidades ainda em validação pertencem exclusivamente ao MEDCORE_LAB.md.

---

# Objetivo

O MedCore é uma plataforma hospitalar desenvolvida em Django para gerenciamento de usuários, pacientes, exames, imagens médicas, laudos e processos clínicos.

Seu foco inicial é a radiologia, utilizando exames DICOM como principal área de atuação.

O objetivo do projeto é reduzir a quantidade de sistemas utilizados pelos profissionais da saúde, concentrando o fluxo operacional em uma única plataforma integrada.

O MedCore inspira-se em sistemas PACS, RIS e plataformas comerciais consolidadas, porém busca construir uma solução própria baseada na compreensão dos fluxos reais de trabalho, e não na simples reprodução de funcionalidades.

---

# Tecnologias

- Python 3.13.2
- Django 6.0.5
- SQLite
- PostgreSQL (planejado)
- HTML
- CSS puro
- JavaScript puro
- Cornerstone
- pydicom
- Pillow
- Node.js
- npm
- Git
- GitHub

## Decisões Técnicas

- Não utilizar Bootstrap.
- Manter identidade visual própria.
- Priorizar controle total sobre a interface.
- Utilizar tema escuro como padrão do sistema.

---

# Estrutura Atual dos Apps

- usuarios
- medicos
- pacientes
- atendimentos
- consultas
- secretarias
- dashboard
- exames

---

# Modelo Conceitual

```text
Usuario
 ↓
Medico (OneToOne)

Paciente

Exame
 ↓
Estudo DICOM
 ↓
Séries DICOM
 ↓
Slices DICOM
 ↓
Preview PNG
 ↓
Workspace Médico
 ↓
Laudo
```

Este modelo representa a arquitetura oficial aprovada do MedCore.

Toda evolução futura deve preservar esta organização conceitual.

---

# Decisões Estruturais

## Usuário

Usuário é a entidade central do sistema.

Perfis como Médico, Secretária, Administrador ou Financeiro representam responsabilidades associadas ao usuário.

---

## Médico

Relacionamento atual:

```text
Usuario
    │
OneToOne
    │
Medico
```

Informações atuais:

- CRM
- Especialidade
- Telefone

---

## Paciente

Pacientes não dependem de autenticação.

Essa decisão representa o funcionamento real de ambientes hospitalares, onde normalmente milhares de pacientes não acessam diretamente o sistema.

---

## Consulta e Atendimento

Consulta representa o agendamento.

Atendimento representa a execução clínica.

As duas entidades permanecem separadas por representarem etapas diferentes do fluxo hospitalar.

---

## Exames

O módulo de exames foi arquitetado para evoluir até um PACS completo.

Sua estrutura oficial é:

```text
Exame
 ↓
Estudo
 ↓
Séries
 ↓
Slices
```

Essa arquitetura representa o funcionamento real de tomografias, ressonâncias magnéticas e demais modalidades DICOM.

---

# Funcionalidades Existentes

## Usuários

- Cadastro de usuários
- Cadastro de médicos
- Cadastro de pacientes

---

## Exames

- Upload de arquivos DICOM
- Processamento via pydicom
- Geração automática de preview PNG
- Renderização DICOM utilizando Cornerstone

---

## Workspace Médico

O Workspace Médico representa a principal estação de trabalho do sistema.

Sua estrutura oficial é composta por:

- Toolbar
- Painel de séries
- Viewer DICOM
- Painel de histórico do paciente
- Painel de laudo
- Barra inferior de status

---

## Laudos

Estados suportados:

- Rascunho
- Finalizado

O sistema protege laudos finalizados contra alterações indevidas, utilizando a política operacional atualmente aprovada.

---

## PACS

Existe uma implementação inicial funcional do módulo PACS.

Sua evolução continuará sobre a arquitetura oficial Estudo → Séries → Slices.

---

# Fluxo Oficial de Laudagem

O fluxo operacional aprovado para o Workspace Médico é:

```text
Inbox
 ↓
Selecionar exame
 ↓
Abrir Workspace
 ↓
Visualizar exame
 ↓
Consultar histórico do paciente
 ↓
Produzir laudo
 ↓
Salvar
 ↓
Finalizar exame
```

Todo novo recurso implementado no Workspace deve respeitar esse fluxo.

---

# Diferencial Estratégico

O principal diferencial competitivo atualmente aprovado para o MedCore é a integração do histórico clínico do paciente diretamente no Workspace Médico.

Durante a produção do laudo, o médico deve conseguir consultar exames e laudos anteriores sem sair da tela principal.

Esse comportamento faz parte da identidade do produto.

---

# Filosofia do Workspace Médico

O Workspace Médico é o núcleo operacional do MedCore.

Toda funcionalidade implementada nessa tela deve seguir os seguintes objetivos:

- reduzir tempo de laudagem;
- reduzir troca de telas;
- reduzir quantidade de cliques;
- reduzir perda de informações;
- permitir comparação entre exames;
- manter o médico concentrado na imagem;
- evitar ações irreversíveis sem confirmação;
- simplificar o fluxo clínico.

Sempre que houver conflito entre complexidade técnica e produtividade do médico, deve-se priorizar a experiência do profissional.

---

# Princípios Arquiteturais

Toda evolução do MedCore deve respeitar os seguintes princípios:

- Evoluir funcionalidades existentes antes de criar novos módulos.
- Reaproveitar código sempre que possível.
- Evitar duplicação de lógica.
- Resolver problemas reais antes de implementar novas funcionalidades.
- Manter a arquitetura simples e incremental.
- Priorizar consistência sobre quantidade de recursos.
- A interface deve servir ao profissional da saúde, não ao desenvolvedor.
- Segurança é responsabilidade da aplicação.

---

# Filosofia do Produto

O MedCore é orientado pelos seguintes princípios:

- Entender antes de copiar.
- Fazer simples antes de fazer complexo.
- Evitar engenharia excessiva.
- Priorizar produtividade clínica.
- Priorizar segurança operacional.
- Reduzir retrabalho.
- Reduzir troca de sistemas.
- Reduzir cliques desnecessários.
- Toda funcionalidade deve justificar o custo de manutenção que adiciona ao projeto.

O objetivo do sistema é tornar o trabalho dos profissionais mais simples, rápido e seguro.

---

# Filosofia de Desenvolvimento

Toda alteração significativa deve seguir o protocolo oficial de desenvolvimento.

Antes da implementação deve-se:

- identificar arquivos afetados;
- explicar o objetivo da alteração;
- avaliar riscos;
- avaliar impacto arquitetural;
- verificar aumento de escopo;
- apresentar alternativas quando necessário;
- aguardar aprovação.

Após a implementação deve-se:

- documentar exatamente o que foi realizado;
- explicar como validar;
- registrar efeitos colaterais conhecidos;
- registrar oportunidades futuras de evolução.

---

# Princípio da Evolução Incremental

Antes da criação de qualquer novo módulo deve-se avaliar se o problema pode ser resolvido através da evolução de funcionalidades já existentes.

Prioridade de decisão:

1. Reaproveitar.
2. Evoluir.
3. Criar novo módulo.

Objetivos:

- reduzir duplicação;
- manter consistência arquitetural;
- diminuir custo de manutenção;
- facilitar aprendizado de novos desenvolvedores;
- preservar simplicidade.

---

# Princípios de Segurança

## Regra de Ouro

Cada usuário deve visualizar e manipular apenas informações relacionadas à sua responsabilidade operacional.

---

## Menor Privilégio

Todo usuário recebe apenas as permissões necessárias para executar sua função.

---

## Validação Obrigatória

Permissões devem ser verificadas obrigatoriamente em:

- Interface;
- Views;
- APIs;
- Consultas ao banco de dados.

A segurança nunca deve depender da boa-fé do usuário.

---

# Regra de Atualização

Este documento registra exclusivamente:

- arquitetura oficial;
- funcionalidades existentes;
- decisões aprovadas;
- princípios permanentes;
- comportamentos oficialmente aceitos.

Roadmaps, backlog, pesquisas, experimentos, funcionalidades em estudo e ideias futuras pertencem exclusivamente ao MEDCORE_LAB.md.