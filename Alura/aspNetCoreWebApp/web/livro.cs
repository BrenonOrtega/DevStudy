using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace web
{
    public class livro
    {
        public livro(string codigo, string nome, decimal preco)
        {
            this.codigo = codigo;
            this.nome = nome;
            this.preco = preco;
        }

        public string codigo { get; set; }
        public string nome { get; set; }
        public decimal preco { get; set; }
    }
}
