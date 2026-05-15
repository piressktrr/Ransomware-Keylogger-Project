# Ransomware & Keylogger — Cybersecurity Bootcamp Projects
 
Projetos desenvolvidos durante o **Bootcamp de Cibersegurança da Riachuelo pela DIO** (40 horas), com o objetivo de compreender na prática como funcionam dois dos vetores de ataque mais comuns no cenário de segurança da informação.
 
> **Aviso:** todos os projetos contidos neste repositório foram desenvolvidos exclusivamente para fins educativos, em ambientes locais e controlados (máquinas virtuais). Nenhum código deve ser executado fora de um ambiente isolado. O uso indevido é de responsabilidade exclusiva do executor.
 
---
 
## Projetos
 
### Simulador de Cifragem de Arquivos (Ransomware)
 
Simulação do comportamento de um ransomware real: o script cifra arquivos de um diretório alvo e disponibiliza um segundo script para a decifragem, revertendo o processo por completo.
 
O objetivo é entender como ataques de ransomware funcionam internamente — e consequentemente, como sistemas de defesa e backups podem mitigá-los.
 
**Biblioteca utilizada:** `cryptography`
 
**Funcionamento:**
- `encrypt.py` — gera uma chave simétrica e cifra os arquivos do diretório alvo
- `decrypt.py` — utiliza a chave gerada para decifrar os arquivos e restaurar o estado original
---
 
### Keylogger
 
Script que captura e registra tudo que é digitado pelo usuário, armazenando os dados localmente em um arquivo de log.
 
O objetivo é compreender como keyloggers atuam como vetor de captura de credenciais e dados sensíveis, base para entender ataques de engenharia social e exfiltração de dados.
 
**Biblioteca utilizada:** `pynput`
 
**Funcionamento:**
- Monitora eventos de teclado em tempo real
- Registra as teclas pressionadas em um arquivo `.txt` local
---
 
## Tecnologias
 
- Python 3
- `cryptography` — cifragem simétrica de arquivos
- `pynput` — captura de eventos de teclado
---
 
## Ambiente recomendado
 
- Sistema operacional: Ubuntu Server ou Kali Linux (via máquina virtual)
- Ferramenta de virtualização: VirtualBox ou VMware
- Nunca execute em máquinas físicas fora de um ambiente controlado
---
 
## Contexto
 
Este repositório faz parte do portfólio desenvolvido durante o **Bootcamp de Cibersegurança da Riachuelo pela DIO**, curso com 40 horas de duração que abordou desde fundamentos de redes e Linux até pentest, OSINT e princípios de segurança ofensiva e defensiva.
 
---
 
## Autor
 
**Pedro** — estudante de Análise e Desenvolvimento de Sistemas na FATEC São Paulo
 
[LinkedIn](https://www.linkedin.com/in/piressktrr) · [GitHub](https://github.com/piressktrr)
