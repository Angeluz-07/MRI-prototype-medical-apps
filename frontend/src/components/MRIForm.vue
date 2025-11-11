<script setup>
import { reactive, ref, inject } from 'vue'
import axios from 'axios'
import FakeService from '@/services/FakeService'

// --- State Variables ---

const formData = reactive({
  fileMRI: '',
  operation: '',
  // Add more properties for each form field
})

const formStatus = reactive({
  message: null,
  messageClass: null,
  isUploading: false,
})

// --- Methods ---
// Handles form submission
const handleSubmit = async () => {
 
  formStatus.isUploading = true
  formStatus.message = 'Uploading file...'
  formStatus.messageClass = 'info'

const result = FakeService.process(formData);
formStatus.isUploading=false
formStatus.message = "Successfully sent"
formStatus.messageClass = 'success'

  //console.log('Form Data is ready here!', formData)

  //   // 1. Create FormData object

  //   try {
  //     // 2. Send the request using axios
  //     const response = await axios.post(API_ENDPOINT, formData, {
  //       // It's good practice to explicitly set the Content-Type header,
  //       // but Axios/browser often handle this automatically for FormData.
  //       headers: {
  //         'Content-Type': 'multipart/form-data',
  //       },
  //       // You can also add an onUploadProgress callback here for a progress bar
  //     })

  //     // 3. Handle the successful (asynchronous) response
  //     const jobId = response.data.job_id // Assuming your Python backend returns a job_id
  //     message.value = `File uploaded! Processing started. Job ID: ${jobId}. Now polling for results...`
  //     messageClass.value = 'success'

  //     // Start polling or open a WebSocket connection here using the jobId
  //     // (See previous discussion on asynchronous workflows)
  //   } catch (error) {
  //     message.value = 'Upload failed. ' + (error.response?.data?.detail || error.message)
  //     messageClass.value = 'error'
  //   } finally {
  //     isUploading.value = false
  //   }
}

const loadImgToPapayaViewer = (event) => {
  const file = event.target.files[0]

  // pre load the mri viewer
  const reader = new FileReader()

  reader.onload = (e) => {
    // Base64 string is available in e.target.result
    var myEncodedDataRef = e.target.result.split(',')[1]
    var params = []
    params['encodedImages'] = [myEncodedDataRef]
    papaya.Container.resetViewer(0, params)
  }

  reader.onerror = (error) => {
    console.error('Error reading file:', error)
  }

  reader.readAsDataURL(file)
}

const loadImgToFormData = (event) => {
  const file = event.target.files[0]
  formData.fileMRI = file
}

const handleFileChange = (event) => {
  loadImgToPapayaViewer(event)
  loadImgToFormData(event)
}
</script>

<template>
  <form enctype="multipart/form-data" method="post" @submit.prevent="handleSubmit">
    <input
      type="file"
      name="fileMRI"
      id="file"
      ref="fileInputRef"
      class="form-control"
      @change="handleFileChange"
      required
    />

    <div class="papaya" data-params="params" id="ii"></div>

    <!--a class="mx-2" href="https://rii-mango.github.io/Papaya/"><i>built with Papaya.js</i></a-->
    <select id="option" class="form-select" v-model="formData.operation" required>
      <option value="" disabled>-- Select an option --</option>
      <option value="fast">Fast Processing</option>
      <option value="detailed">Detailed Analysis</option>
      <option value="archive">Archive Only</option>
    </select>

    <!--button class="btn btn-success" type="submit">run</button-->
    <button class="btn btn-success" type="submit" :disabled="formStatus.isUploading">
      {{ formStatus.isUploading ? 'Uploading...' : 'Start Processing' }}
    </button>
    <p v-if="formStatus.message" :class="formStatus.messageClass">{{ formStatus.message }}</p>
  </form>
</template>

<style scoped></style>
