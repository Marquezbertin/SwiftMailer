import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'  # Para o Gmail
smtp_port = 587
smtp_user = 'bruno@mail.com'
smtp_password = 'Senha do app'  # Use uma senha de aplicativo ou outro método de autenticação seguro.

# Lista de destinatários em BCC
bcc_list = ['user1@mail.com', 'user2@mail.com', 'user3@mail.com', 'user4@mail.com', 'user5@mail.com']

# Crie uma mensagem, titulo
msg = MIMEMultipart()
msg['From'] = smtp_user
msg['To'] = 'bruno@mail.com'  # Você pode deixar em branco ou usar um valor genérico, pois os destinatários estão em BCC
msg['Subject'] = 'Teste aplicativo disparador email automático'

# Conteúdo do email em HTML, subistitua a imagem
html_content = """
<html>
<head></head>
<body>
    <h1>Olá,</h1>
    <p>Este é um email automático disparado por um robô.</p>
    <p>Voce pode inserir quantos emails quiser</p>
    <img src="imagem.jpg"> 
</body>
</html>
"""

# Adicione o conteúdo HTML à mensagem
part_html = MIMEText(html_content, 'html')
msg.attach(part_html)

# Adicione uma imagem
try:
    with open('imagem.jpg', 'rb') as img_file:
        img_data = img_file.read()
    img_part = MIMEImage(img_data)
    img_part.add_header('Content-ID', '<image1>')
    msg.attach(img_part)
except FileNotFoundError:
    print("Imagem não encontrada. Certifique-se de que o arquivo 'imagem.jpg' esteja no mesmo diretório que o script.")

# Tente enviar o email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, bcc_list, msg.as_string())
    print("Email enviado com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao enviar o email: {e}")
