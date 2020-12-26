using Microsoft.AspNetCore.Http;
using System.Threading.Tasks;

namespace web
{
    public interface Irelatorio
    {
        Task imprimir(HttpContext context);
    }
}