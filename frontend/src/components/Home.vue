<script setup>
import MRIForm from './MRIForm.vue';
import PoolOfImages from './PoolOfImages.vue';
import SelectOperation from './SelectOperation.vue';
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
                <pool-of-images></pool-of-images>
            </div>
            <div class="col-12 col-md-10 col-xl-12">
                <select-operation></select-operation>
            </div>
            <div class="col-8">
                <m-r-i-form></m-r-i-form>
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
