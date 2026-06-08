# MedCore - Sistema de Gestão Hospitalar

## Objetivo

O MedCore é um sistema web desenvolvido para auxiliar clínicas e consultórios médicos no gerenciamento de pacientes, médicos, consultas e atendimentos, centralizando as informações em uma única plataforma.

---

## Tecnologias Utilizadas

* Python 3.13.2
* Django 6.0.5
* SQLite
* HTML5
* CSS3
* JavaScript

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

---

## Banco de Dados

O sistema utiliza SQLite para armazenamento e persistência das informações.

---

## Arquitetura

O projeto foi desenvolvido seguindo o padrão MTV (Model-Template-View) do framework Django, buscando organização, legibilidade e facilidade de manutenção.

Aplicações principais:

* usuarios
* pacientes
* medicos
* consultas
* atendimentos
* secretarias
* dashboard

---

## Ambiente de Desenvolvimento

O projeto foi desenvolvido utilizando ambiente virtual Python (venv).

### Executar o projeto

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

## Conclusão

O MedCore atende aos requisitos propostos para o Projeto de Conclusão do Programa Desenvolvedor Trainee 2026 da BGMax Tecnologia e apresenta funcionalidades adicionais que ampliam sua utilização em ambientes clínicos e hospitalares.
