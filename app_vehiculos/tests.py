from django.test import TestCase
from app_vehiculos.models import Camioneta, Automovil, Motocicleta

class CamionetaTests(TestCase):

    def test_creacion_camioneta(self):
        camioneta = Camioneta(marca="Volkswagen", modelo="Amarok", fabricacion=2019, cv=258, peso=2820)
        camioneta.save()

        self.assertEqual(Camioneta.objects.count(), 1)
        self.assertEqual(camioneta.marca, "Volkswagen")
        self.assertEqual(camioneta.modelo, "Amarok")
        self.assertEqual(camioneta.fabricacion, 2019)
        self.assertEqual(camioneta.cv, 258)
        self.assertEqual(camioneta.peso, 2820)

    def test_camioneta_str(self):
        camioneta = Camioneta(marca="Volkswagen", modelo="Amarok", fabricacion=2019, cv=258, peso=2820)
        camioneta.save()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.fabricacion})({self.cv})({self.peso})"
    

class AutomovilTests(TestCase):

    def test_creacion_automovil(self):
        automovil = Automovil(marca="Fiat", modelo="uno", fabricacion=2000, cv=150, peso=800)
        automovil.save()

        self.assertEqual(Automovil.objects.count(), 1)
        self.assertEqual(automovil.marca, "Fiat")
        self.assertEqual(automovil.modelo, "uno")
        self.assertEqual(automovil.fabricacion, 2000)
        self.assertEqual(automovil.cv, 150)
        self.assertEqual(automovil.peso, 800)

    def test_automovil_str(self):
        automovil = Automovil(marca="Fiat", modelo="uno", fabricacion=2000, cv=150, peso=800)
        automovil.save()

        self.assertEqual(automovil.__str__(), "Fiat uno (2000)(150)(800)")





