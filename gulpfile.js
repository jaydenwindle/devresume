var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');

var input = './**/*.scss';
var output = './devresume/static/css';
var sassOptions = {
    errLogToConsole: true,
    outputStyle: 'expanded',
    includePaths: './node_modules/bootstrap-sass/assets/stylesheets'
};

gulp.task('sass', function () {
    return gulp
    // Find all `.scss` files from the `stylesheets/` folder
    .src([input, '!node_modules/**/*'])
    // Run Sass on those files
    .pipe(sass(sassOptions))
    // Write the resulting CSS in the output folder
    .pipe(concat("style.css"))
    .pipe(gulp.dest(output));

});
