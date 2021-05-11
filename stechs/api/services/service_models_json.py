import json
from stechs.settings import BASE_DIR


class ServiceModelsJson:

    url_json = BASE_DIR + "/models.json"

    def get_models_for_vendor(self, vendor):

        # Obtengo modelos de archivo JSON
        file = open(self.url_json, "r")
        file_json = json.load(file)
        file.close()

        # Creo lista de diccionarios del vendor pasado por parámetro
        models = []
        for model_json in file_json.get("models"):
            if vendor in model_json.get("vendor"):
                models.append(model_json)

        # Retorno listado de modelos
        return models

    def add_model(self, model_dict):

        # Obtengo modelos de archivo JSON
        file = open(self.url_json, "r")
        file_json = json.load(file)
        file.close()

        # Verifico que aún no exista el modelo del fabricante en el archivo JSON
        model_encontrado = False
        for model_json in file_json.get("models"):
            if model_json.get("vendor") in model_dict.get("vendor") and \
                    model_json.get("name") == model_dict.get("name"):
                model_encontrado = True
                break
        if model_encontrado:
            return

        # Agrego modelo a listado de modelos
        list_models = file_json.get("models")
        list_models.append(model_dict)
        file_json["models"] = list_models

        # Guardo en archivo JSON la nueva lista de modelos
        file = open(self.url_json, "w")
        json.dump(file_json, file, indent=2)
        file.close()
