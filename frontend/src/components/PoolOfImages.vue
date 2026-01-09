<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'

// 1. Reactive state variables
const items = ref([]) // To store the list of retrieved items
const formData = reactive({
  fileMRI: '',
  // Add more properties for each form field
})

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
  const API_ENDPOINT = 'http://127.0.0.1:8080/mri/images'
  try {
    const response = await axios.post(API_ENDPOINT, formData, {
      // It's good practice to explicitly set the Content-Type header,
      // but Axios/browser often handle this automatically for FormData.
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      // You can also add an onUploadProgress callback here for a progress bar
    })
    fetchItems()

    // 3. Handle the successful (asynchronous) response
    //const fname = response.data.filename
  } catch (error) {
    console.error('Error saving data:', err)
  }
}
const handleFileChange = (event) => {
  const file = event.target.files[0]
  formData.fileMRI = file
}
// 3. Execute the function when the component is mounted (page load)
onMounted(() => {
  fetchItems()
})
</script>

<template>
  <!--h3>Images</h3-->
  <form class="row" enctype="multipart/form-data" method="post" @submit.prevent="handleSubmit">
    <div class="col-6">
      <input
        type="file"
        name="fileMRI"
        id="file"
        ref="fileInputRef"
        class="form-control"
        @change="handleFileChange"
        required
      />
    </div>
    <div class="col-6">
      <button class="btn btn-success" type="submit">Upload</button>
    </div>
  </form>
  <div class="row">
    <div class="card col-8 m-2">
      <ul v-if="items.length">
        <li v-for="item in items" :key="item" class="item-card">
          {{ item }}
        </li>
      </ul>
      <p v-else>No items found.</p>
    </div>
  </div>
</template>

<style scoped></style>
