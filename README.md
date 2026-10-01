# DevSecOps Scan

Projeto desenvolvido para demonstrar a integração de práticas de segurança ao processo de CI/CD, aplicando os conceitos de DevSecOps e Shift Left.

## Objetivo

Implementar uma pipeline automatizada capaz de executar testes, análise de código, análise de dependências e análise dinâmica da aplicação.

## Tecnologias utilizadas

- Python
- Flask
- Pytest
- Docker
- GitHub Actions
- Semgrep
- pip-audit
- OWASP ZAP

## Arquitetura da solução

O fluxo da pipeline é:

```text
Push / Pull Request
        |
        v
GitHub Actions
        |
        +--> Testes automatizados - Pytest
        |
        +--> SAST - Semgrep
        |
        +--> SCA - pip-audit
        |
        +--> Build da aplicação - Docker
        |
        +--> DAST - OWASP ZAP
        |
        v
Resultado da análise
