<template>
  <div id="app">
    <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo" />
    <AddTodo v-on:add-todo="addTodo"/>
  </div>
</template>

<script>
import Todos from '../components/Todos';
import AddTodo from '../components/AddTodo';

export default {
  name: 'Home',
  components: {
    Todos,
    AddTodo    
  },
  data() {
    return {
      todos: [

      ]
    }
  },
  methods: {
    deleteTodo(id) {
      fetch(`https://jsonplaceholder.typicode.com/todos/${id}`, {method:'DELETE'})
        .then(response => {
          if(response.status === 200){
            this.todos = this.todos.filter(todo => todo.id !== id);
          }
        })
        .catch(err => {
          console.log('Delete Request failed: ', err);
        });
    },
    addTodo(newTodo) {
      const { title, completed } = newTodo;
      fetch('https://jsonplaceholder.typicode.com/todos', {
        title,
        completed
      })
        .then(response => {
          if(response.status === 200){
            response.json().then(data => {
              console.log(data);
              this.todos = [...this.todos, data];
            })
          }
        })
        .catch(err => {
          console.log('Post Request failed: ', err);
        });
    }
  },
  created() {
    fetch('https://jsonplaceholder.typicode.com/todos?_limit=5')
      .then(response => {
        if(response.status === 200){
          response.json().then(data => {
            this.todos = data;
          });
        }
      })
      .catch(err => {
        console.log('Fetch Error: ', err);
      });
  }
}
</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    line-height: 1.4;
  }
  .btn {
    display: inline-block;
    border: none;
    background: #555;
    color:#fff;
    padding:7px 20px;
    cursor:pointer;
  }
  .btn:hover {
    background: #000;
  }
</style>