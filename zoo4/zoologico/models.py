from django.db import models


class Zoologico(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del zoológico
    direccion = models.CharField(max_length=100)  # Dirección del zoológico
    horarioAtencion = models.CharField(max_length=100)  # Horario de atención del zoológico
    zona = models.ManyToManyField('Zona', related_name='zonas')  # Relación muchos a muchos con zonas
    empleado = models.ManyToManyField('Empleado', related_name='empleados', default=0)  # Relación muchos a muchos con empleados

    def __str__(self):
        return self.nombre + ' ' + self.direccion


class Persona(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la persona
    fechaNacimiento = models.DateField()  # Fecha de nacimiento
    cedula = models.CharField(max_length=10)  # Cédula de identidad
    numeroTelefono = models.CharField(max_length=10)  # Número de teléfono

    def __str__(self):
        return self.nombre + ' ' + self.cedula  # Representación en cadena de la persona


class Empleado(Persona):
    cargo = models.CharField(max_length=20)  # Cargo del empleado
    horario = models.CharField(max_length=20)  # Horario de trabajo
    sueldo = models.FloatField()  # Sueldo del empleado

    def __str__(self):
        return self.nombre + ' ' + self.cargo  # Representación en cadena del empleado


class Veterinario(Empleado):
    especialidad = models.CharField(max_length=50)  # Especialidad del veterinario
    animalCargo = models.CharField(max_length=50)  # Animal a cargo

    def __str__(self):
        return self.nombre + ' ' + self.especialidad  # Representación en cadena del veterinario


class Guia(Empleado):
    especialidad = models.CharField(max_length=50)  # Especialidad del guía
    idioma = models.CharField(max_length=50)  # Idioma que habla
    turno = models.CharField(max_length=50)  # Turno de trabajo
    boleto = models.ForeignKey('Boleto', on_delete=models.CASCADE, related_name='boletos_guia')  # Relación con Boleto

    def __str__(self):
        return self.nombre + ' ' + self.especialidad  # Representación en cadena del guía


class Cuidador(Empleado):
    areaResponsable = models.CharField(max_length=50)  # Área de responsabilidad


class Conserje(Empleado):
    areaLimpieza = models.CharField(max_length=50)  # Área de limpieza



class Taquillero(Empleado):
    boleto = models.ForeignKey('Boleto', on_delete=models.CASCADE, related_name='boletos_taquillero')  # Relación con Boleto



class Cliente(Persona):
    boleto = models.ForeignKey('Boleto', on_delete=models.CASCADE, related_name='clientes', default=0)  # Relación con Boleto

    def __str__(self):
        return self.nombre + ' ' + self.cedula  # Representación en cadena del cliente


class Animal(models.Model):
    # Opciones para el tipo de columna vertebral
    class TipoColumnaVertebral(models.TextChoices):
        VERTEBRADO = 'Vertebrado'
        INVERTEBRADO = 'Invertebrado'

    # Opciones para el tipo de alimentación
    class TipoAlimentacion(models.TextChoices):
        CARNIVORO = 'Carnivoro'
        HERBIVORO = 'Herbivoro'
        OMNIVORO = 'Omnivoro'

    nombre = models.CharField(max_length=50)  # Nombre del animal
    edad = models.CharField(max_length=50)  # Edad del animal
    peso = models.FloatField()  # Peso del animal
    especie = models.CharField(max_length=50)  # Especie del animal
    historialSalud = models.CharField(max_length=50)  # Historial de salud
    tipoColumnaVertebral = models.CharField(max_length=15, choices=TipoColumnaVertebral.choices)  # Tipo de columna vertebral
    tipoAlimentacion = models.CharField(max_length=15, choices=TipoAlimentacion.choices)  # Tipo de alimentación


class Alimentacion(models.Model):
    tipoAlimento = models.CharField(max_length=50)  # Tipo de alimento
    cantidad = models.CharField(max_length=50)  # Cantidad de alimento
    frecuencia = models.CharField(max_length=50)  # Frecuencia de alimentación
    horario = models.CharField(max_length=50)  # Horario de alimentación


class Jaula(models.Model):
    # Opciones para el estado de la jaula
    class Estado(models.TextChoices):
        OCUPADA = 'Ocupada'
        MANTENIMIENTO = 'Mantenimiento'
        DESOCUPADA = 'Desocupada'
        RESERVADA = 'Reservada'

    codigo = models.CharField(max_length=50)  # Código de la jaula
    estado = models.CharField(max_length=15, choices=Estado.choices)  # Estado actual de la jaula


class Exhibicion(models.Model):
    nombre = models.CharField(max_length=50)  # Nombre de la exhibición
    horario = models.CharField(max_length=50)  # Horario de la exhibición
    ubicacion = models.CharField(max_length=50)  # Ubicación de la exhibición
    tema = models.CharField(max_length=50)  # Tema de la exhibición

    def __str__(self):
        return self.nombre + ' ' + self.horario  # Representación en cadena de la exhibición


class PanelInformativo(models.Model):
    nombreCientifico = models.CharField(max_length=50)  # Nombre científico del animal
    nombreComun = models.CharField(max_length=50)  # Nombre común del animal
    familia = models.CharField(max_length=50)  # Familia del animal
    habitatNatural = models.CharField(max_length=50)  # Hábitat natural
    dieta = models.CharField(max_length=50)  # Dieta del animal
    estadoDeConservacion = models.CharField(max_length=50)  # Estado de conservación


class Boleto(models.Model):
    numero = models.CharField(max_length=100)  # Número del boleto
    fecha = models.DateField()  # Fecha de emisión
    hora = models.TimeField()  # Hora de emisión
    precio = models.FloatField()  # Precio del boleto


class Habitat(models.Model):
    tipoHabitat = models.CharField(max_length=100)  # Tipo de hábitat
    temperatura = models.FloatField()  # Temperatura del hábitat
    area = models.FloatField()  # Área del hábitat
    capacidad = models.CharField(max_length=100)  # Capacidad del hábitat


class Zona(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la zona
    tipoZona = models.CharField(max_length=100)  # Tipo de zona

    def __str__(self):
        return self.nombre + ' ' + self.tipoZona  # Representación en cadena de la zona


class Diagnostico(models.Model):
    sintoma = models.CharField(max_length=100)  # Síntoma diagnosticado
    fecha = models.DateField()  # Fecha del diagnóstico


class HistorialSalud(models.Model):
    fecha = models.DateField()  # Fecha del registro
    diagnostico = models.CharField(max_length=100)  # Diagnóstico realizado
    veterinario = models.CharField(max_length=100)  # Veterinario encargado
    tratamiento = models.CharField(max_length=100)  # Tratamiento aplicado
    anamnesis = models.CharField(max_length=100)  # Anamnesis del paciente
