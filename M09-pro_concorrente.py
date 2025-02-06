#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import asyncio
from asyncio import get_event_loop
from requests import get
import nest_asyncio
from time import time

nest_asyncio.apply()

inicio = time()


url_list = [
    "https://www.petsloja.com.br/cachorro",
    "https://www.petsloja.com.br/brinquedo-cachorro-pelucia-macaco-com-apito-savana-pet/p",
    "https://www.petsloja.com.br/gato",
    "https://www.petsloja.com.br/guia-de-passeio-com-mola-amortecedor-resistente-cachorro-grande-medio-porte-lr-0137/p",
    "https://www.petsloja.com.br/coleira-para-caes-pequenos-modelo-peitoral-stillinho-guia-amortecedor-pet/p",
    "https://www.petsloja.com.br/racoes",
    "https://www.petsloja.com.br/coleiras",
    "https://www.petsloja.com.br/higiene-e-beleza",
    "https://www.petsloja.com.br/kit-shampoo-5-em-1-perfume-para-caes-pet-clean/p",
    "https://www.petsloja.com.br/racao-quatree-life-filhote-raca-pequena-10-kg/p"
]

def web_scrape():
        loop = get_event_loop()
        scrape_list = [loop.run_in_executor(None, get, url) for url in url_list]
        for scrape in scrape_list:
            resp = yield from scrape
            tags = BeautifulSoup(resp.text, "html5lib")
            title = tags.find("title")
            print(title.text)

async def main():
    loop = get_event_loop()
    loop.run_until_complete(web_scrape())

asyncio.run(main())

print(f"Total: {time() - inicio}")


# In[ ]:




