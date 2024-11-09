def seleccionar_subproductos(producto):
    if "Máquinas universales tracción-compresión" in producto:
        text = (
            "A continuación le ofrecemos un listado con las diferentes máquinas "
            "de tracción-compresión que ofrece Servosis:"
        )
    elif "Máquinas dinámicas y de fatiga" in producto:
        text = (
            "A continuación le ofrecemos un listado con las diferentes máquinas "
            "dinámicas y de fatiga que ofrece Servosis:"
        )
    elif "Máquinas para compresión de hormigones y rocas" in producto:
        text = (
            "A continuación le ofrecemos un listado con las diferentes máquinas "
            "para compresión de hormigones y rocas que ofrece Servosis:"
        )
    elif "Máquinas de Torsión" in producto:
        text = (
            "A continuación le ofrecemos un listado con las diferentes máquinas "
            "de torsión que ofrece Servosis:"
        )
    elif "Pórticos monoactuador y multiactuador" in producto:
        text = (
            "A continuación le ofrecemos un listado con los diferentes pórticos "
            "monoactuador y multiactuador que ofrece Servosis:"
        )
    elif "Actuadores Hidráulicos" in producto:
        text = (
            "A continuación le ofrecemos un listado con los diferentes actuadores "
            "hidráulicos que ofrece Servosis:"
        )
    elif "Máquinas para ensayo de apoyos elastoméricos" in producto:
        text = (
            "A continuación le ofrecemos un listado con las diferentes máquinas "
            "para ensayo de apoyos elastoméricos que ofrece Servosis:"
        )

    elif "Preparación de muestras metálicas para tracción" in producto:
        text = (
            "A continuación le ofrecemos un listado con las diferentes máquinas "
            "para la preparación de muestras metálicas para tracción que ofrece Servosis:"
        )

    elif "Máquina de corte y recalcado" in producto:
        text = (
            "A continuación le ofrecemos una breve descripción de la máquina de "
            "corte y recalcado que ofrece Servosis:"
        )
    # Accesorios
    elif "Software de control" in producto:
        text = (
            "A continuación le ofrecemos un listado con los diferentes softwares de control "
            "que ofrece Servosis:"
        )
    elif "Células de carga" in producto:
        text = (
            "A continuación le ofrecemos información sobre las células de carga "
            "que ofrece Servosis:"
        )
    elif "Mordazas para tracción" in producto:
        text = (
            "A continuación le ofrecemos información sobre las mordazas de tracción "
            "que ofrece Servosis:"
        )
    elif "Platos de compresión" in producto:
        text = (
            "A continuación le ofrecemos información sobre los platos de compresión "
            "que ofrece Servosis:"
        )
    elif "Dispositivos de flexión" in producto:
        text = (
            "A continuación le ofrecemos información sobre los dispositivos de flexión "
            "que ofrece Servosis:"
        )
    elif "Mezclas bituminosas" in producto:
        text = (
            "A continuación le ofrecemos información sobre las soluciones en mezclas bituminosas "
            "que ofrece Servosis:"
        )
    elif "Extensómetros y videoextensómetros" in producto:
        text = (
            "A continuación le ofrecemos información sobre los extensómetros "
            "que ofrece Servosis:"
        )
    elif "Cámaras climáticas y hornos" in producto:
        text = (
            "A continuación le ofrecemos un listado con los equipos de control climático y térmico "
            "que ofrece Servosis:"
        )
    elif "Acondicionadores de señal" in producto:
        text = (
            "A continuación le ofrecemos un listado con los acondicionadores de señal "
            "y tarjetas de medición que ofrece Servosis:"
        )
    else:
        text = "No se ha encontrado información sobre el producto especificado."

    return text
