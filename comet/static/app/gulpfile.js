var gulp = require('gulp')

var plugins = require('gulp-load-plugins')();

var source = './src';
var destination = '../dist';

gulp.task('clean', function(){
    return gulp.src([destination + '/assets/css/*.css', destination + '/assets/js/*.js' ], {read: false})
        .pipe(plugins.clean({force: true}));
});

gulp.task('css', function() {
    return gulp.src(source + '/assets/css/*.less')
    .pipe(plugins.less())
    .pipe(plugins.csscomb())
    .pipe(plugins.cssbeautify({indent: '  '}))
    .pipe(plugins.autoprefixer())
    .pipe(gulp.dest(destination + '/assets/css/'));
});

gulp.task('js', function() {
    return gulp.src(source + '/assets/js/*.js')
        .pipe(plugins.concat('app.js'))
        .pipe(gulp.dest(destination + '/assets/js/'));
});

gulp.task('build', ['clean', 'css', 'js']);

gulp.task('default', ['build']);