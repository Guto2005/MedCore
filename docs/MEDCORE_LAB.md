# MEDCORE_LAB.md

## Função

Laboratório de ideias.

## Pergunta que este arquivo responde

**"O que está sendo investigado?"**

Nada neste arquivo é regra oficial. Tudo deve ser analisado antes de migrar para o `MEDCORE_CORE_CONTEXT.md`.

## Fluxo

```text
IDEIA
 ↓
LAB
 ↓
ANÁLISE
 ↓
DECISÃO

      ↙      ↘

REPROVADO   APROVADO
     ↓          ↓
 Arquivado   CORE_CONTEXT
```

> Nota: no documento original a data registrada era **10/07/2026**, não 11/07 — mantive a data real do arquivo.

## Regra de Promoção LAB → CONTEXT

Sempre que uma ideia for promovida do LAB para o `MEDCORE_CORE_CONTEXT.md`, o registro de promoção deve conter obrigatoriamente:

1. **Qual problema real ela resolve** (não "parecia interessante tecnicamente").
2. **Quem solicitou** a funcionalidade (Gustavo, Dr. Cristiano, outro usuário real, etc.).
3. **Por que entrou no roadmap** naquele momento específico.

Isso preserva não só a decisão, mas o raciocínio que levou a ela — para que qualquer pessoa (ou IA) lendo o histórico depois entenda o "porquê", não só o "o quê".

## Filosofia de Evolução (regra de aceite de qualquer ideia nova)

Toda funcionalidade nova deve resolver um problema real identificado por médicos, secretárias, administradores ou outros profissionais da saúde — não deve ser implementada apenas por parecer interessante tecnicamente. Antes de entrar no planejamento oficial, precisa agregar valor comprovado ao fluxo de trabalho e, sempre que possível, ser validada com usuários reais. O MedCore cresce priorizando qualidade e utilidade prática, não quantidade de funcionalidades.

---


Ideias Futuras do MedCore (Backlog Estratégico)
Objetivo

Esta seção registra funcionalidades, módulos e diferenciais pensados para o futuro do MedCore.

Importante: estas ideias não fazem parte da prioridade atual de desenvolvimento. Elas existem para preservar a visão de longo prazo do projeto e evitar que boas ideias sejam esquecidas.

A prioridade permanece concluir um MVP sólido para validação com o primeiro médico usuário (Dr. Cristiano).

Prioridade Atual (MedCore 1.5)
Objetivo Principal

Finalizar a estação de trabalho de radiologia (Workspace Médico) até um nível utilizável em ambiente real.

Escopo
Finalizar integração completa do Cornerstone;
Implementar visualização correta de estudos DICOM;
Navegação entre slices;
Painel de séries dinâmico;
Ferramentas básicas (Zoom, Pan, Window/Level);
Campo de laudo integrado ao visualizador;
Fluxo completo:
Inbox

↓

Selecionar exame

↓

Abrir Workspace

↓

Visualizar DICOM

↓

Realizar Laudo

↓

Salvar

↓

Finalizar exame

Nenhum novo módulo deverá atrasar esta etapa.

O foco absoluto é entregar uma estação de laudo funcional para validação com o Dr. Cristiano.

Backlog Estratégico
1. Módulo Financeiro Integrado

Inspirado na necessidade observada durante o fluxo de trabalho do Dr. Cristiano.

Objetivo

Eliminar sistemas separados para controle financeiro.

Ao finalizar um laudo, o MedCore deverá registrar automaticamente:

Médico responsável;
Procedimento;
Convênio;
Valor;
Hospital;
Data;
Produção médica.

Posteriormente será possível gerar:

Relatórios;
PDF;
Excel;
Demonstrativos mensais;
Fechamento financeiro.

O médico apenas lauda.

O sistema realiza toda a contabilização automaticamente.

2. Cadastro de Procedimentos

Cada procedimento poderá possuir:

Código TUSS;
Nome;
Categoria;
Valor Particular;
Valor Convênio;
Valor SUS;
Especialidade.
3. Cadastro de Convênios

Tabela própria contendo:

Operadora;
Valores específicos;
Regras de cobrança.
4. Dashboard Financeiro

Indicadores por:

Médico;
Hospital;
Período;
Convênio;
Modalidade;
Receita;
Impostos;
Produção.
5. Odontologia

Novo módulo especializado para exames odontológicos.

Exemplos:

Tomografia Cone Beam (CBCT);
Radiografia panorâmica;
Telerradiografia;
Modelos 3D;
Planejamento de implantes.
6. Expansão para outras especialidades

