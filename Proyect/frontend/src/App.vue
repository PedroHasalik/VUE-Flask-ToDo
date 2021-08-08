<template>
  <div id="app">
    <header class="header">
        <h1>TodoList</h1>
    </header>
   <AddTodo v-on:add-todo="addTodo"/>
   <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo" v-on:complete-todo="completeTodo" v-on:show-edit="displayEdit"/>
   <EditTodo v-if="on" v-bind:todoToEdit="todoToEdit" v-on:edit-todo="editTodo"/>
  </div>
</template>

<script>

import Todos from './components/Todos.vue'
import AddTodo from './components/AddTodo.vue'
import EditTodo from './components/EditTodo.vue'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    Todos,
    AddTodo,
    EditTodo,
  },
  data() {
    return{
      todos: [],
      on: false,
      todoToEdit: null
    }
  },
  methods: {
    deleteTodo(id){
      axios.delete('http://localhost:5000/delete/'+id)
      .then(this.todos = this.todos.filter(todo => todo.id !== id))
      .catch(err => console.log(err));
    },
    addTodo(newTodo){
      const {title,completed} = newTodo;
      axios.post('http://localhost:5000/add', {
        title,
        completed
      })
        .then (res => this.todos = [...this.todos, newTodo])
        .catch(err => console.log(err))
    },
    editTodo(todo){
      axios.put('http://localhost:5000/update/'+todo.id,{
              title:todo.title,
      })
      this.on = !this.on
    },
    completeTodo(todo){
      axios.put('http://localhost:5000/complete/'+todo.id,{
              completed:!todo.completed
      })
    },
    displayEdit(todo){
      this.on = !this.on
      this.todoToEdit = todo
    }
  },
  created() {
    axios.get('http://localhost:5000/get')
      .then(res => this.todos = res.data)
      .catch(err => console.log(err));
  }
}
</script>

<style>
 *{
   box-sizing: border-box;
   margin: 0;
   padding: 0;
 }
 body{
   font-family: Arial, Helvetica, sans-serif;
   line-height: 1.4;
 }
 .btn {
    display: inline-block;
    border: none;
    background: #555;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
  }
 .btn:hover {
    background: #666;
  }
  .header {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
  }
  .header a {
    color: #fff;
    padding-right: 5px;
    text-decoration: none;
  }
</style>
