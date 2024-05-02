<template>
  <ul>
    <li>
      <input
        type="checkbox"
        :checked="todo.isCompleted"
        @input="$emit('toggle-complete', todo.task_id)"
      />
      <div class="todo">
        <div v-if="todo.isEditing">
          <input type="text" v-model="currentTodo.title" />
          <input type="text" v-model="currentTodo.text" />
        </div>

        <div v-else>
          <h3 :class="{ 'completed-todo': todo.isCompleted }">
            {{ todo.title }}
          </h3>
          <span :class="{ 'completed-todo': todo.isCompleted }">
            {{ todo.text }}
          </span>
        </div>
      </div>

      <div class="todo-actions">
        <Icon
          v-if="todo.isEditing && currentTodo"
          icon="ph:check-circle"
          class="icon check-icon"
          color="41b080"
          width="22"
          @click="
            $emit(
              'update-todo',
              todo.task_id,
              currentTodo.title,
              currentTodo.text
            )
          "
        />
        <Icon
          v-if="todo.isEditing"
          icon="ph:arrow-counter-clockwise"
          class="icon arrow-icon"
          color="202020"
          width="22"
          @click="$emit('edit-todo', todo.task_id)"
        />
        <Icon
          v-if="!todo.isCompleted && !todo.isEditing"
          icon="ph:pencil-fill"
          class="icon edit-icon"
          color="41b080"
          width="22"
          @click="$emit('edit-todo', todo.task_id)"
        />
        <Icon
          icon="ph:trash"
          class="icon trash-icon"
          color="f95e5e"
          width="22"
          @click="$emit('delete-todo', todo.task_id)"
        />
      </div>
    </li>
  </ul>
</template>

<script setup>
import { ref } from 'vue'
import { Icon } from '@iconify/vue'
const props = defineProps({
  todo: {
    type: Object,
    required: true,
  }
})

const currentTodo = ref({})

defineEmits(['toggle-complete', 'edit-todo', 'update-todo', 'delete-todo'])
</script>

<style lang="scss" scoped>
ul {
  margin: 0 auto;
  width: 60vw;
}

li {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 10px;
  background-color: #f1f1f1;
  box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1),
    0 8px 10px -6px rgb(0 0 0 / 0.1);

  &:hover {
    .todo-actions {
      opacity: 1;
    }
  }

  input[type='checkbox'] {
    appearance: none;
    width: 20px;
    height: 20px;
    background-color: #fff;
    border-radius: 50%;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);

    &:checked {
      background-color: #41b080;
    }
  }

  .todo {
    display: flex;
    flex-direction: column;
    flex: 1;

    .completed-todo {
      text-decoration: line-through;
    }

    input[type='text'] {
      width: 100%;
      padding: 2px 6px;
      border: 2px solid #41b080;
    }
  }

  .todo-actions {
    display: flex;
    margin-right: 30px;
    gap: 6px;
    opacity: 0;
    transition: 150ms ease-in-out;
    .icon {
      cursor: pointer;
    }
  }
}

li > input {
  margin-left: 30px;
}
</style>