Após validação da radiologia:

Cardiologia;
Neurologia;
Ortopedia;
Dermatologia;
Patologia;
Outras áreas médicas.
Filosofia do Produto

O MedCore não pretende apenas ser um visualizador DICOM.

O objetivo é tornar-se uma plataforma integrada para profissionais da saúde, unificando:

Visualização de exames;
Laudos;
Gestão de pacientes;
Gestão médica;
Financeiro;
Relatórios;
Administração.

Cada novo módulo deverá reduzir o número de sistemas utilizados pelos profissionais, concentrando o fluxo de trabalho em uma única plataforma.

Roadmap Simplificado
MedCore 1.5
↓
Workspace Médico completo
(Cornerstone + Laudo)

↓

Validação com Dr. Cristiano

↓

Primeiro uso real

↓

Correções

↓

MedCore 2.0

↓

Financeiro integrado

↓

Dashboard

↓

Odontologia

↓

Expansão para novas especialidades

↓

SaaS Multi-hospital


---

## LAB #009 - Campos Estruturados em Exame/Laudo (Região Anatômica, Prioridade, Médico Responsável)

**Origem:** discussão sobre o card de Histórico do Paciente no Workspace de Laudagem (11/07/2026).

**Contexto:** ao desenhar o card de histórico, ficou claro que hoje `Exame` só tem `tipo_exame` (texto livre) e `Laudo` não tem nenhum vínculo com o médico que o escreveu. Isso é suficiente pro card funcionar agora, mas limita indicadores futuros (ex: filtrar por prioridade, saber quem laudou sem abrir o laudo).

**Proposta:**
- `Exame.regiao_anatomica` (opcional, estruturado)
- `Exame.prioridade` (opcional — ex: Rotina/Urgente/Emergência)
- `Laudo.medico` (FK para `Medico`, nullable)

**Por que não entrou na 1.5:** aumentaria o escopo da entrega atual sem resolver um problema real e urgente hoje — o `tipo_exame` já cobre a necessidade imediata do card de histórico.

**Status:** A AVALIAR

---

## LAB #010 - Edição de Laudo Finalizado + Trilha de Auditoria

**Origem:** discussão sobre a tela read-only de exame antigo, no fluxo do Histórico do Paciente (11/07/2026).

**Problema identificado:** bloquear completamente a edição de um laudo já finalizado pode gerar retrabalho real — médicos às vezes precisam corrigir um laudo depois de finalizado (e muitos laudos já foram exportados/impressos até esse ponto). Uma regra rígida de "nunca editar" não reflete o fluxo de trabalho real.

**Proposta para versão futura:**
- Workspace operando em dois modos: **Edição** e **Consulta**.
- Somente o médico responsável pelo laudo pode editá-lo após finalizado.
- Toda alteração pós-finalização gera um registro de auditoria contendo, no mínimo:
  - Quem realizou a alteração;
  - Quando foi realizada;
  - O que foi alterado;
  - Versão anterior do laudo;
  - Motivo da alteração (configurável conforme a política de cada hospital).

**Por que não entrou na 1.5:** é uma regra de negócio sensível (mexe com integridade de laudo médico/legal) que merece discussão própria, não uma decisão tomada de passagem dentro de outra entrega.

**Status:** A AVALIAR — nenhuma regra de bloqueio de edição será implementada na 1.5.

---

## Ideias em Avaliação — Versão 1.6

**Registradas em 11/07/2026.** Todas marcadas "A Avaliar" — nenhuma tem compromisso de implementação imediata e nenhuma deve aumentar o escopo da 1.5.

> Nota: esta lista expande e formaliza a seção "Regras de Negócio Planejadas" já registrada mais abaixo neste arquivo — não a substitui, ambas continuam válidas como registro histórico da mesma linha de raciocínio.

- **RBAC completo e configurável por hospital**: sistema de autenticação e permissões baseado em papéis, onde cada hospital pode configurar quais funcionalidades cada cargo enxerga/usa. Permissões não devem ficar fixas no código.
- **Perfis padrão iniciais**: Administrador, Diretor, Médico, Secretária — com possibilidade de adicionar novos cargos futuramente.
- **Estrutura Multi-Hospital com isolamento completo**: cada instituição vê apenas seus próprios pacientes, exames, usuários, configurações e dados administrativos.
- **Médico em múltiplos hospitais**: um mesmo médico pode atender vários hospitais, recebendo exames de instituições diferentes num único Workspace, respeitando as regras de permissão de cada uma.
- **Configuração de servidores de origem dos exames** (integrações futuras).
- **Fluxo de edição de laudos com auditoria completa** — ver LAB #010.
- **Versionamento de laudos** — ver LAB #010.
- **Workspace em dois modos (Edição / Consulta)** — ver LAB #010.
- **Revisão da modelagem do Exame** (região anatômica, prioridade, médico responsável, outros atributos a identificar) — ver LAB #009.

