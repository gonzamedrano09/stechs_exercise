(function () {
    $(document).ready(function () {

        /* Variables */

        var buqueda = "";

        /* Eventos*/

        $("#btn-buscar").click(function () {
            // Guardo busqueda en variable global
            buqueda = $("#txt-nombre-fabricante").val().trim();

            // Consulto cable modems
            consultarCableModems();

        });

        $(document).on("click", ".btn-accion", function () {
            // Genero parámetros para petición
            let datos = {};
            datos.accion = "agregar_modelo_de_cable_modem_a_archivo_json"
            datos.mac_addr = $(this).attr("data");

            // Realizo petición a api
            $.ajax({
                type: "patch",
                contentType: "application/x-www-form-urlencoded; charset=UTF-8",
                url: "http://localhost:8000/api/cable_modems/",
                data: JSON.stringify(datos),

            // Respuesta exitosa
            }).done(function (data, status, xmlHttpRequest) {
                consultarCableModems();

            // Respuesta erronea
            }).fail(function (xmlHttpRequest, status, error) {
                mostrarMensajeError(xmlHttpRequest.responseText);
            });

        });

        /* Funciones */

        function consultarCableModems() {
            let datos = {};
            if (buqueda !== "") {
                datos.fabricante = buqueda;
            }

            // Realizo petición a api
            $.ajax({
                type: "get",
                contentType: "application/x-www-form-urlencoded; charset=UTF-8",
                url: "http://localhost:8000/api/cable_modems/",
                data: datos,

            // Respuesta exitosa
            }).done(function (data, status, xmlHttpRequest) {
                let modelos = data.datos;
                cargarTablaCableModems(modelos);

            // Respuesta erronea
            }).fail(function (xmlHttpRequest, status, error) {
                mostrarMensajeError(xmlHttpRequest.responseText);
            });
        }

        function cargarTablaCableModems(modelos) {
            $("#div-tabla").removeClass("hidden");
            $("#div-mensaje-error").addClass("hidden");

            let $tablaCableModems = $("#table-cable-modems");
            $tablaCableModems.find("tbody tr:not(.clone)").remove();

            for (let i=0; i<modelos.length; i++) {
                var modelo = modelos[i];

                var $tr = $tablaCableModems.find("tbody tr.clone").clone();
                $tr.removeClass("clone");
                $tr.removeClass("hidden");
                $tr.find(".td-vendor").text(modelo.vsi_vendor);
                $tr.find(".td-mac").text(modelo.modem_macadd);
                $tr.find(".td-ip").text(modelo.ipaddr);
                $tr.find(".td-modelo").text(modelo.vsi_model);
                $tr.find(".td-version").text(modelo.vsi_swver);
                $tr.find(".btn-accion").attr("data", modelo.modem_macadd);

                $tablaCableModems.find("tbody").append($tr);
            }
        }

        function mostrarMensajeError(mensajeError) {
            $("#div-tabla").addClass("hidden");
            $("#div-mensaje-error").removeClass("hidden");

            $("#mensaje-error").text(mensajeError);
        }

    });
})();