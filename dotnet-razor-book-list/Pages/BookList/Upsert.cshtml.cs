using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;

using dotnet_razor_book_list.Model;

namespace dotnet_razor_book_list.Pages.BookList
{
    public class UpsertModel : PageModel
    {
        private ApplicationDbContext _db;
        
        public UpsertModel(ApplicationDbContext db)
        {
            _db = db;
        }

        [BindProperty]
        public Book Book { get; set; }

        public async Task<IActionResult> OnGet(int? Id)
        {
            Book = new Book();
            if(Id == null) {
                // Create
                return Page();
            }

            // Update
            Book = await _db.Book.FirstOrDefaultAsync(u => u.Id == Id);
            if(Book == null){
                return NotFound();
            }

            return Page();
        }

        public async Task<IActionResult> OnPost()
        {
            if(ModelState.IsValid) {
                if(Book.Id == 0) {
                    _db.Book.Add(Book);
                } else {
                    _db.Book.Update(Book);
                }

                await _db.SaveChangesAsync();

                return RedirectToPage("Index");
            } else {
                return Page();
            }
        }
    }
}
