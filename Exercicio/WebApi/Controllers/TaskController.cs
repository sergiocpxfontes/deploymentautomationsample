using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TaskController : ControllerBase
    {
        [HttpGet]
        public IEnumerable<Lib.Task> Get()
        {
            List<Lib.Task> lst = new List<Lib.Task>();

            Lib.Task t = new Lib.Task();
            t.Id = 1;
            t.Nome = "Enviar email";
            t.Data = new DateTime(2021, 11, 25);
            t.Utilizador = "Sergio";
            lst.Add(t);

            Lib.Task t1 = new Lib.Task();
            t1.Id = 2;
            t1.Nome = "Enviar carta";
            t1.Data = new DateTime(2021, 11, 25);
            t1.Utilizador = "Antonio";
            lst.Add(t1);

            return lst;
        }


    }
}
