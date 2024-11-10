# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk import Action, Tracker
import json
from actions.functions import *


class ActionPoliticaCalidad(Action):

    def name(self) -> str:
        return "action_politica_calidad"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict
    ) -> list:
        # Verifica si el usuario está pidiendo el certificado ISO
        certificado = list(tracker.get_latest_entity_values("certificado"))
        if certificado:
            text = "En Servosis, contamos con la certificación ISO 9001, que asegura la calidad de nuestros procesos y productos. Puede descargar nuestro certificado aquí:"
            message = {
                "payload": "pdf_attachment",
                "title": "certificado ISO",
                "url": "https://www.servosis.com/wp-content/uploads/2024/04/Certificado-ISO_-9001_Servosis.pdf",
            }
            dispatcher.utter_message(text=text, json_message=message)
        else:
            text = "En Servosis, nuestra política de calidad se basa en la mejora continua de nuestros procesos y en proporcionar productos de alta calidad, siempre con un trato personalizado al cliente.\nNuestro objetivo principal es satisfacer tanto a nuestros clientes como a nuestros empleados, buscando la eficiencia y rentabilidad en todas nuestras actividades de diseño, fabricación, comercialización y mantenimiento de máquinas de ensayo y sus componentes.\nPara lograr esto, hemos implementado un Sistema de Calidad de acuerdo con la Norma UNE-EN ISO 9001 vigente, lo que nos compromete a cumplir con los requisitos de todas las partes implicadas en nuestro proceso. Nuestro equipo está comprometido con la identificación y análisis de riesgos y oportunidades, buscando siempre mejoras que nos lleven a la excelencia."
            dispatcher.utter_message(text=text)
        return []


# class ActionSendDropdown(FormValidationAction):
#     def name(self) -> Text:
#         return "action_lista_videos"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         data = [
#             {
#                 "label": "Marcadora Manual",
#                 "value": "Video marcadora manual",
#             },
#             {
#                 "label": "Marcadora Automática",
#                 "value": "Video marcadora automática",
#             },
#             {
#                 "label": "Máquina de Corte y Recalcado",
#                 "value": "Video máquina de corte y recalcado",
#             },
#             {
#                 "label": "Ensayo de Impacto",
#                 "value": "Video ensayo de impacto",
#             },
#             {
#                 "label": "Prensa para Ensayos de Corte y Recalcado",
#                 "value": "Video prensa para ensayos de corte y recalcado",
#             },
#             {
#                 "label": "Ensayo cíclico tracción-compresión sobre barra",
#                 "value": "Video ensayo cíclico tracción-compresión sobre barra",
#             },
#         ]

#         message = {"payload": "dropDown", "data": data}

#         dispatcher.utter_message(
#             text="Seleccione uno de los siguientes vídeos para ver más detalles:",
#             json_message=message,
#         )

#         return []


class ActionMostrarVideo(FormValidationAction):
    def name(self) -> Text:
        return "action_mostrar_video"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        slot_value = tracker.get_slot("video_seleccionado")
        print(f"El valor del slot es el siguiente:{slot_value}")

        if "marcadora manual" in slot_value.lower():
            video_url = "https://www.youtube.com/embed/BoIp-pjrsk4"
        elif any(keyword in slot_value.lower() for keyword in ["automatica", "automática"]):
            video_url = "https://youtu.be/5TEbhxk_Ll8"
        elif any(keyword in slot_value.lower() for keyword in ["maquina", "máquina"]) and (
            "corte" in slot_value.lower() or "recalcado" in slot_value.lower()
        ):
            video_url = "https://www.youtube.com/embed/MmY02MKO3sI"
        elif "impacto" in slot_value.lower():
            video_url = "https://www.youtube.com/embed/biK7bZbCYfg"
        elif "prensa" in slot_value.lower():
            video_url = "https://www.youtube.com/embed/9QPz5mT5aPQ"
        elif "ensayo cíclico" in slot_value.lower():
            video_url = "https://www.youtube.com/embed/BuiTKWtNOLI"

        else:
            video_url = ""

        if video_url != "":
            msg = {"type": "video", "payload": {"title": "Link name", "src": video_url}}

            dispatcher.utter_message(
                text=f"Aquí está el vídeo que seleccionó:", attachment=msg
            )
        else:
            dispatcher.utter_message(
                text="Ha habido un error. Disculpe las molestias. ¿Puedo ayudarle en algo más?"
            )

        return []


