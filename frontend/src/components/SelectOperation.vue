<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'

// 1. Reactive state variables
const items = ref([]) // To store the list of retrieved items
const formData = reactive({
  fileName: '',
  operation: '',
  // Add more properties for each form field
})

const message = ref(null)

// 2. Define the function to fetch data
const fetchItems = async () => {
  // A placeholder URL - **Replace this with your actual API endpoint**
  const API_URL = 'http://127.0.0.1:8080/mri/images'

  try {
    const response = await axios.get(API_URL)
    // Assuming the response data is an array of objects
    items.value = response.data.images
  } catch (err) {
    console.error('Error fetching data:', err)
  }
}

const handleSubmit = async () => {
  const API_ENDPOINT = 'http://127.0.0.1:8080/mri/segment-brain'
  try {
    message.value = 'processing'
    const response = await axios.post(API_ENDPOINT, formData)
    // 3. Handle the successful (asynchronous) response
    //const fname = response.data.filename
    message.value = 'success'
  } catch (error) {
    console.error('Error saving data:', error)
    message.value = 'error'
  }
}
// 3. Execute the function when the component is mounted (page load)
onMounted(() => {
  fetchItems()
})
</script>

<template>
  <h3>Operation</h3>
  <form class="row" enctype="multipart/form-data" method="post" @submit.prevent="handleSubmit">
    <div class="col-4">
      <select id="option" class="form-select" v-model="formData.fileName" required>
        <option value="" disabled>Select input image</option>
        <option :value="item" v-for="item in items" :key="item">
          {{ item }}
        </option>
      </select>
    </div>

    <div class="col-4">
      <select id="option" class="form-select" v-model="formData.operation" required>
        <option value="" disabled>Select operation</option>
        <option value="fast">Fast Processing</option>
        <option value="detailed">Detailed Analysis</option>
        <option value="archive">Archive Only</option>
      </select>
    </div>

    <div class="col-4">
      <button class="btn btn-success" type="submit">Run</button>
    </div>
  </form>
  <p v-if="message">{{ message }}</p>
</template>
<style scoped></style>
