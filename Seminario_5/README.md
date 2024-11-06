# Casa Inteligente - MQTT e CoAP Demo

Este projeto demonstra a integração de sensores ambientais e dispositivos de controle em uma casa inteligente usando os protocolos MQTT e CoAP.

## Arquitetura

- **Sensor Ambiental** (MQTT Publisher): Simula sensores que coletam dados de temperatura, umidade e luz
- **Central de Controle** (MQTT Subscriber + CoAP Client): Processa dados dos sensores e controla dispositivos
- **Termostato** (CoAP Server): Simula um dispositivo de controle de temperatura

## Pré-requisitos

`bash # Python 3.7+ python3 --version # Pip para instalação de pacotes pip --version `

## Instalação

1. Clone o repositório:
   `bash git clone [URL_DO_REPOSITÓRIO] cd casa-inteligente `
2. Instale as dependências Python:
   `bash pip install paho-mqtt aiocoap `
3. Instale e configure o broker MQTT (Mosquitto):
   Para Ubuntu/Debian:
   `bash sudo apt-get update sudo apt-get install mosquitto mosquitto-clients `
   Para Fedora:
   `bash sudo dnf install mosquitto `
4. Inicie o serviço Mosquitto:
   `bash sudo systemctl start mosquitto sudo systemctl enable mosquitto # Para iniciar automaticamente no boot ` 5. Verifique se o Mosquitto está rodando:
   `bash sudo systemctl status mosquitto `

## Executando o projeto Abra três terminais diferentes e execute os componentes na seguinte ordem:

1. Terminal 1 - Inicie o Termostato (Servidor CoAP):
   `bash python thermostat.py `
2. Terminal 2 - Inicie a Central de Controle:
   `bash python control_center.py `
3. Terminal 3 - Inicie o Sensor Ambiental: `bash python sensor.py `

## Funcionamento

- O sensor ambiental publica dados a cada 5 segundos via MQTT - A central de controle recebe os dados e verifica a temperatura - Se a temperatura exceder 25°C, a central envia um comando via CoAP para ligar o termostato - O termostato responde às requisições CoAP alterando seu estado