class ActionServicios(Action):
    def name(self) -> Text:
        return "action_mostrar_servicios"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        data = [
            {
                "title": "Actualización de máquinas antiguas",
                "payload": "Actualización de máquinas antiguas",
            },
            {"title": "Mantenimiento", "payload": "Mantenimiento"},
            {"title": "Calibraciones", "payload": "Calibraciones"},
        ]

        message = {"payload": "quickReplies", "data": data}

        text = (
            "Servosis ofrece servicios sobre actualización de máquinas antiguas, calibraciones y mantenimiento de equipos. \n"
            + "¿Sobre cuál le gustaría saber más?"
        )

        # Mostramos los servicios
        dispatcher.utter_message(text=text, json_message=message)

        return []


class ActionMostrarServicio(Action):
    def name(self) -> Text:
        return "action_mostrar_servicio"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        producto = next(tracker.get_latest_entity_values("producto"), None).lower()

        if (
            "actualización" in producto
            or "actualizacion" in producto
            or "actualizaciones" in producto
        ):
            producto = "actualización de máquinas antiguas"
        elif any(keyword in producto for keyword in ["calibr", "certif"]):
            producto = "calibraciones"

        with open("actions/servicios.json", "r", encoding="utf-8") as json_object:
            json_file = json.load(json_object)
            dispatcher.utter_message(text=json_file[producto])

        # Proporcionamos pdf sobre la reconversión de máquinas.
        if "actualización" in producto or "actualizaciones" in producto:
            text = "Puede ver más información sobre las reconversiones que realizamos de máquinas de ensayo en el siguiente pdf:"
            message = {
                "payload": "pdf_attachment",
                "title": "Servicio de reconversión de máquinas de ensayo",
                "url": "https://www.servosis.com/wp-content/uploads/2022/11/03-SV-SL-Automatizaciones.pdf",
            }

            dispatcher.utter_message(text=text, json_message=message)

        return []


class ActionMostrarTiposProductos(Action):
    def name(self) -> Text:
        return "action_mostrar_tipos_productos"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        data = [
            {"title": "Máquinas de ensayo", "payload": "maquinas_de_ensayo"},
            {"title": "Accesorios", "payload": "accesorios"},
        ]

        message = {"payload": "quickReplies", "data": data}

        dispatcher.utter_message(
            text="¿Sobre qué tipo de producto desea saber más?", json_message=message
        )

        return []


class ActionTipoProductoSeleccionado(Action):
    def name(self) -> Text:
        return "action_tipo_producto_seleccionado"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        producto = next(tracker.get_latest_entity_values("producto"), None)
        print(f"producto:{producto}")

        if "máquinas" in producto.lower() or "maquinas" in producto.lower():
            producto = "maquinas_de_ensayo"
        else:
            producto = "accesorios"

        with open("actions/productos.json", "r", encoding="utf-8") as json_object:
            data = json.load(json_object)
            maquinas_o_accesorios = data[producto].keys()

        if "maquinas_de_ensayo" in producto:
            text = (
                "Estas son las diferentes máquinas de ensayo que proporciona Servosis. ¿Sobre cuál desea más información?"
                + "\n Deslice hacia la derecha para ver las diferentes máquinas de ensayo."
            )

        else:
            text = (
                "Estos son los diferentes accesorios que proporciona Servosis. ¿Sobre cuál desea más información?"
                + "\n Deslice hacia la derecha para ver los diferentes accesorios."
            )

        data = []
        for key in maquinas_o_accesorios:
            # if "acondicionadores de señal" not in key.lower():
            data.append({"title": key, "payload": key})

        message = {"payload": "quickReplies", "data": data}

        dispatcher.utter_message(
            text=text,
            json_message=message,
        )

        return []


