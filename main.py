from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request
    file = request.files['file']

    # Save the file to a location on your server
    file.save('uploads/' + file.filename)

    # Call your Python function on the uploaded file
    result_file = process_file('uploads/' + file.filename)

    # Return the result file to the user for download
    return send_file(result_file, as_attachment=True)

# Define your Python function to process the file
def process_file(file_path):
    # Process the file here and return the path of the resulting file
    # You can customize this function based on your requirements
    # For demonstration purposes, let's assume it converts a text file to uppercase

    # Open the file and read its content
    with open(file_path, 'r') as f:
        content = f.read()

    # Convert the content to uppercase
    content = content.upper()

    # Create a new file with the processed content
    result_file_path = 'result/' + file_path.split('/')[-1]
    with open(result_file_path, 'w') as f:
        f.write(content)

    return result_file_path

if __name__ == '__main__':
    app.run(debug=True)




