# SwiftMailer
SwiftMailer é uma aplicação de automação de emails que envia mensagens personalizadas em HTML para múltiplos destinatários com eficiência e discrição.

## Funcionalidades
* Envio de emails automáticos com conteúdo em HTML.
* Suporte para anexar imagens e outros tipos de arquivos.
* Capacidade de enviar emails para múltiplos destinatários usando a lista de cópia oculta (BCC) para manter a privacidade.
* Configuração simples e rápida com servidores SMTP de sua escolha.

## Requisitos
* Python 3.6 ou superior.
* Acesso a um servidor SMTP para enviar emails.
* Senha de aplicativo ou método de autenticação seguro, especialmente ao usar o Gmail ou outros provedores.
* 
## Configuração
Clone este repositório para o seu computador:
* shell
* Copy code
* git clone https://github.com/Marquezbertin/swiftmailer.git

Navegue até o diretório do projeto:
* shell
* Copy code
* cd swiftmailer

## Configure as configurações do servidor SMTP no arquivo de script:
* Substitua as configurações smtp_server, smtp_port, smtp_user e smtp_password com as credenciais do servidor SMTP que deseja usar.
* Altere os destinatários na lista de BCC (bcc_list) conforme necessário.
* Personalize o conteúdo do email no script, incluindo o conteúdo HTML, assunto e imagem, conforme desejado.

## Uso
Para usar o SwiftMailer, execute o script Python:
* shell
* Copy code
* python swiftmailer.py

Os emails serão enviados para os destinatários especificados na lista de BCC.

## Contribuição
Contribuições são bem-vindas! Se você deseja contribuir com este projeto, por favor, faça um fork deste repositório e envie um pull request com suas mudanças.

## Licença
Este projeto é licenciado sob a MIT License, permitindo o uso, modificação e distribuição livre do código.

## Contato
Para perguntas ou sugestões, entre em contato em bertinmarquez84@gmail.com.

