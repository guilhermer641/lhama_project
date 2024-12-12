from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionHandleSupport(Action):
    def name(self):
        return "action_handle_support"

    def run(self, dispatcher, tracker, domain):
        # Aqui você pode processar a entrada do usuário ou simplesmente seguir adiante.
        # Por enquanto, apenas deixe passar para a próxima etapa.
        dispatcher.utter_message(text="Encaminhando seu atendimento...")
        return []





