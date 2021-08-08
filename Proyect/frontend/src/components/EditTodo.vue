<template>
    <div>
        <form @submit="editTodo">
            <input type="text" v-model="title" name="title" placeholder="Edit ToDo...">
            <input type="submit" value="Edit" class="btn">
        </form>
    </div>
</template>

<script>
export default {
    name: "EditTodo",
    data() {
      return {
        title: ''
      }
    },
    props :['todoToEdit'],
    methods: {
        editTodo(e) {
            e.preventDefault();
            this.todoToEdit.title = this.title;
            this.$emit('edit-todo', this.todoToEdit);
            this.title = '';
        }
    }

}
</script>

<style scoped>
  form {
    display: flex;
  }
  input[type="text"] {
    flex: 10;
    padding: 5px;
  }
  input[type="submit"] {
    flex: 2;
  }
</style>