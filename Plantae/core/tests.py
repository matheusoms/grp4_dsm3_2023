from django.test import TestCase
from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.urls import reverse
from http import HTTPStatus
from .services import obter_planta
from .forms import PlantasForm


class IndexHtmlTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'), follow=True)

    def test_found_html(self):
        tags = (
        ('<html', 1),
        ('<body>', 1),
        ('<link', 5),
        ('<li',14),
        ('<span', 12),
        ('<a', 15),
        ('<div', 71),
        ('href="', 20),
        ('<br>', 7),
        ('</body>', 1),
        ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
                
class SobreHtmlTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sobre'), follow=True)
        
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<link', 5),
            ('<li',12),
            ('<button', 2),
            ('<div', 28),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
                
class CriarHtmlTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('criar_plantas'), follow=True)
        
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<link', 5),
            ('<li',12),
            ('<a',9),
            ('<button', 3),
            ('<div', 22),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
                
class ListarHtmlTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('consultar'), follow=True)

    def test_found_html(self):
        a_numero = 2 * len(obter_planta())
        href_numero = 2 * len(obter_planta())
        tags = [
            ('<html', 1),
            ('<link', 5),
            ('<a', a_numero + 10),
            ('<div', 22),
            ('href="', href_numero + 15),
            ('</html>', 1),
        ]
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
                
class EditarHtmlTest(TestCase):
    def setUp(self):
        teste = 'Achillea millefolium' 
        self.resp = self.client.get(reverse('editar_planta', kwargs={'nome_planta': teste}), follow=True)

    def test_found_html(self):
        tags = (
        ('<html', 1),
        ('<link', 5),
        ('<div', 7),
        ('href="', 5),
        ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)                   

class IndexGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'), follow=True)
        
    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')
        

class IndexPost(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('home'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp , 'index.html')
        
class SobreGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sobre'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'about.html')

class SobrePost(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('sobre'),follow=True)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'about.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
        
class CriarGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('criar_plantas'), follow=True)
        
    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'criar.html')

class ConsultarGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sobre'), follow=True)
        
    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'about.html')
      
class PlantasFormTest(TestCase):
    def test_fields_in_form(self):
        form = PlantasForm()
        expected = ['nome_cientifico','nome_popular','melhor_solo','clima','regiao','dificuldade_cultivar','ml_dia']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_form_all_OK(self):
        dados = dict(nome_cientifico='Dianthus caryophyllus', nome_popular='Cravo', melhor_solo ='Solo Bem Drenado', clima='Temperado', regiao ='Europa', dificuldade_cultivar='Fácil', ml_dia =200)
        form = PlantasForm(dados)
        errors = form.errors
        self.assertEqual({}, errors)