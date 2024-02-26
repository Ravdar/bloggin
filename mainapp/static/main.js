// GENERAL FUNCTIONS

// Showing and hidding window on button click
function showHideContainer(showHideButton, affectedContainer) {
    if (showHideButton.textContent === "+") {
        affectedContainer.style.maxHeight = "2000px";
        affectedContainer.style.transition = "maxHeight 1s ease-in-out";
        showHideButton.textContent = "-";
    }
    else {
        affectedContainer.style.maxHeight = "0";
        affectedContainer.style.transition = " maxHeight 0.5s ease-in-out";
        console.log("hide"); showHideButton.textContent = "+";
    }
}

// Making trending section responsive
var trendingArticlesButton = document.querySelector(".trending-button");
var trendingArticlesContainer = document.querySelector(".trending-articles");

trendingArticlesButton.addEventListener("click", function () {
    showHideContainer(trendingArticlesButton, trendingArticlesContainer);
});


// NEW ARTICLE PAGE

// Show and hide topics checkboxes
var showTopicsButton = document.getElementById("show-topics");
var topicsContainer = document.querySelector(".available-topics");

showTopicsButton.addEventListener("click", function () { showHideContainer(showTopicsButton, topicsContainer) });



