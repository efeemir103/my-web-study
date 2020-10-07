import { Component, OnInit } from '@angular/core';
import { TodoService } from '../../services/todo.service';
import { Todo } from '../../models/Todo'

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {
  data:Todo[];

  constructor(private todoService:TodoService) { }

  ngOnInit(): void {
    this.todoService.getTodos().subscribe(todos => {
      this.data = todos;
    });
  }

  deleteTodo(todo:Todo){
    this.todoService.deleteTodo(todo).subscribe(res => {
      this.data = this.data.filter(t => t.id !== todo.id);
    });
  }

  addTodo(todo:Todo) {
    this.todoService.addTodo(todo).subscribe(res => {
      this.data.push(res);
    });
  }

}
