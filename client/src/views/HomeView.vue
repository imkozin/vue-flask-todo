<script setup>
import { ref, watch, computed, onMounted } from 'vue'
import { Icon } from '@iconify/vue'
import axios from 'axios'
import TodoCreator from '@/components/TodoCreator.vue'
import TodoItem from './TodoItem.vue'
import { Vue3Snackbar } from "vue3-snackbar";
import { useSnackbar } from 'vue3-snackbar'
const snackbar = useSnackbar()

const todoList = ref([])
const showModal = ref(false)
const taskToDelete = ref(null)

watch(
  todoList,
  (newVal, oldVal) => {
    setTodoListToLocalStorage()
  },
  { deep: true }
)

onMounted(() => {
  getAllTodos()
})

const todosCompleted = computed(() => {
  return todoList.value.every((item) => item.isCompleted)
})

const getAllTodos = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/tasks')
    const data = response.data
    todoList.value = data
    const savedTodos = JSON.parse(localStorage.getItem('todos')) || []
    todoList.value.forEach(todo => {
      const savedTodo = savedTodos.find(savedTodo => savedTodo.task_id === todo.task_id)
      if (savedTodo) {
        todo.isCompleted = savedTodo.isCompleted
      }
    })
  } catch (error) {
    console.error('Error fetching tasks:', error)
    snackbar.add({
      type: 'error',
      text: error.response.data.error,
    })
  }
}

const createTodo = (todo) => {
  todo.isCompleted = false

  todoList.value.pop(todo)
  getAllTodos()
}

const setTodoListToLocalStorage = () => {
  localStorage.setItem('todos', JSON.stringify(todoList.value))
}

const toggleTodoComplete = (id) => {
  const todo = todoList.value.find((item) => item.task_id === id)
  let savedTodoList = JSON.parse(localStorage.getItem('todos'))
  if (todo) {
    todo.isCompleted = !todo.isCompleted
    setTodoListToLocalStorage()
    savedTodoList = todoList.value
  } else {
    console.error(`Todo with id ${id} not found.`)
  }
}

const toggleEditTodo = (id) => {
  const todo = todoList.value.find((item) => item.task_id === id)
  if (todo) {
    todo.isEditing = !todo.isEditing
  } else {
    console.error(`Todo with id ${id} not found.`)
  }
}

const deleteTodo = async (id) => {
  try {
    showModal.value = true
    const todo = todoList.value.find((item) => item.task_id === id)
    taskToDelete.value = todo
  } catch (error) {
    console.error('Error deleting task:', error)
  }
}

const confirmDelete = async () => {
  try {
    const id = taskToDelete.value.task_id
    const response = await axios.delete(
      `http://localhost:8000/api/delete-task/${id}`
    )
    snackbar.add({
      type: 'success',
      text: response.data.message,
    })
    getAllTodos()
  } catch (error) {
    console.error('Error deleting task:', error.message)
  } finally {
    showModal.value = false
    taskToDelete.value = null
  }
}

const cancelDelete = () => {
  showModal.value = false
  taskToDelete.value = null
}

const updateTodo = async (id, title, text) => {
  try {
    const response = await axios.put(
      `http://localhost:8000/api/edit-task/${id}`,
      { title, text }
    )
    getAllTodos()
    // setTodoListToLocalStorage()
    snackbar.add({
      type: 'success',
      text: response.data.message,
    })
  } catch (error) {
    snackbar.add({
      type: 'error',
      text: error.response.data.error,
    })
    console.error('Error updating task:', error)
  }
}
</script>

<template>
  <main>
    <div v-if="showModal" class="overlay">
      <div class="modal">
        <Icon icon="ph:x-bold" class="close" @click="showModal = false" />
        <p>Are you sure you want to delete this task?</p>
        <div class="btn-container">
          <button class="btn" @click="confirmDelete">Yes</button>
          <button class="btn" @click="cancelDelete">No</button>
        </div>
      </div>
    </div>

    <h1>Create Todo</h1>
    <TodoCreator @create-todo="createTodo" />
    <ul class="todo-list" v-if="todoList.length > 0">
      <TodoItem
        v-for="todo in todoList"
        :key="todo.task_id"
        :todo="todo"
        @toggle-complete="toggleTodoComplete"
        @edit-todo="toggleEditTodo"
        @update-todo="updateTodo"
        @delete-todo="deleteTodo"
      />
    </ul>
    <p class="todos-msg" v-else>
      <Icon icon="noto:sad-but-relieved-face" />
      <span>You have no todo's to complete! Add one!</span>
    </p>
    <p v-if="todosCompleted && todoList.length > 0" class="todos-msg">
      <Icon icon="noto-v1:party-popper" />
      <span>You have completed all your todos!</span>
    </p>
    <vue3-snackbar top right :duration="4000"></vue3-snackbar>
  </main>
</template>

<style lang="scss" scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 100vw;
  height: 100vh;

  .overlay {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.77);
    z-index: 10;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    width: 400px;
    height: 200px;
    background-color: #f3f3f3;
    border-radius: 10px;
    padding: 0 30px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: space-between;

    .close {
      position: absolute;
      top: 5%;
      right: 3%;
      cursor: pointer;
    }

    p {
      text-align: center;
      margin-bottom: 30px;
    }

    .btn-container {
      display: flex;
      justify-content: center;
      align-items: center;

      .btn {
        margin: 15px;
        padding: 10px 10px;
        background-color: #999;
        font-size: 20px;
        width: 100%;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }
    }
  }

  h1 {
    margin-top: 50px;
    margin-bottom: 16px;
    text-align: center;
  }

  .todo-list {
    display: flex;
    flex-direction: column;
    list-style: none;
    margin-top: 24px;
    gap: 20px;
  }

  .todos-msg {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-top: 24px;
  }
}
</style>
