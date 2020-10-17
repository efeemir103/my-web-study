using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

using dotnet_razor_book_list.Model;


namespace dotnet_razor_book_list.Controllers
{
    [Route("api/Book")]
    [ApiController]
    public class BookController : Controller
    {
        private readonly ApplicationDbContext _db;

        public BookController(ApplicationDbContext db)
        {
            _db = db;
        }

        [HttpGet]
        public async Task<IActionResult> GetAll()
        {
            return Json(new { data = await _db.Books.ToListAsync() });
        }

        [HttpDelete]
        public async Task<IActionResult> Delete(int id)
        {
            var BookFromDb = await _db.Books.FirstOrDefaultAsync(u => u.Id == id);
            if(BookFromDb == null) {
                return Json(new { success = false, message = "Error while deleting" });
            }
            
            _db.Books.Remove(BookFromDb);
            await _db.SaveChangesAsync();
            return Json(new { success = true, message = "Delete was successful" });
        }
    }
}