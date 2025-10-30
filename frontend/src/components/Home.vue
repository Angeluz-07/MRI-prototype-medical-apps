<script setup>
import { ref } from 'vue';
import axios from 'axios';

// --- State Variables ---
const fileInputRef = ref(null); // Reference to the file input DOM element
const selectedFile = ref(null);
const selectedOption = ref(''); 
const isUploading = ref(false);
const message = ref('');
const messageClass = ref('');

// The endpoint URL on your Python backend
const API_ENDPOINT = 'http://localhost:8000/api/upload-and-process/'; 

// --- Methods ---

// Handles form submission
const handleSubmit = async () => {
  if (!selectedFile.value || !selectedOption.value) {
    message.value = 'Please select a file and a processing option.';
    messageClass.value = 'error';
    return;
  }

  isUploading.value = true;
  message.value = 'Uploading file...';
  messageClass.value = 'info';

  // 1. Create FormData object
  // This is crucial for correctly sending files and other form data in a single request.
  const formData = new FormData();
  
  // Append the file. 'file' is the name your backend will use to access the file (e.g., request.files['file']).
  formData.append('file', selectedFile.value); 
  console.log('file', selectedFile.value);
  // Append the selected option. 'option' is the name your backend will use to access this string value.
  formData.append('option', selectedOption.value); 
  console.log('option', selectedOption.value); 

  try {
    console.log("f", formData);
    console.log("--- Correctly Logging FormData Entries ---");

    // Use the entries() method and a for...of loop
    for (const [key, value] of formData.entries()) {
    // 'key' will be the field name (e.g., 'file', 'option')
    // 'value' will be the field content (File object or string)
    
    if (value instanceof File) {
        console.log(`Key: ${key}, Value: [File: ${value.name}, Type: ${value.type}, Size: ${value.size} bytes]`);
    } else {
        console.log(`Key: ${key}, Value: ${value}`);
    }
    }

    console.log("-----------------------------------------");
    return
    // cut here
    // 2. Send the request using axios
    const response = await axios.post(API_ENDPOINT, formData, {
      // It's good practice to explicitly set the Content-Type header, 
      // but Axios/browser often handle this automatically for FormData.
      headers: {
        'Content-Type': 'multipart/form-data', 
      },
      // You can also add an onUploadProgress callback here for a progress bar
    });

    // 3. Handle the successful (asynchronous) response
    const jobId = response.data.job_id; // Assuming your Python backend returns a job_id
    message.value = `File uploaded! Processing started. Job ID: ${jobId}. Now polling for results...`;
    messageClass.value = 'success';

    // Start polling or open a WebSocket connection here using the jobId
    // (See previous discussion on asynchronous workflows)

  } catch (error) {
    message.value = 'Upload failed. ' + (error.response?.data?.detail || error.message);
    messageClass.value = 'error';
  } finally {
    isUploading.value = false;
  }
};

const handleFileChange = (event) => {
  const file = event.target.files[0]

  // pre load the mri viewer
  const reader = new FileReader()
  
  reader.onload = (e) => {
    // Base64 string is available in e.target.result
    var myEncodedDataRef = e.target.result.split(',')[1];
    var params = [];
    params["encodedImages"] = [myEncodedDataRef];
    papaya.Container.resetViewer(0, params)
  }
  
  reader.onerror = (error) => {
    console.error('Error reading file:', error)
  }
  
  reader.readAsDataURL(file)

  // set file uploaded to send in form
  selectedFile.value = file
}
</script>


<template>
    <div class="container">
        <div class="row">
			<!-- Use entire width to display header -->
			<div class="col-sm-12">
				<div class="header stacked">
					<h1>My MRI Medical App</h1>
					<h6>App to load MRI images and display</h6>
				</div>
			</div>
		</div>
        <div id="main_content" class="row">
            <div class="col-12 col-md-10 col-xl-12">
           
            </div>
            <div class="col-8">
                <form enctype="multipart/form-data" method="post" @submit.prevent="handleSubmit" >
                <input type="file" name="fileMRI"  id="file" ref="fileInputRef" class="form-control" @change="handleFileChange" required>
                 
                <div class="papaya" data-params="params" id="ii"></div>
                <!--a class="mx-2" href="https://rii-mango.github.io/Papaya/"><i>built with Papaya.js</i></a-->
                <select 
                    id="option" 
                    class="form-select"
                    v-model="selectedOption" 
                    required
                >
                    <option value="" disabled>-- Select an option --</option>
                    <option value="fast">Fast Processing</option>
                    <option value="detailed">Detailed Analysis</option>
                    <option value="archive">Archive Only</option>
                </select>
                <!--button class="btn btn-success" type="submit">run</button-->
                <button class="btn btn-success" type="submit" :disabled="isUploading">
                    {{ isUploading ? 'Uploading...' : 'Start Processing' }}
                </button>
                <p v-if="message" :class="messageClass">{{ message }}</p>
                </form>
            </div>
            
            <div class="col-4" id="right_side_content">
                <h4>Features:</h4>
                <ul>
                <li>
                    Add image
                </li>
                <li>
                    Close All
                </li>
                <li>
                    Show header info, Show img info
                </li>
                <li>
                    Change color table
                </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
/*
 This is a custom class to 'stack' elements vertically and centered.
*/		
.stacked {
    display: flex;
    justify-content: center;
    align-items: center;		 
    flex-direction: column;
}

.header {
padding:2% 0%;/*set padding above and none in sides*/

color:white;
background-color:#3B4990;

}

#main_content {			
    margin: 2% ;
}
</style>
