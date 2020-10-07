import { compileComponentFromMetadata } from '@angular/compiler';
import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { title } from 'process';
import { Todo } from 'src/app/models/Todo';

@Component({
  selector: 'app-add-todo',
  templateUrl: './add-todo.component.html',
  styleUrls: ['./add-todo.component.css']
})
export class AddTodoComponent implements OnInit {
  @Output() addTodo: EventEmitter<any> = new EventEmitter();
  
  title:string;

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit() {
    this.addTodo.emit({
      title: this.title,
      completed: false
    });
  }

}
