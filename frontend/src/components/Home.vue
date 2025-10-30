<script setup>

const handleFileChange = (event) => {
  const file = event.target.files[0]

  if (!file) return
  
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
                <form enctype="multipart/form-data" method="post">
                    <input type="file" name="fileMRI"  id="fileMRI" class="form-control" @change="handleFileChange" required>
                <div class="papaya" data-params="params" id="ii"></div>
                <!--a class="mx-2" href="https://rii-mango.github.io/Papaya/"><i>built with Papaya.js</i></a-->
                <select class="form-select" aria-label="Default select example">
                    <option value="1">Brain Extraction</option>
                </select>
                <button class="btn btn-success" type="submit">run</button>
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
