+++
# Photo section

widget = "blank"  # Use a blank widget for custom content
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 3  # Order that this section will appear.

title = "Group Photos"
subtitle = ""

[design]
  view = 2  # Choose your preferred layout

[design.background]
  # You can customize the background and text color if needed

[advanced]
 css_style = ""
 css_class = ""
+++

<style>
    /* Container holding the images and the navigation */
    .slider {
        position: relative;
        width: 100%;
        max-width: 800px; /* Adjust based on your images' size */
        height: 500px;
    }

    /* Hide the radio inputs */
    .slider input {
        display: none;
    }

    /* The images */
    .slide {
        position: absolute;
        opacity: 0;
        transition: opacity 0.5s ease;
        width: 100%;
        height: 70vh; /* Adjust this value based on your needs */
        object-fit: cover; /* This will ensure the image covers the area, adjust as needed */
    }

    /* Show image when its corresponding input is checked */
    .slider input:checked + .slide {
        opacity: 1;
    }

    /* Navigation dots container */
    .navigation {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
    }

    /* Navigation dots */
    .navigation label {
        cursor: pointer;
        padding: 5px;
        background-color: #ccc;
        margin: 0 2px;
        border-radius: 50%;
    }

    /* Increase the dot size when its corresponding input is checked */
    .slider input:checked + label {
        background-color: #333;
    }
</style>


<div class="slider">
    <input type="radio" name="slide" id="slide1" checked>
    <img class="slide" src="files/group20241005.JPG">
    <input type="radio" name="slide" id="slide2">
    <img class="slide" src="files/group6.jpg">
    <input type="radio" name="slide" id="slide3">
    <img class="slide" src="files/group1.jpg">
    <input type="radio" name="slide" id="slide4">
    <img class="slide" src="files/group2.jpg">
    <input type="radio" name="slide" id="slide5">
    <img class="slide" src="files/group3.jpg">
    <input type="radio" name="slide" id="slide6">
    <img class="slide" src="files/group4.jpg">
    <input type="radio" name="slide" id="slide7">
    <img class="slide" src="files/group5.jpg">
    <div class="navigation">
        <label for="slide1"></label>
        <label for="slide2"></label>
        <label for="slide3"></label>
        <label for="slide4"></label>
        <label for="slide5"></label>
        <label for="slide6"></label>
        <label for="slide7"></label>
    </div>
</div>

