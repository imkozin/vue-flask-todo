<script setup>
import { reactive, defineEmits } from 'vue'
import MyButton from './MyButton.vue'
import axios from 'axios'
// import { Vue3Snackbar } from "vue3-snackbar";
import { useSnackbar } from 'vue3-snackbar'
const snackbar = useSnackbar()

const emit = defineEmits(['create-todo'])

const todoState = reactive({
  title: '',
  text: '',
  invalid: false,
  errMsg: '',
})

const addTodo = async () => {
  const todo = { title: todoState.title, text: todoState.text }
  todoState.invalid = false

  try {
    const response = await axios.post(
      'http://localhost:8000/api/add-task',
      todo
    )
    if (todoState.title.trim() !== '' && todoState.text.trim() !== '') {
      emit('create-todo', todo)
      todoState.title = ''
      todoState.text = ''
      todoState.errMsg = ''
      snackbar.add({
      type: 'success',
      text: response.data.message,
    })
    }
  } catch (error) {
    todoState.errMsg = error.response.data.error
    todoState.invalid = true
    console.error('Error creating todo:', error)
  }
}
</script>

<template>
  <form class="form-wrap" @submit.prevent="addTodo()">
    <input
      class="input-field"
      :class="{ 'input-err': todoState.invalid }"
      type="text"
      v-model="todoState.title"
      placeholder="Title"
    />

    <textarea
      class="input-field"
      :class="{ 'input-err': todoState.invalid }"
      type="text"
      placeholder="Text"
      v-model="todoState.text"
    ></textarea>
    <div class="button-container">
      <p v-show="todoState.invalid" class="err-msg">{{ todoState.errMsg }}</p>
      <MyButton type="submit" />
    </div>
  </form>
</template>

<style lang="scss" scoped>
.form-wrap {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 600px;
  margin: 0 auto;
  padding: 10px;
  transition: 250ms ease;
  border-radius: 5px;
  box-shadow: 0 10px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);

  &:focus-within {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 3px 10px 0 rgba(0, 0, 0, 0.19);
  }

  .input-field {
    display: block;
    width: 100%;
    padding: 8px 6px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;

    &:focus {
      outline: none;
    }

    &.input-err {
      border-color: red;
    }
  }

  .button-container {
    width: 100%;
    height: 50px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .err-msg {
    position: absolute;
    left: 0;
    top: 0;
    font-size: 12px;
    text-align: center;
    color: red;
  }
}
</style>
