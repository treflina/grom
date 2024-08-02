const gulp = require("gulp");
const browserSync = require("browser-sync");
const reload = browserSync.reload;

gulp.task("default", function () {
    browserSync.init({
        notify: false,
        proxy: "localhost:8000",
    });
    gulp.watch(["./**/*.{scss,css,html,py,js}"], reload);
});
