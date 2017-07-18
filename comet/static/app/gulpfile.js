var gulp = require('gulp')

var plugins = require('gulp-load-plugins')();

var source = './src';
var destination = '../dist';

gulp.task('clean', function(){
    return gulp.src(destination + '/assets/css/*.css', {read: false})
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

gulp.task('minify', function () {
  return gulp.src(destination + '/assets/css/*.css')
    .pipe(plugins.csso())
    .pipe(plugins.rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(destination + '/assets/css/'));
});

gulp.task('build', ['clean', 'css', 'minify']);
// Tâche par défaut
gulp.task('default', ['build']);