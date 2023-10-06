# Calculadora usando Python hospedada no AZURE FUNCTIONS

Neste projeto, desenvolvi uma **calculadora**  usando Python e a hospedei no [Azure Functions](https://learn.microsoft.com/pt-br/azure/azure-functions/functions-overview).

## Visão Geral

A calculadora pode realizar operações matemáticas básicas, como adição, subtração, multiplicação e divisão. O objetivo deste projeto é demonstrar como criar e hospedar uma função Python no Azure Functions.

### Passos seguidos: 
* Usei o Visual Studio Code para criar a função em Python
* Testei o código localmente usando o Postman
* Implantei no ambiente sem servidor do Azure Functions

## Requisitos

* Conta do Azure com uma assinatura ativa
* [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools), versão local do Azure Functions, fornece comandos para criar funções, se conectar ao Azure e implantar projetos de função
* [Python](https://docs.python.org/pt-br/3/tutorial/), linguagem de programação de alto nível
* [Visual Studio Code](https://code.visualstudio.com/), editor de código
* [Postman](https://www.postman.com/), ferramenta com a função de testar e desenvolver APIs



## Implantação

- Hospedado no Azure Function: [https://calculadora-python.azurewebsites.net/api/Calculadora](https://calculadora-python.azurewebsites.net/api/Calculadora).

## Testando a Calculadora

Você pode testar a calculadora usando o Postman ou qualquer outra ferramenta de sua preferência. Basta fazer uma solicitação POST para o endpoint fornecido e passar os dados da operação que deseja realizar no corpo da solicitação.

  
* Testado no Postman:
<br>

![POSTMAN](https://user-images.githubusercontent.com/96353855/170143653-5e759be4-c675-4181-89b2-b8a3fe8e34b7.jpg)


