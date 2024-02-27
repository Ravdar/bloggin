// GENERAL FUNCTIONS

// Showing and hidding window on button click
function showHideContainer(showHideButton, affectedContainer) {
    if (showHideButton.textContent === "+") {
        affectedContainer.style.maxHeight = "2000px";
        affectedContainer.style.padding = "15px";
        showHideButton.textContent = "-";
    }
    else {
        affectedContainer.style.maxHeight = "0";
        affectedContainer.style.padding = "0";
        console.log("hide"); showHideButton.textContent = "+";
    }
}

// Making trending section responsive
var trendingArticlesButton = document.querySelector(".trending-button");
var trendingArticlesContainer = document.querySelector(".trending-articles");

if (trendingArticlesButton) {
    trendingArticlesButton.addEventListener("click", function () {
        showHideContainer(trendingArticlesButton, trendingArticlesContainer);
    })
};


// NEW ARTICLE PAGE

// Show and hide topics checkboxes
var showTopicsButton = document.getElementById("show-topics");
var topicsContainer = document.querySelector(".available-topics");

if (showTopicsButton) {
    showTopicsButton.addEventListener("click", function () { showHideContainer(showTopicsButton, topicsContainer) })
};



