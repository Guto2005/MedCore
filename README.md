# MedCore - Sistema de Gestão Hospitalar

## Objetivo

O MedCore é um sistema web desenvolvido para auxiliar clínicas, consultórios e profissionais da saúde no gerenciamento de pacientes, médicos, consultas, atendimentos e exames médicos, centralizando as informações em uma única plataforma.

---

## Tecnologias Utilizadas

* Python 3.13.2
* Django 6.0.5
* SQLite
* HTML5
* CSS3
* JavaScript
* PyDICOM
* Pillow (PIL)
* NumPy

---

## Funcionalidades

### Pacientes

* Cadastro
* Edição
* Exclusão
* Listagem

### Médicos

* Cadastro
* Edição
* Exclusão
* Listagem

### Consultas

* Agendamento
* Controle de status
* Visualização das próximas consultas

### Atendimentos

* Registro de prontuário
* Histórico de atendimentos por paciente
* Controle de status dos atendimentos

### Secretárias

* Cadastro
* Vinculação de médicos
* Edição de vínculos

### Usuários

* Sistema de login
* Perfil de usuário
* Alteração de senha
* Validações de segurança para senha

### Dashboard

* Total de pacientes
* Total de médicos
* Total de secretárias
* Total de atendimentos
* Atendimentos em aberto
* Atendimentos finalizados
* Atendimentos cancelados
* Consultas agendadas
* Consultas realizadas
* Próximas consultas

### Exames (PACS Inicial)

* Importação manual de exames DICOM
* Inbox de exames pendentes
* Controle de status dos exames

  * Pendente
  * Em Laudo
  * Finalizado
* Leitura de metadados DICOM
* Preview de exames médicos
* Sistema de laudos
* Salvamento de rascunhos
* Finalização de laudos
* Histórico de exames finalizados

---

## Diferenciais Implementados

Além dos requisitos obrigatórios propostos no desafio, o sistema conta com:

* Dashboard administrativo
* Controle completo de médicos
* Controle completo de consultas
* Controle de secretárias
* Sistema de autenticação
* Perfil de usuário
* Alteração segura de senha
* Interface moderna em tema escuro
* Organização modular utilizando múltiplas aplicações Django
* PACS inicial para gerenciamento de exames médicos
* Leitura de arquivos DICOM
* Sistema de laudos médicos
* Preview de exames por imagem

---

## Banco de Dados

O sistema utiliza SQLite para armazenamento e persistência das informações.

---

## Arquitetura

O projeto foi desenvolvido seguindo o padrão MTV (Model-Template-View) do framework Django, buscando organização, legibilidade e facilidade de manutenção.

### Aplicações Principais

* usuarios
* pacientes
* medicos
* consultas
* atendimentos
* secretarias
* dashboard
* exames

---

## Ambiente de Desenvolvimento

O projeto foi desenvolvido utilizando ambiente virtual Python (venv).

### Executar o Projeto

Ativar ambiente virtual:

Windows

```bash
venv\Scripts\activate
```

Executar servidor:

```bash
python manage.py runserver
```

Acessar:

```text
http://127.0.0.1:8000/
```

---

## Evolução do Projeto

### Versão 1.4

Implementação inicial do módulo PACS do MedCore.

Recursos adicionados:

* Importação de exames DICOM
* Inbox de exames
* Fluxo de laudos
* Salvamento de rascunhos
* Finalização de laudos
* Preview de imagens médicas
* Leitura de metadados DICOM utilizando PyDICOM

Esta versão estabelece a base para futuras integrações com servidores PACS, sistemas RIS e visualizadores médicos avançados.

---

## Próximos Passos

Planejamento da versão 1.5:

* Integração com Cornerstone
* Controle de permissões por perfil
* Médico responsável pelo laudo
* Auto preenchimento de dados via DICOM
* Auditoria de alterações
* Evolução do módulo PACS

---

## Conclusão

O MedCore atende aos requisitos propostos para o Projeto de Conclusão do Programa Desenvolvedor Trainee 2026 da BGMax Tecnologia.

Além dos requisitos obrigatórios, o sistema evoluiu para incluir funcionalidades voltadas ao ambiente clínico e hospitalar, como gerenciamento de exames médicos, fluxo de laudos e integração inicial com arquivos DICOM, servindo como base para futuras expansões do módulo PACS.
