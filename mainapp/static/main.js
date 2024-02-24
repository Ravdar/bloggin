var trendingArticlesButton = document.querySelector(".trending-button");
var trendingArticlesContainer = document.querySelector(".trending-articles");

trendingArticlesButton.addEventListener("click", function () {
    if (trendingArticlesButton.textContent === "+") {
        console.log("show");
        trendingArticlesContainer.style.maxHeight = "2000px";
        trendingArticlesContainer.style.padding = "10px";
        trendingArticlesContainer.style.transition = "1s ease-in-out";
        trendingArticlesButton.textContent = "-";
    }
    else {
        trendingArticlesContainer.style.maxHeight = "0";
        trendingArticlesContainer.style.padding = "0px";
        trendingArticlesContainer.style.transition = "0.5s ease-in-out";
        console.log("hide"); trendingArticlesButton.textContent = "+";
    }
})