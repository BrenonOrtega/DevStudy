using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace web
{
    public class relatorio : Irelatorio
    {
        private readonly Icatalogo Catalogo;

        public relatorio(Icatalogo Catalogo)
        {
            this.Catalogo = Catalogo;
           
        }

        public async Task imprimir(HttpContext context)
        {
            foreach (var livro in Catalogo.getLivros())
            {
                await context.Response.WriteAsync($"{livro.codigo,-10}  {livro.nome,-40}  {livro.preco,10} \r\n");
            }
        }

    }
}
