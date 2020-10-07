import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './components/layout/Header'
import TodoList from './components/TodoList';
import AddTodo from './components/AddTodo';
import About from './components/pages/About'

import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';

import './App.css';

class App extends Component {
  state = {
    todos: [
      {id: uuidv4(), title: 'Take out the trash', completed: false},
        {id: uuidv4(), title: 'Dinner with wife', completed: true},
        {id: uuidv4(), title: 'Meeting with boss', completed: false}
    ]
  }

  componentDidMount() {
    axios.get('https://jsonplaceholder.typicode.com/todos?_limit=10')
      .then(res => this.setState({todos: res.data}))
  }

  onItemRemove = (id) => {
    axios.delete(`https://jsonplaceholder.typicode.com/todos/${id}`)
      .then(res => this.setState({
        todos: this.state.todos.filter(todo => todo.id !== id)
      }));
  }

  onItemUpdate = (item) => {
    axios.put(`https://jsonplaceholder.typicode.com/todos/${item.id}`)
      .then(res => this.setState({todos: this.state.todos.map(todo => {
        if(todo.id === item.id) {
            return item;
        } else {
            return todo;
        }
      })
    }));
  }

  onAdd = (title) => {
    if(!title) {
      return;
    }
    axios.post('https://jsonplaceholder.typicode.com/todos', {
      title,
      completed: false
    })
      .then(res => this.setState({
        todos: [
          ...this.state.todos,
          res.data
        ]
      }));
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Header>TodoList</Header>
          <Route exact path="/" render={props => (
            <React.Fragment>
              <AddTodo onComplete={this.onAdd}/>
              <TodoList data={this.state.todos} onItemUpdate={this.onItemUpdate} onItemRemove={this.onItemRemove}/>
            </React.Fragment>
          )}/>
          <Route path="/about" component={About} />
        </div>
      </Router>
    );
  }
}

export default App;
