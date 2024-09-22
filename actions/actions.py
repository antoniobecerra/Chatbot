# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk import Action, Tracker

class ActionPoliticaCalidad(Action):

    def name(self) -> str:
        return "action_politica_calidad"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Verifica si el usuario está pidiendo el certificado ISO
        certificado = list(tracker.get_latest_entity_values("certificado"))
        if certificado:
            dispatcher.utter_message(response="utter_politica_calidad_certificado")
        else:
            dispatcher.utter_message(response="utter_politica_calidad_general")
        return []
    

class ActionSendDropdown(FormValidationAction):
    def name(self) -> Text:
        return "action_lista_videos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = [
            {"label": "Marcadora Manual", "value": "/inform{'video_selected':'marcadora_manual'}"},
            {"label": "Marcadora Automática", "value": "/inform{'video_selected':'marcadora_automatica'}"},
            {"label": "Máquina de Corte y Recalcado", "value": "/inform{'video_selected':'maquina_corte_recalcado'}"},
            {"label": "Ensayo de Impacto", "value": "/inform{'video_selected':'ensayo_impacto'}"},
            {"label": "Prensa para Ensayos de Corte y Recalcado", "value": "/inform{'video_selected':'prensa_ensayos_corte_recalcado'}"},
            {"label": "Ensayo cíclico tracción-compresión sobre barra", "value": "/inform{'video_selected':'traccion_compresion_barra'}"}
        ]

        message = {
            "payload": "dropDown",
            "data": data
        }

        dispatcher.utter_message(
            text="Seleccione uno de los siguientes vídeos para ver más detalles:",
            json_message=message
        )

        return []
    
class ActionMostrarVideo(FormValidationAction):
    def name(self) -> Text:
        return "action_mostrar_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot_value = tracker.get_slot("video_seleccionado")
        
        if  slot_value == "Marcadora manual":
            video_url = "https://www.youtube.com/embed/BoIp-pjrsk4"
        elif slot_value == "Marcadora automática":
            video_url = "https://www.youtube.com/embed/5TEbhxk_Ll8&t=4s"
        elif slot_value == "Máquina de corte y recalcado":
            video_url = "https://www.youtube.com/embed/MmY02MKO3sI"
        elif slot_value == "Ensayo de impacto":
            video_url = "https://www.youtube.com/embed/biK7bZbCYfg"
        elif slot_value == "Prensa para ensayos de corte y recalcado":
            video_url = "https://www.youtube.com/embed/9QPz5mT5aPQ"
        elif slot_value == "Ensayo cíclico tracción-compresión sobre barra":
            video_url = "https://www.youtube.com/embed/BuiTKWtNOLI"
            
        else:
            video_url = ""

        if video_url != "":
            msg = { "type": "video", "payload": { "title": "Link name", "src": video_url} }

            dispatcher.utter_message(text=f"Aquí está el vídeo que seleccionó:",attachment=msg)
        else:
            dispatcher.utter_message(text="Ha habido un error. Disculpe las molestias. ¿Puedo ayudarle en algo más?")

        return []
    
class ActionServicios(Action):
    def name(self) -> Text:
        return "action_mostrar_servicios"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = [
            {
                "title": "Actualización de máquinas antiguas",
                "description": "Automatización y modernización de equipos de ensayo con controles antiguos para mejorar su rendimiento. \n"+
                "Podemos automatizar máquinas de cualquier marca, con sistema de control obsoleto o dañado, incorporando nuestra electrónica y software de control. Revisamos la mecánica, sustituyendo los elementos necesarios, y realizamos la puesta a punto."
            },
            {
                "title": "Mantenimiento",
                "description": "Servicio preventivo y correctivo para asegurar el correcto funcionamiento y prolongar la vida útil de las máquinas de ensayo."+
                "Proporcionamos para nuestros productos revisiones periódicas in situ, emisiones de informe, verificación de valores de medida y asistencia ténica en 24-48 horas."
            },
            {
                "title": "Calibraciones",
                "description": "Ofrecemos certificación y calibración de máquinas de ensayo con estándares trazables para mediciones de fuerza, desplazamiento y deformación. Nuestras capacidades incluyen carga entre 50 Kgf y 200 Tm en compresión, y entre 50 Kgf y 100 Tm en tracción. También calibramos transductores de desplazamiento (0-200 mm) y extensometría para deformaciones de hasta 50 mm."
            }
        ]

        message = {"payload": "collapsible", "data": data}

        dispatcher.utter_message(text="Servosis ofrece los siguientes servicios:", json_message=message)
        return []