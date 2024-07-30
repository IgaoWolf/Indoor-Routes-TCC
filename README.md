# Indoor-Routes-TCC

Este guia fornece um passo a passo para instalar e configurar o Nginx no seu projeto Indoor-Routes-TCC. O Nginx será usado como servidor web para servir sua aplicação.

## 1. Atualizar o Sistema

Primeiro, atualize os pacotes do sistema:

```bash
sudo apt update && sudo apt upgrade -y
```

## 2. Instalar Dependências

Instale as dependências necessárias:

```bash

sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring
```

## 3. Adicionar a Chave de Assinatura do Nginx

Baixe e adicione a chave de assinatura do Nginx:

```bash

curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
```

Verifique se a chave foi importada corretamente:

```bash

gpg --dry-run --quiet --no-keyring --import --import-options import-show /usr/share/keyrings/nginx-archive-keyring.gpg
```

## 4. Adicionar Repositórios do Nginx

Adicione os repositórios do Nginx para Ubuntu:

```bash

echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" | sudo tee /etc/apt/sources.list.d/nginx.list

echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" | sudo tee /etc/apt/sources.list.d/nginx.list
```

Configure as preferências para priorizar os pacotes do Nginx:

```bash

echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" | sudo tee /etc/apt/preferences.d/99nginx
```

## 5. Atualizar a Lista de Pacotes

Atualize a lista de pacotes novamente para incluir os repositórios do Nginx:

```bash

sudo apt update
```

## 6. Instalar o Nginx

Instale o Nginx:

```bash

sudo apt install nginx
```
