using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace web
{
    public class catalogo : Icatalogo
    {
        public List<livro> getLivros()
        {
            var livros = new List<livro>();
            livros.Add(new livro("001", "Sherlock Holmes e o Enigma do Principe", 19.99m));
            livros.Add(new livro("002", "Fique rico com C#", 40.00m));
            livros.Add(new livro("002", "Javascript só para baixinhos", 25.90m));

            return livros;
        }
    }
}
