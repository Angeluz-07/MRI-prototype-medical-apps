<script setup>
import { reactive, ref, inject, onMounted, computed, toRaw } from 'vue'
import axios from 'axios'
import FakeService from '@/services/FakeService'

// --- State Variables ---
const items = ref([]) // To store the list of retrieved items
const imageList = ref([])
const isLoadingInitialList = ref(true)
const fetchInitialIds = async () => {
  isLoadingInitialList.value = true

  // 💡 REPLACE THIS WITH YOUR ACTUAL ENDPOINT
  const API_URL = 'http://127.0.0.1:8080/mri/images'
  const INITIAL_API_ENDPOINT = 'http://127.0.0.1:8080/mri/images'

  try {
    // --- SIMULATION ---
    // Simulate API call returning a list of strings (IDs)
    const response = await axios.get(INITIAL_API_ENDPOINT)
    const rawIds = response.data.images
    //const rawIds = ['img_001', 'img_002', 'img_003', 'img_004'];
    // --- END SIMULATION ---

    // **CRITICAL STEP:** Map the raw ID strings into the structured object array
    imageList.value = rawIds.map((id) => ({
      id: id,
      selected: false,
      strValue: null,
      isFetching: false, // Temporary flag to prevent double-clicks during fetch
    }))
  } catch (error) {
    console.error('Error fetching initial IDs:', error)
  } finally {
    isLoadingInitialList.value = false
  }
}

// Fetch the IDs when the component mounts
onMounted(() => {
  fetchInitialIds()
})

// --- 3. Subsequent Value Fetch Simulation (Unchanged) ---

const fetchStringValue = async (id) => {
  // Replace this with your actual API endpoint and logic for the single value
  const INITIAL_API_ENDPOINT = 'http://127.0.0.1:8080/mri/images'
  const API_ENDPOINT = `http://127.0.0.1:8080/mri/images/${id}`
  console.log(`📡 Hitting endpoint: ${API_ENDPOINT}`)

  try {
    // Simulate network delay and data response
    await new Promise((resolve) => setTimeout(resolve, 500))
    const response = await axios.get(API_ENDPOINT)
    return response.data.basestr
  } catch (error) {
    console.error(`Error fetching strValue for ${id}:`, error)
    return null
  }
}

const toggleImageSelection = async (id, isChecked) => {
  const index = imageList.value.findIndex((img) => img.id === id)
  if (index === -1) return

  const image = imageList.value[index]

  // 1. Update the selection status
  image.selected = isChecked

  // 2. Conditional Fetch Logic: Only if selected AND value is missing
  if (isChecked && !image.strValue) {
    if (image.isFetching) return

    image.isFetching = true

    const value = await fetchStringValue(id)

    // 3. Update the strValue if successful
    if (value) {
      imageList.value[index].strValue = value
    }

    image.isFetching = false
  }
  var params = []
  params['showControlBar'] = true
  params['images'] = rawStringValues.value
  console.log(params['encodedImages'])
  papaya.Container.resetViewer(0, params)
}

const selectedData = computed(() => {
  return imageList.value
    .filter((image) => image.selected)
    .map((image) => ({
      id: image.id,
    }))
})

const selectedDataAll = computed(() => {
  return imageList.value
    .filter((image) => image.selected)
    .map((image) => ({
      id: image.id,
      strValue: `data:image/nifti;base64,${image.strValue}`,
    }))
})

const rawStringValues = computed(() => {
  // 1. Get the current value of the computed property (which is an array of objects)
  const data = selectedDataAll.value

  // 2. Use Vue's toRaw() utility to strip the Proxy/Ref wrapper if needed.
  //    This is crucial for ensuring you get a standard JS object/array.
  const rawArray = toRaw(data)
  console.log
  // 3. Map the raw array to extract ONLY the strValue
  return rawArray.map((item) => item.strValue)
  // Optional: Filter out any null values if a fetch failed
  //.filter(str => str !== null);
})

// This array will store the IDs of the selected items
const selectedItems = ref([])

// Function to handle checkbox changes and update selectedItems
const handleCheckboxChange = (item) => {
  if (item) {
    selectedItems.value.push(item)
  } else {
    const index = selectedItems.value.indexOf(item)
    if (index > -1) {
      selectedItems.value.splice(index, 1)
    }
  }
  console.log(selectedItems)
}
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

  // const result = FakeService.process(formData)
  // formStatus.isUploading = false
  // formStatus.message = 'Successfully sent'
  // formStatus.messageClass = 'success'

  console.log('Form Data is ready here!', formData)

  const API_ENDPOINT = 'http://127.0.0.1:8000/mri/segment-brain'
  try {
    const response = await axios.post(API_ENDPOINT, formData, {
      // It's good practice to explicitly set the Content-Type header,
      // but Axios/browser often handle this automatically for FormData.
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      // You can also add an onUploadProgress callback here for a progress bar
    })

    // 3. Handle the successful (asynchronous) response
    const fname = response.data.filename
    formStatus.message = `File uploaded!  fname: ${fname}.`
    formStatus.messageClass = 'success'
  } catch (error) {
    message.value = 'Upload failed. ' + (error.response?.data?.detail || error.message)
    messageClass.value = 'error'
  } finally {
    formStatus.isUploading = false
  }
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
  <h3>Viewer</h3>
  <div class="row">

    <div class="col-4">
      <h5>Image List Selector</h5>
      <div v-if="isLoadingInitialList">Loading image IDs...</div>
      <ul v-else class="image-list overflow-x">
        <li v-for="image in imageList" :key="image.id" class="list-item">
          <input
            type="checkbox"
            :id="`checkbox-${image.id}`"
            :checked="image.selected"
            @change="toggleImageSelection(image.id, $event.target.checked)"
          />
          <label :for="`checkbox-${image.id}`">
            {{ image.id }}
            <span v-if="image.strValue" class="fetched-indicator"> (Value Present)</span>
          </label>
        </li>
      </ul>
    </div>
    <div class="col-8">
      <div class="papaya" data-params="params" id="ii"></div>
    </div>

    <!--div class="selected-data">
      <h3>Selected Image Data (IDs and String Values)</h3>
      <pre>{{ selectedData }}</pre>
    </div-->
  </div>

  <!--a class="mx-2" href="https://rii-mango.github.io/Papaya/"><i>built with Papaya.js</i></a-->
  <!--select id="option" class="form-select" v-model="formData.operation" required>
      <option value="" disabled>-- Select an option --</option>
      <option value="fast">Fast Processing</option>
      <option value="detailed">Detailed Analysis</option>
      <option value="archive">Archive Only</option>
    </select-->

  <!--button class="btn btn-success" type="submit">run</button-->
  <!--button class="btn btn-success" type="submit" :disabled="formStatus.isUploading">
    {{ formStatus.isUploading ? 'Uploading...' : 'Start Processing' }}
  </button-->
  <p v-if="formStatus.message" :class="formStatus.messageClass">{{ formStatus.message }}</p>
</template>

<style scoped></style>
