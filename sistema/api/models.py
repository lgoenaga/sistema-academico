from django.db import models

# Create your models here.
class Submodulos(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Sub Modulo: {self.nombre} - Ultima actualizacion: {self.fecha_actualizacion}"


class Estudiantes(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexos = (
        ("F", "Femenino"),
        ("M", "Masculino"),
    )
    sexo = models.CharField(max_length=1, choices=sexos, default="M")
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    submodulo = models.ForeignKey(
        Submodulos, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} {self.apellido} - {estado} - Ultima actualizacion: {self.fecha_actualizacion}"


class Profesores(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexos = (
        ("F", "Femenino"),
        ("M", "Masculino"),
    )
    sexo = models.CharField(max_length=1, choices=sexos, default="M")
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} {self.apellido} - {estado} - Ultima actualizacion: {self.fecha_actualizacion}"


class Cursos(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    submodulo = models.ForeignKey(
        Submodulos, on_delete=models.CASCADE, null=False, blank=False
    )
    profesor = models.ForeignKey(
        Profesores, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return f"Curso: {self.nombre} - Sub Modulo: {self.submodulo.nombre} - Profesor: {self.profesor.nombre} {self.profesor.apellido} - Ultima actualizacion: {self.fecha_actualizacion}"


class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiantes, on_delete=models.CASCADE, null=False, blank=False
    )
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=False, blank=False)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"Estudiante: {self.estudiante.nombre} {self.estudiante.apellido} - {estado} - Curso: {self.curso.nombre} - Ultima actualizacion: {self.fecha_actualizacion}"
