<script setup>
import MRIForm from './MRIForm.vue'
import PoolOfImages from './PoolOfImages.vue'
import SelectOperation from './SelectOperation.vue'
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
      <nav>
        <div class="nav nav-tabs my-2" id="nav-tab" role="tablist">
          <button
            class="nav-link active"
            id="nav-home-tab"
            data-bs-toggle="tab"
            data-bs-target="#nav-home"
            type="button"
            role="tab"
            aria-controls="nav-home"
            aria-selected="true"
          >
            Images
          </button>
          <button
            class="nav-link"
            id="nav-profile-tab"
            data-bs-toggle="tab"
            data-bs-target="#nav-profile"
            type="button"
            role="tab"
            aria-controls="nav-profile"
            aria-selected="false"
          >
            Operations
          </button>
          <button
            class="nav-link"
            id="nav-contact-tab"
            data-bs-toggle="tab"
            data-bs-target="#nav-contact"
            type="button"
            role="tab"
            aria-controls="nav-contact"
            aria-selected="false"
          >
            Results Viewer
          </button>
        </div>
      </nav>
      <div class="tab-content" id="nav-tabContent">
        <div
          class="tab-pane fade show active"
          id="nav-home"
          role="tabpanel"
          aria-labelledby="nav-home-tab"
        >
          <pool-of-images></pool-of-images>
        </div>
        <div
          class="tab-pane fade"
          id="nav-profile"
          role="tabpanel"
          aria-labelledby="nav-profile-tab"
        >
          <select-operation></select-operation>
        </div>
        <div
          class="tab-pane fade col-12"
          id="nav-contact"
          role="tabpanel"
          aria-labelledby="nav-contact-tab"
        >
          <m-r-i-form></m-r-i-form>
        </div>
      </div>


      <!--div class="col-4" id="right_side_content">
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
            </div-->
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
  padding: 2% 0%; /*set padding above and none in sides*/

  color: white;
  background-color: #3b4990;
}

#main_content {
  margin: 2%;
}
</style>
