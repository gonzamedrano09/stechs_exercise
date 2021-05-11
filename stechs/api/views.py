import json
from django.db.models import Q
from django.views import View
from django.http import HttpResponse
from stechs.api.models import DocsisUpdate
from stechs.api.exceptions import StechsApiError
from stechs.api.services.service_models_json import ServiceModelsJson


class CableModemView(View):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            # Obtengo y valido fabricante enviado por parámetro
            vendor = data.get("fabricante")
            if vendor is None:
                raise StechsApiError("Se necesita un fabricante")

            # Obtengo listado de modelos que coincidan con el fabricante en el archivo JSON a través del servicio
            service_models_json = ServiceModelsJson()
            models = service_models_json.get_models_for_vendor(vendor)

            # Verifico que se haya encontrado al menos un modelo
            if len(models) == 0:
                raise StechsApiError("El fabricante solicitado no se encuentra en el archivo models.json")

            # Consulto cable modems del mismo fabricante pero de distintos modelos a los obtenidos
            vendor = models[0].get("vendor")
            list_models = [model.get("name") for model in models]
            cable_modems = DocsisUpdate.objects.filter(Q(vsi_vendor__icontains=vendor) & ~Q(vsi_model__in=list_models))

            # Verifico que existan modelos de cable modems sin agregar al archivo JSON
            if len(cable_modems) == 0:
                raise StechsApiError("Todos los modelos del fabricante solicitado ya se encuentran en el archivo "
                                     "models.json")

            # Armo lista de diccionarios para respuesta
            cable_modems_list_dicts = []
            for cable_modem in cable_modems:
                cable_modems_list_dicts.append(cable_modem.get_dict())

            # Armo respuesta json
            response_json = {
                "mensaje": "Modelos obtenidos exitosamente",
                "datos": cable_modems_list_dicts
            }

            # Retorno respuesta en formato json
            return HttpResponse(json.dumps(response_json), content_type="application/json", status=200)

        except StechsApiError as ex:
            return HttpResponse(str(ex), status=500)

    def patch(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))

        try:
            # Obtengo acción
            action = data.get("accion")

            if action == "agregar_modelo_de_cable_modem_a_archivo_json":
                mac_addr = data.get("mac_addr")

                # Obtengo cable modem a partir de dirección MAC
                try:
                    cable_modem = DocsisUpdate.objects.get(modem_macaddr=mac_addr)
                except DocsisUpdate.DoesNotExist:
                    raise StechsApiError("No se encontró el cable modem")

                # Genero diccionario a partir de cable modem para agregarlo a archivo JSON
                model_dict = {
                    "vendor": cable_modem.vsi_vendor,
                    "name": cable_modem.vsi_model,
                    "version": cable_modem.vsi_swver
                }

                # Agrego modelo a archivo json
                service_models_json = ServiceModelsJson()
                try:
                    service_models_json.add_model(model_dict)
                except Exception:
                    raise StechsApiError("Ocurió un error al intentar agregar el modelo al archivo models.json")

                # Armo respuesta json
                response_json = {
                    "mensaje": "Modelo agregado exitosamente",
                }

                # Retorno respuesta en formato json
                return HttpResponse(json.dumps(response_json), content_type="application/json", status=200)

            else:
                raise StechsApiError("Acción inválida")

        except StechsApiError as ex:
            return HttpResponse(str(ex), status=500)
