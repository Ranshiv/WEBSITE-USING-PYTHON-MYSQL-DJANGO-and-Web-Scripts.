from website import create_app
app = create_app()

if __name__ == '__main__':
    #used debug so that whenever a change is made in py code , website automatically rerun the web server.
    app.run(debug=True)
    #if we get running on https-----:localhost , that means our web server is working
