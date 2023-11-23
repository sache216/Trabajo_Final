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
        
        
        self.assertEqual(camioneta.__str__(), "Volkswagen Amarok (2019)(258)(2820)")
    

class AutomovilTests(TestCase):

    def test_creacion_automovil(self):
        automovil = Automovil(marca="Fiat", modelo="uno", fabricacion=2000, cv=150, peso=1000)
        automovil.save()

        self.assertEqual(Automovil.objects.count(), 1)
        self.assertEqual(automovil.marca, "Fiat")
        self.assertEqual(automovil.modelo, "uno")
        self.assertEqual(automovil.fabricacion, 2000)
        self.assertEqual(automovil.cv, 150)
        self.assertEqual(automovil.peso, 1000)

    def test_automovil_str(self):
        automovil = Automovil(marca="Fiat", modelo="uno", fabricacion=2000, cv=150, peso=1000)
        automovil.save()

        self.assertEqual(automovil.__str__(), "Fiat uno (2000)(150)(1000)")


class MotocicletaTests(TestCase):

    def test_creacion_motocicleta(self):
        motocicleta = Motocicleta(marca="Honda", modelo="Tornado", fabricacion=2018, cv=94, peso=800)
        motocicleta.save()

        self.assertEqual(Motocicleta.objects.count(), 1)
        self.assertEqual(motocicleta.marca, "Honda")
        self.assertEqual(motocicleta.modelo, "Tornado")
        self.assertEqual(motocicleta.fabricacion, 2018)
        self.assertEqual(motocicleta.cv, 94)
        self.assertEqual(motocicleta.peso, 800)

    def test_motocicleta_str(self):
        motocicleta = Motocicleta(marca="Honda", modelo="tornado", fabricacion=2018, cv=94, peso=800)
        motocicleta.save()
        
        self.assertEqual(motocicleta.__str__(), "Honda tornado (2018)(94)(800)")


