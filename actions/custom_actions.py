from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from typing import List
import logging

# Configuração do logger
logger = logging.getLogger(__name__)

class ActionLogFallback(Action):
    def name(self) -> str:
        return "action_log_fallback"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> List[EventType]:
        # Registrar o fallback no log
        user_message = tracker.latest_message.get('text')
        intent = tracker.latest_message.get('intent', {}).get('name')
        confidence = tracker.latest_message.get('intent', {}).get('confidence')

        # Log de aviso
        logger.warning(f"Fallback occurred for message: {user_message}, intent: {intent}, confidence: {confidence}")

        # Salvar o fallback no arquivo fallback_log.txt
        fallback_log_path = "C:/Users/Project/Desktop/lhama/logs/fallback_log.txt"
        with open(fallback_log_path, "a", encoding="utf-8") as file:
            file.write(f"Fallback for message: {user_message}, intent: {intent}, confidence: {confidence}\n")
        
        # Enviar mensagem de fallback para o usuário
        dispatcher.utter_message(response="utter_fallback")  # Corrigi de template para response

        return []
