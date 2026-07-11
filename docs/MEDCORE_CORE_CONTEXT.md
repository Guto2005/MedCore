# MEDCORE_CORE_CONTEXT.md

## Função

Representar a verdade atual do projeto.

## Pergunta que este arquivo responde

**"Como o MedCore funciona hoje?"**

---

## Objetivo

Sistema hospitalar desenvolvido em Django para gerenciar exames, DICOMs, laudos médicos e usuários, com foco inicial em radiologia. Inspirado em Sonic DICOM, sistemas PACS, RIS e plataformas de radiologia reais.

## Tecnologias

- Python 3.13.2
- Django 6.0.5
- SQLite (plano futuro: PostgreSQL)
- HTML / CSS puro / JavaScript puro (sem Bootstrap — decisão consciente por identidade visual própria)
- Cornerstone (visualização DICOM)
- pydicom (processamento DICOM)
- Pillow (geração de preview PNG)
- Node.js / npm (dependência exigida pelo Cornerstone)
- Git / GitHub

## Apps

- usuarios
- medicos
- pacientes
- atendimentos
- consultas
- secretarias
- dashboard
- exames

## Modelo Conceitual Atual

```text
Usuario
 ↓
Medico (OneToOne)

Paciente

Exame
 ↓
DICOM
 ↓
Preview PNG
 ↓
Workspace
 ↓
Laudo
```

Decisões que sustentam esse modelo:
- Usuário é centralizado; Médico, Admin, Secretária etc. são especializações dele.
- Médico é `OneToOne` com Usuario e carrega CRM, especialidade e telefone.
- Paciente é separado e não depende de login (hospitais têm milhares de pacientes que não acessam o sistema).
- Consulta (agendamento) é separada de Atendimento (execução).
- Exames é módulo independente e escalável, pensado desde o início para DICOM.

## Funcionalidades Existentes

- Cadastro de usuários, médicos e pacientes (funcionando)
- Upload de exame DICOM
- Leitura/processamento DICOM via pydicom
- Geração de preview PNG
- Viewer Cornerstone renderizando DICOM real no navegador
- Workspace Médico (toolbar, painel de séries, viewer central, painel de laudo, status inferior)
- Estrutura de Laudos (rascunho / finalizado)
- Base PACS inicial

## Prioridade Imediata (MedCore 1.5)

**Objetivo principal:** finalizar a estação de trabalho de radiologia (Workspace Médico) até um nível utilizável em ambiente real, para validação com o primeiro médico usuário (Dr. Cristiano).

**Critério de aceite explícito da 1.5:** a tela de laudagem deve funcionar no padrão do sistema **Sonic DICOM**, com o diferencial de trazer o **histórico do paciente** (exames e laudos anteriores dele) visível ali mesmo no workspace — algo que o Sonic não oferece nativamente. Esse é o diferencial competitivo da 1.5, não um detalhe secundário.

Escopo desta etapa — nenhum módulo novo deve atrasá-la:
- Finalizar integração completa do Cornerstone
- Visualização correta de estudos DICOM (múltiplos slices reais, não os 6 arquivos repetidos atuais)
- Navegação entre slices
- Painel de séries dinâmico (hoje é fixo/hardcoded: "Série Principal", "Série Auxiliar", "Reconstrução")
- Ferramentas básicas: Zoom, Pan, Window/Level
- Campo de laudo integrado ao visualizador
- Painel de histórico do paciente (exames anteriores + laudos anteriores), no padrão visual do workspace atual

Fluxo alvo:
```text
Inbox → Selecionar exame → Abrir Workspace → Visualizar DICOM → Consultar Histórico do Paciente → Realizar Laudo → Salvar → Finalizar exame
```

Ao concluir e aprovar visualmente esta etapa: commit `feat: workspace de laudagem MedCore 1.5 (padrão Sonic + histórico do paciente)`.

## Gap Arquitetural Identificado (bloqueia o Financeiro)

Ao ler o código real (`usuarios/models.py`, `medicos/models.py`, `usuarios/views.py`), foi identificado que:

- O login (`login_view`) usa o sistema padrão do Django (`django.contrib.auth`, `request.user`), cujo modelo é `auth.User`.
- O model `Usuario` (app `usuarios`) é uma tabela **separada e desconectada** de `auth.User` — não existe `AUTH_USER_MODEL` customizado nem OneToOne entre eles.
- `Medico` está ligado a `Usuario`, não a `auth.User`.

**Consequência prática:** hoje não existe uma forma confiável de descobrir, a partir do médico logado (`request.user`), qual é o `Medico` correspondente. Isso é pré-requisito obrigatório para "o médico só mexe na própria tabela de preço" e para a produção financeira automática — sem isso, não dá pra isolar dados por médico logado.

**Correção necessária (pequena, aditiva, não quebra nada existente):** adicionar um campo `usuario_auth = models.OneToOneField(User, ...)` ligando `Medico` (ou `Usuario`) ao `auth.User` real usado no login.

## Pendências Técnicas (dívidas conhecidas)

- Estudos reais (hoje: 1 exame = 1 arquivo DICOM; realidade hospitalar: 1 exame = múltiplas séries = centenas de DICOMs)
- Painel de séries dinâmico (hoje é placeholder fixo)
- Slice counter real (hoje fixo em "1/1"; deveria refletir o total real, ex: "157/300")
- Scroll entre slices
- Zoom, Pan, Window/Level (botões existem na UI, sem função ligada ainda)
- Medidas e anotações (círculo, seta, texto sobre a imagem, sem alterar o DICOM original)
- Fullscreen e Histórico (botões existem, sem implementação/backend)
- PACS completo, Worklist, Query/Retrieve

## Filosofia

- Entender antes de copiar — nunca copiar sistemas prontos sem entender o funcionamento interno.
- Fazer simples agora para crescer depois; evitar engenharia excessiva e complexidade prematura.
- Cada módulo novo deve reduzir o número de sistemas que os profissionais precisam usar, concentrando o fluxo numa única plataforma.
- Tema escuro é decisão obrigatória (ambiente hospitalar, menos fadiga visual).
- Toda funcionalidade nova deve resolver um problema real identificado por médicos, secretárias, administradores ou outros profissionais da saúde — nunca implementada só por parecer interessante tecnicamente. Sempre que possível, validar com usuários reais antes de entrar no planejamento oficial (registrado em 11/07/2026).

## Princípios de Segurança (válidos desde já, independente de módulo)

- **Regra de ouro:** cada usuário só visualiza e manipula dados da sua própria função/responsabilidade. Nenhum usuário comum vê inbox, laudos ou dados financeiros de outro médico.
- Princípio do menor privilégio: cada usuário tem só o acesso estritamente necessário para sua função.
- A segurança não pode depender da boa-fé do usuário — permissões devem ser validadas em interface, views, APIs e consultas ao banco.

---

> Regra de atualização: este arquivo reflete apenas o que já está implementado e funcionando (ou é prioridade ativa de implementação). Nada do LAB entra aqui sem passar por análise e aprovação.