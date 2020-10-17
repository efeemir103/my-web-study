using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;

namespace dotnet_mvc_book_list.Models
{
    public class Book
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public int Name { get; set; }
        public int Author { get; set; }
        public int ISBN { get; set; }

    }
}