from django.test import TestCase

from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.urls import reverse
from http import HTTPStatus

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
        tags = (
        ('<html', 1),
        ('<link', 5),
        ('<a', 174),
        ('<div', 22),
        ('href="', 179),
        ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
                
# class ListarHtmlTest(TestCase):
#     def setUp(self):
#         pessoa_cpf = '000.000.000-00' 
#         self.resp = self.client.get(reverse('excluir_pessoa', kwargs={'pessoa_cpf': pessoa_cpf}), follow=True)

#     def test_found_html(self):
#         tags = (
#         ('<html', 1),
#         ('<link', 5),
#         ('<a', 10),
#         ('<div', 22),
#         ('href="', 15),
#         ('</html>', 1),
#         )
#         for text, count in tags:
#             with self.subTest():
#                 self.assertContains(self.resp, text, count)                   

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
        self.resp = self.client.get(r('criar_plantas'), follow=True)
        
    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'criar.html')
    

# class EditarGet(TestCase):
#     def setUp(self):
#         self.resp = self.client.get(r('criar_plantas'), follow=True)
        
#     def test_status_code(self):
#         self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
#     def test_template_used(self):
#         self.assertTemplateUsed(self.resp, 'criar.html')     
        
# class PlantasFormTest(TestCase):
#     def test_fields_in_form(self):
#         form = PlantasForm()
#         expected = ['nome_cientifico','nome_popular','melhor_solo','clima','regiao','dificuldade_cultivar','ml_dia']
#         self.assertSequenceEqual(expected, list(form.fields))
    
#     def test_form_all_OK(self):
#         dados = dict(nome_cientifico='Rosa gallica', nome_popular='Rosa Vermelha', melhor_solo ='Solo Argiloso', clima='Temperado', regiao ='Europa', dificuldade_cultivar='Moderada', ml_dia =300)
#         form = PlantasForm(dados)
#         errors = form.errors
#         self.assertEqual({}, errors)
        
#     def test_form_without_data_1(self):
#         dados = dict(titulo='Contos do Machado de Assis')
#         form = PlantasForm(dados)
#         errors = form.errors
#         errors_list = errors['editora']
#         msg = 'Informe a editora do livro.'
#         self.assertEqual([msg], errors_list)

#     def test_form_without_data_2(self):
#         dados = dict(editora='Editora Brasil')
#         form = PlantasForm(dados)
#         errors = form.errors
#         errors_list = errors['titulo']
#         msg = 'Informe o título do livro.'
#         self.assertEqual([msg], errors_list)
    
#     def test_form_less_than_10_character_1(self):
#         dados = dict(titulo='123', editora='Editora Brasil')
#         form = PlantasForm(dados)
#         errors = form.errors
#         errors_list = errors['titulo']
#         msg = 'Deve ter pelo menos dez caracteres'
#         self.assertEqual([msg], errors_list)
    
#     def test_form_less_than_10_character_2(self):
#         dados = dict(titulo='Contos do Machado de Assis', editora='123')
#         form = PlantasForm(dados)
#         errors = form.errors
#         errors_list = errors['editora']
#         msg = 'Deve ter pelo menos dez caracteres'
#         self.assertEqual([msg], errors_list)