import logging #modulo para registrar mensagens que deseja ver, permite sinalizar avisos e erros que ocorrem durante a execução da função

from orjson import loads, dumps   #orjson: serializa dataclass,datetime,numpy   loads: recebe uma string e retorna um objeto json   dumps: recebe um objeto json e retorna uma string
import azure.functions as func  


def main(req: func.HttpRequest) -> func.HttpResponse:  #define uma função chamada main, que recebe um parâmetro req do tipo func.HttpRequest e retorna um valor do tipo func.HttpResponse
    #HTTP: protocolo de comunicação HttpRequest:solicitacao que o usuario realiza ao servidor  HttpResponse: resposta que o servidor envia ao usuario
    logging.info('Calculadora')# relata eventos que podem ocorrer durante a operação de um programa

    data = loads(req.get_body())  # uma variavel chamada data que recebe uma string no corpo da solicitacao e converte em um objeto json
    try:  # tratando exceçoes  try: se nao houver excecao o except será ignorado e o codigo vai ser executado
        numero1 = data['a'] # na variavel chamada numero1 , recebe a resposta do usuario na forma de uma string e retorna um objeto json
        numero2 = data['b']
        operacao = data['op']
    except KeyError as e: # uma exceção que irá ser tratada
        return func.HttpResponse(  # se houver a excecao vai retornar uma mensagem de erro dizendo que não foi encontrado o que foi solicitado 
        #status code: erro do cliente, 400: o servidor não entendeu a requisição pois está com uma sintaxe inválida
        #mimetype: usado para indicar como o conteúdo deve ser tratado, nesse caso será tipo texto e subtipo json
            dumps({"error": f"Not found {e}"}), status_code=400, mimetype='text/json'  
          
        )
    
    if not isinstance(numero1, (int, float)):  
        #verifica se o objeto (primeiro argumento) é uma instância da classe(segundo argumento).
        #vai verificar se numero1 não é um int ou float. Se não for vai retornar a mensagem de erro
        #f-string: torna a interpolação de strings mais simples( o espaco reservado onde é substituido pelo valor correspondente)
        #r!: formata a string, nesse caso deixa o numero1 entre chaves
        return func.HttpResponse(
            dumps({"error": f"Ivalid value for a {numero1!r}"}), status_code=400, mimetype='text/json'  
        )

    if not isinstance(numero2, (int, float)):
        return func.HttpResponse(
            dumps({"error": f"Ivalid value for b {numero2!r}"}), status_code=400, mimetype='text/json'
        )

    if operacao == "soma":# se a operacao for igual a soma, recebe um json no campo numero1+numero2  e retorna na forma de uma string
        return func.HttpResponse(dumps({"result": numero1+numero2}), mimetype='text/json')
    if operacao == "subtracao":
        return func.HttpResponse(dumps({"result": numero1-numero2}), mimetype='text/json')
    if operacao == "multiplicacao":
        return func.HttpResponse(dumps({"result": numero1*numero2}), mimetype='text/json')  
    if operacao == "divisao":
        if numero2 == 0: # se o numero2 for igual a 0, retorna uma mensagem de erro 
            return func.HttpResponse(dumps({"error": "Divison by zero"}), status_code=400, mimetype='text/json')
        return func.HttpResponse(dumps({"result": numero1/numero2}), mimetype='text/json') 
    return func.HttpResponse(# caso o usuario nao digitar nenhuma das operacoes solicitadas, irá retornar uma mensagem de erro
       dumps({"error": "Invalid Operation"}), status_code=400, mimetype='text/json'
        )






