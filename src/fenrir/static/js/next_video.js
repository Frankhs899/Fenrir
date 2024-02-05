var animeVideo = document.getElementById("animeVideo");

animeVideo.addEventListener("ended", function () {
    // Redirige a la página "next_chapter" de Django
    var nextChapterLink = document.getElementById("nextChapterLink");
    if (nextChapterLink) {
        window.location.href = nextChapterLink.href;
    }
});