class ActionMostrarSubproductos(Action):
    def name(self) -> Text:
        return "action_mostrar_subproductos"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        maquinas_o_accesorios = next(tracker.get_latest_entity_values("producto"), None)

        if (
            "universales" in maquinas_o_accesorios
            or "tracción y compresión" in maquinas_o_accesorios
        ):
            maquinas_o_accesorios = "Máquinas universales tracción-compresión"

        if (
            "monoactuador" in maquinas_o_accesorios
            or "multiactuador" in maquinas_o_accesorios
        ):
            maquinas_o_accesorios = "Pórticos monoactuador y multiactuador"

        if (
            "dinámicas" in maquinas_o_accesorios
            or "dinamicas" in maquinas_o_accesorios
            or "fatiga" in maquinas_o_accesorios
        ):
            maquinas_o_accesorios = "Máquinas dinámicas y de fatiga"

        if "hormigones" in maquinas_o_accesorios or "rocas" in maquinas_o_accesorios:
            maquinas_o_accesorios = "Máquinas para compresión de hormigones y rocas"

        if "corte" in maquinas_o_accesorios or "recalcado" in maquinas_o_accesorios:
            maquinas_o_accesorios = "Máquina de corte y recalcado"

        if "metálicas" in maquinas_o_accesorios or "metalicas" in maquinas_o_accesorios:
            maquinas_o_accesorios = "Preparación de muestras metálicas para tracción"

        if any(keyword in maquinas_o_accesorios for keyword in ["celdas","celda","células","celulas"]):
            maquinas_o_accesorios = "Células de carga"

        print(f"producto:{maquinas_o_accesorios}")
        print(f"longitud:{len(maquinas_o_accesorios)}")

        with open("actions/productos.json", "r", encoding="utf-8") as json_object:
            data = json.load(json_object)
            if maquinas_o_accesorios in data["maquinas_de_ensayo"].keys():
                tipo_producto = "maquinas_de_ensayo"
                mas_informacion = "¿Sobre qué máquina le gustaría saber más?"
            else:
                tipo_producto = "accesorios"
                mas_informacion = "¿Sobre qué software le gustaría saber más?"

            subproductos = data[tipo_producto][maquinas_o_accesorios]
            print(f"Subproductos: {subproductos}")

        if len(subproductos) > 1:
            # Texto general que introduce los distintos productos
            dispatcher.utter_message(
                text=seleccionar_subproductos(maquinas_o_accesorios),
            )

            # Collapsible con los diferentes productos
            message = {"payload": "collapsible", "data": subproductos}

            dispatcher.utter_message(
                json_message=message,
            )

            # quickReplies para que el usuario seleccione el subproducto del que
            # desea saber más.

            # Guardamos los subproductos
            modelos = [
                {"title": modelo["title"], "payload": modelo["title"]}
                for modelo in subproductos
            ]

            message = {"payload": "quickReplies", "data": modelos}
            dispatcher.utter_message(
                text=mas_informacion,
                json_message=message,
            )
        else:
            # Mostramos la descripción del subproducto
            subproducto = subproductos[0]
            dispatcher.utter_message(text=subproducto["description"])

            # Compartimos el pdf, si lo tenemos, por si le interesa saber más
            with open(
                "actions/subproductos.json", "r", encoding="utf-8"
            ) as json_object:
                subproductos = json.load(json_object)
                if subproducto["title"] in subproductos.keys():
                    message = {
                        "payload": "pdf_attachment",
                        "title": subproductos[subproducto["title"]]["title"],
                        "url": subproductos[subproducto["title"]]["url"],
                    }
                    dispatcher.utter_message(
                        text="En este pdf podrá encontrar más información:",
                        json_message=message,
                    )
                else:
                    print(f"No hay pdf asociado al subproducto: {subproducto['title']}")

                # Explicación por si necesita más información.
                dispatcher.utter_message(template="utter_mas_informacion")

                # Ofrecer más ayuda
                dispatcher.utter_message(template="utter_ayuda")
        return []


class ActionCompartirPdfSubproducto(Action):
    def name(self) -> Text:
        return "action_compartir_pdf_subproducto"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        subproducto = next(tracker.get_latest_entity_values("producto"), None)
        print(f"Subproducto seleccionado: {subproducto}")

        with open("actions/subproductos.json", "r", encoding="utf-8") as json_object:
            subproductos = json.load(json_object)
            message = {
                "payload": "pdf_attachment",
                "title": subproductos[subproducto]["title"],
                "url": subproductos[subproducto]["url"],
            }

        # Compartir pdf
        dispatcher.utter_message(
            text="En este pdf podrá encontrar más información.",
            json_message=message,
        )

        # Ofrecerle más información a través de nuestros expertos
        dispatcher.utter_message(template="utter_mas_informacion")

        return []
