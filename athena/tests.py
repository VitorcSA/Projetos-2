from django.test import TestCase

from django.urls import reverse
# Importamos os modelos que queremos testar:
from .models import Noticia, Tag 

class TagViewTest(TestCase):
    
    
    def setUp(self):
        # Cria Tags de teste
        self.tag_politica = Tag.objects.create(nome='Política Local')
        self.tag_economia = Tag.objects.create(nome='Economia')
        
        # Cria Notícias de teste e as associa às Tags
        self.noticia_a = Noticia.objects.create(titulo='Título A', conteudo='Conteúdo A')
        self.noticia_b = Noticia.objects.create(titulo='Título B', conteudo='Conteúdo B')
        self.noticia_c = Noticia.objects.create(titulo='Título C', conteudo='Conteúdo C')
        
        # Associa Tags:
        self.noticia_a.tags.add(self.tag_politica) # Noticia A é Política
        self.noticia_b.tags.add(self.tag_politica, self.tag_economia) # Noticia B é Política E Economia
        self.noticia_c.tags.add(self.tag_economia) # Noticia C é só Economia

  
    def test_noticias_por_tag_filtra_corretamente(self):
        
        # a) Simula o acesso à URL da tag "Política Local" (o slug é gerado automaticamente)
        response_politica = self.client.get(
            reverse('noticias_por_tag', args=[self.tag_politica.slug])
        )
        
        # Verifica se o status HTTP é 200 (Sucesso na exibição da página)
        self.assertEqual(response_politica.status_code, 200)
        
        # Verifica se as notícias corretas estão na resposta (A e B devem ser encontradas)
        self.assertIn(self.noticia_a, response_politica.context['noticias'])
        self.assertIn(self.noticia_b, response_politica.context['noticias'])
        
        # Verifica se a notícia incorreta NÃO está na resposta (C não deve ser encontrada)
        self.assertNotIn(self.noticia_c, response_politica.context['noticias'])

        
   
    def test_noticias_por_tag_slug_invalido(self):
        
        # Simula o acesso a um slug que não existe no banco
        response = self.client.get(
            reverse('noticias_por_tag', args=['tag-que-nao-existe'])
        )
        
        # Espera um erro 404 (Not Found), que é o comportamento do get_object_or_404
        self.assertEqual(response.status_code, 404)
