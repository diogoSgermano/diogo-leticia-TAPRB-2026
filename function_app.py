import logging
import azure.functions as func
import logging


app = func.FunctionApp()

#timer trigger

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def tapr6_timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.') 


#http trigger
@app.route(route="imprimir", methods=["GET"])
def imprimir_parametro(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processando requisição HTTP.")

    nome = req.params.get("nome")

    if not nome:
        return func.HttpResponse(
            "Informe o parâmetro 'nome'. Exemplo: ?nome=Diogo",
            status_code=400
        )

    return func.HttpResponse(
        f"Parâmetro recebido: {nome}",
        status_code=200
    )