---

## Regras de Negócio Planejadas (Permissões, Multi-Hospital, Financeiro)

> Estas regras descrevem um sistema de hospitais múltiplos, perfis (Diretor, Financeiro) e módulo financeiro que **ainda não existem** nos apps atuais do MedCore (`usuarios`, `medicos`, `pacientes`, `atendimentos`, `consultas`, `secretarias`, `dashboard`, `exames`). Por isso ficam no LAB até serem implementadas e migradas para o CORE_CONTEXT.

# Estrutura de Hospitais

O sistema deve permitir múltiplos hospitais.

Cada hospital possui:

* Nome.
* Identificação.
* Configurações de integração.
* Médicos vinculados.

Relacionamento:

* Um hospital pode possuir vários médicos.
* Um médico pode atuar em vários hospitais.

Modelo conceitual:

Hospital ↔ Médico

Relacionamento muitos-para-muitos.

---

# Estrutura de Usuários

O sistema deve possuir separação de funções e permissões.

Perfis previstos:

## Administrador

Possui acesso total.

Responsabilidades:

* Gerenciar usuários.
* Gerenciar hospitais.
* Gerenciar integrações.
* Gerenciar permissões.
* Configurações gerais do sistema.

---

## Diretor

Possui visão gerencial.

Responsabilidades:

* Visualizar indicadores.
* Visualizar produção médica.
* Visualizar relatórios financeiros.
* Visualizar estatísticas dos hospitais sob sua gestão.

Não deve alterar laudos médicos.

---

## Médico

Responsabilidades:

* Receber exames.
* Visualizar inbox autorizado.
* Elaborar laudos.
* Assinar laudos.
* Acompanhar produção financeira própria.

Restrições:

* Não visualizar dados de outros médicos.
* Não acessar hospitais sem vínculo.

---

## Financeiro

Responsabilidades:

* Consultar faturamento.
* Consultar pagamentos.
* Gerar relatórios financeiros.
* Acompanhar produção médica.

Não possui acesso clínico desnecessário.

---

# Sistema de Inbox

O inbox é individual e controlado por permissões.

Regras:

* Cada médico visualiza apenas os exames destinados a ele.
* O sistema deve impedir acesso cruzado.
* Hospitais podem direcionar exames para médicos específicos.

Configuração prevista:

Cada médico poderá definir:

* Hospitais autorizados.
* Destino de importação DICOM.
* Preferências operacionais.

---

# Fluxo de Exames e Laudos

Fluxo principal:

DICOM recebido
↓
Inbox do médico autorizado
↓
Análise médica
↓
Criação do laudo
↓
Assinatura
↓
Registro financeiro

O laudo é o núcleo operacional do sistema.

---

# Sistema Financeiro

O financeiro depende diretamente da produção de laudos.

Objetivos:

* Calcular quantidade de laudos produzidos.
* Calcular valor bruto.
* Calcular custos operacionais.
* Calcular participação do sistema.
* Calcular impostos.
* Calcular valor líquido.

Indicadores desejados:

* Total de laudos.
* Receita gerada.
* Receita líquida.
* Receita por hospital.
* Receita por médico.
* Custos operacionais.

---

# Filosofia de Segurança

O MedCore deve operar sob o princípio do menor privilégio.

Todo usuário deve possuir apenas os acessos estritamente necessários para executar suas funções.

A segurança não deve depender da boa-fé do usuário.

A aplicação deve validar permissões em:

* Interface.
* Views.
* APIs.
* Consultas ao banco de dados.

---

# Direção de Crescimento

O MedCore deve evoluir para uma plataforma hospitalar completa contendo:

* Gestão de DICOM.
* Gestão de laudos.
* Gestão de usuários.
* Gestão hospitalar.
* Gestão financeira.
* Relatórios gerenciais.
* Integrações médicas.
* Inteligência Artificial aplicada ao diagnóstico.
* Escalabilidade para múltiplas instituições.

Toda nova funcionalidade deve respeitar os pilares:

1. Segurança.
2. Escalabilidade.
3. Simplicidade operacional.
4. Separação de responsabilidades.
5. Privacidade dos dados.