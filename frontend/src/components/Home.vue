<script setup>
</script>

<template>
    <div class="container">
        <div id="" class="row">
            <h1>My medical App</h1>
        </div>
        <div id="main_content" class="row">
            <div class="col-8">
                <div class="papaya" data-params="params"></div>
                <a class="mx-2" href="https://rii-mango.github.io/Papaya/"><i>built with Papaya.js</i></a>
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

</style>
