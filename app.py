from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import pandas as pd
import os
from werkzeug.utils import secure_filename
import io

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def merge_competency_data(csv1_data, csv2_data):
    """
    Merges competency assessment data from two dataframes.
    Returns tuple: (success, result_df or error_message)
    """
    try:
        # Automatically detect question columns
        question_columns = [col for col in csv1_data.columns if col.startswith('Q') and '_' in col]
        question_columns = [col for col in question_columns if col in csv2_data.columns]
        
        if len(question_columns) == 0:
            return False, "No matching question columns found between the two files."
        
        # Verify required columns exist
        if 'Raters Group' not in csv1_data.columns:
            return False, "'Raters Group' column not found in raw data file"
        
        if 'Desired_State' not in csv1_data.columns:
            return False, "'Desired_State' column not found in raw data file"
        
        if 'Desired State' not in csv2_data.columns:
            return False, "'Desired State' column not found in desired state mapping file"
        
        # Find rows where Raters Group = "Desired State"
        desired_state_mask = csv1_data['Raters Group'] == 'Desired State'
        
        updates_made = 0
        no_match_count = 0
        
        # Iterate through each row that needs updating
        for idx in csv1_data[desired_state_mask].index:
            desired_state_value = csv1_data.loc[idx, 'Desired_State']
            
            # Find matching row in CSV2
            matching_rows = csv2_data[csv2_data['Desired State'] == desired_state_value]
            
            if len(matching_rows) > 0:
                match = matching_rows.iloc[0]
                
                # Update question columns
                for col in question_columns:
                    csv1_data.loc[idx, col] = match[col]
                
                updates_made += 1
            else:
                no_match_count += 1
        
        summary = f"Successfully updated {updates_made} rows. No match found for {no_match_count} rows."
        return True, (csv1_data, summary)
        
    except Exception as e:
        return False, f"Error processing files: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_files():
    # Check if files are present
    if 'raw_data' not in request.files or 'desired_state' not in request.files:
        flash('Both files are required!', 'error')
        return redirect(url_for('index'))
    
    raw_data_file = request.files['raw_data']
    desired_state_file = request.files['desired_state']
    department = request.form.get('department')
    
    # Check if files are selected
    if raw_data_file.filename == '' or desired_state_file.filename == '':
        flash('Please select both files!', 'error')
        return redirect(url_for('index'))
    
    # Validate file types
    if not (allowed_file(raw_data_file.filename) and allowed_file(desired_state_file.filename)):
        flash('Only CSV files are allowed!', 'error')
        return redirect(url_for('index'))
    
    try:
        # Read CSV files
        csv1_data = pd.read_csv(raw_data_file)
        csv2_data = pd.read_csv(desired_state_file)
        
        # Process the data
        success, result = merge_competency_data(csv1_data, csv2_data)
        
        if not success:
            flash(result, 'error')
            return redirect(url_for('index'))
        
        result_df, summary = result
        
        # Create output file
        output = io.BytesIO()
        result_df.to_csv(output, index=False)
        output.seek(0)
        
        # Create filename based on department
        department_clean = department.replace(' ', '_')
        output_filename = f"{department_clean}_Competency_Assessment_Updated.csv"
        
        flash(summary, 'success')
        
        return send_file(
            output,
            mimetype='text/csv',
            as_attachment=True,
            download_name=output_filename
        )
        
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
