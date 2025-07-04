from app import create_app
import sass

sass.compile(dirname=('app/static/scss', 'app/static/css'), output_style='compressed')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
