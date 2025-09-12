frases_p_statements_ordenadas = [
    # NIVEL 1: RESPUESTA DE EMERGENCIA INMEDIATA
    ("P301+P310", "EN CASO DE INGESTIÓN: Llamar inmediatamente a un CENTRO DE TOXICOLOGÍA o a un médico",1),
    ("P302+P352", "EN CASO DE CONTACTO CON LA PIEL: Lavar con abundante agua",2),
    ("P303+P361+P353", "EN CASO DE CONTACTO CON LA PIEL (o el cabello): Quitar inmediatamente la ropa contaminada. Aclarar la piel con agua o ducharse",3),
    ("P304+P340", "EN CASO DE INHALACIÓN: Transportar a la persona al aire libre y mantenerla en reposo en una posición confortable para respirar",4),
    ("P305+P351+P338", "EN CASO DE CONTACTO CON LOS OJOS: Aclarar cuidadosamente con agua durante varios minutos. Quitar lentes de contacto si lleva y resulta fácil. Seguir aclarando",5),
    ("P308+P313", "EN CASO de exposición manifiesta o presunta: consultar a un médico",6),
    ("P310", "Llamar inmediatamente a un CENTRO DE TOXICOLOGÍA o a un médico",7),
    ("P311", "Llamar a un CENTRO DE TOXICOLOGÍA o a un médico",8),
    ("P312", "Llamar a un CENTRO DE TOXICOLOGÍA o a un médico si la persona se siente mal",9),

    # NIVEL 2: MEDIDAS PREVENTIVAS CRÍTICAS
    ("P210", "Mantener alejado del calor, superficies calientes, chispas, llamas abiertas y otras fuentes de ignición. No fumar",10),
    ("P220", "Mantener/Almacenar alejado de ropa y otros materiales combustibles",11),
    ("P260", "No respirar el polvo/el humo/el gas/la niebla/los vapores/el aerosol",12),
    ("P261", "Evitar respirar el polvo/el humo/el gas/la niebla/los vapores/el aerosol",13),
    ("P280", "Llevar guantes/prendas/gafas/máscara de protección",14),
    ("P281", "Utilizar el equipo de protección individual obligatorio",15),
    ("P284", "Llevar equipo de protección respiratoria",16),
    ("P270", "No comer, beber ni fumar durante su utilización",17),
    ("P264", "Lavarse bien las manos tras la manipulación",18),
    ("P273", "Evitar su liberación al medio ambiente",19),

    # NIVEL 3: ALMACENAMIENTO SEGURO
    ("P405", "Guardar bajo llave",20),
    ("P403+P233", "Almacenar en un lugar bien ventilado. Mantener el recipiente herméticamente cerrado",21),
    ("P403+P235", "Almacenar en un lugar bien ventilado. Mantener en lugar fresco",22),
    ("P410+P403", "Proteger de la luz solar. Almacenar en un lugar bien ventilado",23),
    ("P411+P235", "Almacenar a temperaturas no superiores a X°C. Mantener en lugar fresco",24),

    # NIVEL 4: DISPOSICIÓN Y MANIPULACIÓN SEGURA
    ("P501", "Eliminar el contenido/el recipiente conforme a la normativa local/regional/nacional/internacional",25),
    ("P391", "Recoger el vertido",26),
    ("P321", "Tratamiento específico (ver instrucciones suplementarias en la etiqueta)",27),
    ("P330", "Enjuagar la boca",28),
    ("P362+P364", "Quitar la ropa contaminada y lavarla antes de volverla a usar",29),

    # NIVEL 5: CONSEJOS GENERALES
    ("P101", "Si se necesita consejo médico, tener a mano el envase o la etiqueta",30),
    ("P102", "Mantener fuera del alcance de los niños",31),
    ("P103", "Leer la etiqueta antes del uso",32),
    ("P201", "Solicitar instrucciones especiales antes del uso",33),
    ("P202", "No manipular la sustancia antes de haber leído y comprendido todas las precauciones de seguridad",34),
    ("P235", "Mantener en lugar fresco",35),
    ("P410", "Proteger de la luz solar",36),
    ("P234", "Conservar únicamente en el envase original",37),

    # NIVEL 6: MEDIDAS ADICIONALES/SECUNDARIAS
    ("P240", "Conectar a tierra/enlazar el recipiente y el equipo receptor",38),
    ("P241", "Utilizar material eléctrico/de ventilación/iluminación/.../antideflagrante",39),
    ("P242", "Utilizar solo herramientas que no produzcan chispas",40),
    ("P243", "Tomar medidas de precaución contra descargas electrostáticas",41),
    ("P272", "La ropa de trabajo contaminada no debe salir del lugar de trabajo",42),
    ("P391", "Recoger el vertido",43),
    ("P332+P313", "En caso de irritación cutánea: consultar a un médico",44),
    ("P337+P313", "Si persiste la irritación ocular: consultar a un médico",45),
    ("P370+P378", "En caso de incendio: utilizar el agente de extinción apropiado",46),
    ("P377", "Incendio provocado por fuga de gas: No extinguir si no es seguro",47),
    ("P381", "Eliminar todas las fuentes de ignición si se puede hacer sin peligro",48),
    ("P301+P330+P331", "EN CASO DE INGESTIÓN: Enjuagar la boca. NO provocar el vómito",49),

    # SITUACIONES ESPECIALES Y CONTINGENCIA
    ("P391", "Recoger el vertido",50),
    ("P402+P404", "Almacenar en un lugar seco. Guardar en recipiente cerrado",51),
    ("P420", "Almacenar separado de otros productos químicos",52),
    ("P422", "Almacenar el contenido en un recipiente resistente a la corrosión",53),
    ("P410+P412", "Proteger de la luz solar. No exponer a temperaturas superiores a 50°C/122°F",54),
    ("P501", "Eliminar el contenido y/o su recipiente de conformidad con la normativa local/regional/nacional/internacional",55),

    # Frases combinadas
    ("P303+P361+P353", "EN CASO DE CONTACTO CON LA PIEL (o el cabello): quitar inmediatamente toda la ropa contaminada. Enjuagar la piel con agua o ducharse",56),
    ("P304+P340+P310", "EN CASO DE INHALACIÓN: transportar a la persona al aire libre y mantenerla en reposo en una posición cómoda para respirar. Llamar inmediatamente a un centro de toxicología o a un médico",57)
]
